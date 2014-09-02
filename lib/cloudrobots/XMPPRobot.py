from JumpScale import j

import JumpScale.grid.osis
import JumpScale.baselib.redisworker
import JumpScale.lib.html
import JumpScale.lib.cloudrobots
import JumpScale.baselib.redis
import ujson as json

import datetime

import sleekxmpp

import sys

if sys.version_info < (3, 0):
    reload(sys)
    sys.setdefaultencoding('utf8')
else:
    raw_input = input

class XMPPRobot(sleekxmpp.ClientXMPP):
    def __init__(self, username, passwd):
        self.robots = {}
        # self.osis = j.core.osis.getClient(user='root')
        # self.osis_job = j.core.osis.getClientForCategory(self.osis, 'robot', 'job')
        self.login_username=username
        self.login_passwd=passwd
        sleekxmpp.ClientXMPP.__init__(self, username, passwd)

        # The session_start event will be triggered when
        # the bot establishes its connection with the server
        # and the XML streams are ready for use. We want to
        # listen for this event so that we we can initialize
        # our roster.
        self.add_event_handler("session_start", self.start)

        # The message event is triggered whenever a message
        # stanza is received. Be aware that that includes
        # MUC messages and error messages.
        self.add_event_handler("message", self.message)

        self.register_plugin('xep_0030') # Service Discovery
        # self.register_plugin('xep_0004') # Data Forms
        self.register_plugin('xep_0060') # PubSub
        self.register_plugin('xep_0199') # XMPP Ping        

        self.redis=j.clients.redis.getRedisClient("127.0.0.1", 7768)
        self.redisq=j.clients.redis.getRedisQueue("127.0.0.1", 7768,"xmpp")

    def init(self):

        conn=self.connect()
        # conn=self.connect(('talk.google.com', 5222))
        if conn==False:
            raise RuntimeError("Cannot connect xmpp")        

        res=self.process(block=True)

    def start(self, event):
        """
        Process the session_start event.

        Typical actions for the session_start event are
        requesting the roster and broadcasting an initial
        presence stanza.

        Arguments:
            event -- An empty dictionary. The session_start
                     event does not provide any additional
                     data.
        """        
        print "STARTED"
        print "get presense"
        self.send_presence()
        print "get roster"
        self.get_roster()
        
        self.scheduler.add("checkback",0.1,self.checkReturn,repeat=True)

        # sleekxmpp.xmlstream.scheduler.Task(name, seconds, callback, args=None, kwargs=None, repeat=False, qpointer=None)[source]
        
        # for i in range(10):
        #     self.send_message(mto="despiegk@jabb3r.net",mbody="test",mtype='chat')

    def checkReturn(self,*args,**kwargs):
        res=self.redisq.get_nowait()
        while res<>None:
            if res.find(":")<>-1:
                ttype,to,msg=res.split(":",2)
                if int(ttype)==1:
                    self.send_message(mto=to,mbody=msg,mtype='chat')
                elif int(ttype)==2:
                    msg0=j.tools.html.html2text(msg)
                    self.send_message(mto=to,mbody=msg0,mhtml=msg,mtype='chat')
            res=self.redisq.get_nowait()

    def message(self, msg):
        """
        Process incoming message stanzas. Be aware that this also
        includes MUC messages and error messages. It is usually
        a good idea to check the messages's type before processing
        or sending replies.

        Arguments:
            msg -- The received message stanza. See the documentation
                   for stanza objects and the Message stanza to see
                   how it may be used.
        """

        def sendState(userid):
            state=j.servers.cloudrobot.getUserState(userid)
            # state.pop("moddate")
            hrddata=j.db.serializers.hrd.dumps(state)
            j.servers.cloudrobot.sendUserMessage(userid,"state:\n%s"%hrddata)

        ffrom=str(msg["from"]).split("/")[0]
        
        try:
            userid=j.servers.cloudrobot.userIdGetFromXmpp(ffrom)
            session=j.servers.cloudrobot.sessionGet(userid)
            if "xmpp" not in session.retchannels:
                session.retchannels.append["xmpp"]
                session.save()                    

        except Exception,e:
            self.redisq.put("1:%s:Error:%s"%(ffrom,str(e)))
            return

        if msg['type'] in ('chat', 'normal'):

            try:
                body=msg["body"]
                if body.find("session")==0:
                    body=body.replace("session","")
                    sessionname=body.strip().strip(":=").strip()
                    if sessionname=="":
                        sessionname=j.servers.cloudrobot.getUserSession(userid)
                    else:
                        j.servers.cloudrobot.setUserSession(userid,sessionname) 
                    session.sendUserMessage("your current session:%s\n"%sessionname)
                    return
                
                session.process(body,channel=None,scriptname="xmpp",args={})

            except Exception,e:
                self.redisq.put("1:%s:Error:%s"%(ffrom,str(e)))
                return


