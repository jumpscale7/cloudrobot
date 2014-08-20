from JumpScale import j

from .FileRobot import FileRobot

import JumpScale.baselib.redis
import ujson as json
import time

import JumpScale.grid.osis

import sys

class Empty():
    pass

class CloudRobotFactory(object):
    def __init__(self):
        self.hrd=None
        
    def init(self):
        return self._init()

    def _init(self):
        j.cloudrobot=Empty()
        j.cloudrobot.vars={}
        j.cloudrobot.verbosity=2

        self.redisq_xmpp=j.clients.redis.getRedisQueue("127.0.0.1", 7768,"xmpp")
        ppath="%s/apps/cloudrobot/"%j.dirs.baseDir
        if ppath not in sys.path:
            sys.path.append(ppath)
        import robots
        self.robots=robots
        if self.hrd==None:
            raise RuntimeError("hrd not specified yet.")
        osisinstance=self.hrd.get("cloudrobot.osis.connection")
        self.osis =j.core.osis.getClientByInstance(osisinstance)        
        self.osis_robot_job = j.core.osis.getClientForCategory(self.osis, 'robot', 'job')        
        self.osis_oss_user = j.core.osis.getClientForCategory(self.osis, 'oss', 'user')
        self.osis_system_user = j.core.osis.getClientForCategory(self.osis, 'system', 'user')
        self.redis=j.clients.redis.getRedisClient("127.0.0.1", 7768)
        self.domain=self.hrd.get("cloudrobot.mail.domain")


    def startMailServer(self,robots={}):
        self._init()
        from .MailRobot import MailRobot
        robot = MailRobot(('0.0.0.0', 25),hrd_instance=self.hrd)
        robot.robots=robots
        print "start server on port:25"
        robot.serve_forever()

    def startHTTP(self, addr='0.0.0.0', port=8099,robots={}):
        self._init()
        from .HTTPRobot import HTTPRobot
        robot=HTTPRobot(addr=addr, port=port)
        robot.robots=robots
        robot.start()

    def startXMPPRobot(self,username,passwd,robots={}):
        self._init()
        from .XMPPRobot import XMPPRobot        
        robot=XMPPRobot(username=username, passwd=passwd)
        robot.robots=robots
        robot.init()     

    def startFileRobot(self,robots={}):
        self._init()
        robot=FileRobot()
        robot.robots=robots
        robot.start()

    def job2redis(self,job):
        q=self._getQueue(job)
        data=json.dumps(job.obj2dict())
        self.redis.hset("robot:jobs",job.guid,data)   
        print "job:%s to redis"%job.guid
        if job.end<>0:
            n=j.base.time.getTimeEpoch()
            print "QUEUE OK"
            q.put(str(n))
            q.set_expire(n+120)

    def jobWait(self,jobguid):
        q=j.clients.redis.getGeventRedisQueue("127.0.0.1", 7768, "robot:queues:%s" % jobguid)
        print "wait for job:%s"%jobguid
        # while q.empty():
        #     print "queue empty for %s"%jobguid
        #     time.sleep(0.1)
        jobguid=q.get()
        return 
        
    def _getQueue(self,job):    
        queue=j.clients.redis.getGeventRedisQueue("127.0.0.1", 7768, "robot:queues:%s" % job.guid)
        return queue

    def toFileRobot(self,channel,msg,mailfrom,rscriptname,args={},userid=None):
        
        # msg=j.tools.text.toAscii(msg)

        if msg.strip()=="":
            raise RuntimeError("Cannot be empty msg")

        if msg[-1]<>"\n":
            msg+="\n"
        
        robotdir=j.system.fs.joinPaths(j.dirs.varDir, 'cloudrobot', channel)
        if not j.system.fs.exists(path=robotdir):
            msg = 'Could not find robot for channel \'%s\' on fs. Please make sure you are sending to the right one, \'youtrack\' & \'machine\' & \'user\' are supported.'%channel
            raise RuntimeError("E:%s"%msg)

        args["msg_subject"]=rscriptname
        args["msg_email"]=mailfrom
        args["msg_channel"]=channel

        if userid<>None:
            args["msg_userid"]=userid

        subject2=j.tools.text.toAscii(args["msg_subject"],80)
        fromm="%s@%s"%(channel,self.domain)
        fromm2=j.tools.text.toAscii(fromm)
        filename="%s_%s.py"%(fromm2,subject2)

        cl=self.osis_robot_job

        job = cl.new()
        job.start = j.base.time.getTimeEpoch()
        job.rscript_name = rscriptname
        job.rscript_content = msg
        job.rscript_channel = channel
        job.state = "PENDING"
        job.onetime = True
        if userid<>None:
            job.user=userid
        else:
            job.user = self.getUserGuidOrEmail(mailfrom)
        guid,tmp, tmp = cl.set(job)

        args["msg_jobguid"]=job.guid

        premsg=""
        for key in args.keys():
            premsg+="@%s=%s\n"%(key,args[key])
        msg="%s\n%s\n"%(premsg,msg)

        self.job2redis(job)

        path=j.system.fs.joinPaths(j.dirs.varDir, 'cloudrobot', channel,'in',filename)
        

        j.system.fs.writeFile(path,msg)

        return guid


    def getUserGuidOrEmail(self,email):
        if email.find("<")<>-1:
            email=email.split("<",1)[1]
            email=email.split(">",1)[0]        
        return email        
        
    def getUserIdFromXmpp(self,xmpp=""):
        if self.redis.hexists("cloudrobot:users:xmpp",xmpp):
            #found the user
            userid=self.redis.hget("cloudrobot:users:xmpp",xmpp)
        else:
            res=self.osis_system_user.simpleSearch({"xmpp":xmpp})
            if len(res)==0:
                j.events.inputerror_critical("Could not find user with xmpp login:%s"%xmpp,"xmpp.auth")
            if len(res)>1:
                j.events.inputerror_critical("Found more than 1 user with xmpp login:%s"%xmpp,"xmpp.auth")
            userid=res[0]["id"]
            userid=self.redis.hset("cloudrobot:users:xmpp",xmpp,userid)
        return userid
            
    def getUserState(self,userid):
        default={"state":"","session":"0","moddate":j.base.time.getTimeEpoch(),"retchannel":"xmpp","loglevel":5,"channel":"ms1_iaas"}
        if not self.redis.hexists("cloudrobot:users:state",userid):            
            self.redis.hset("cloudrobot:users:state",userid,json.dumps(default))
        data=json.loads(self.redis.hget("cloudrobot:users:state",userid))
        if not data.has_key("loglevel") or not data.has_key("retchannel") or not data.has_key("channel"):
            self.redis.hset("cloudrobot:users:state",userid,json.dumps(default))
            data=json.loads(self.redis.hget("cloudrobot:users:state",userid))
        return data

    def sendUserMessage(self,userid,msg,html=False):        
        state=self.getUserState(userid)
        user=self.getUserObject(userid)
        if state["retchannel"]=="xmpp":
            for xmpp in user["xmpp"]:
                if html:
                    self.redisq_xmpp.put("2:%s:%s"%(xmpp,str(msg)))
                else:
                    self.redisq_xmpp.put("1:%s:%s"%(xmpp,str(msg)))

    def getUserObject(self,userid):
        if not self.redis.hexists("cloudrobot:users:obj",userid):
            res=self.osis_system_user.simpleSearch({"id":userid})
            if len(res)==0:
                j.events.inputerror_critical("Could not find user with id:%s"%userid,"cloudrobot.auth")            
            user=self.osis_system_user.get(res[0]["guid"])
            self.redis.hset("cloudrobot:users:obj",userid,json.dumps(user.__dict__))
        obj=json.loads(self.redis.hget("cloudrobot:users:obj",userid))
        return obj

    def getUserSessionId(self,userid):
        state=self.getUserState(userid)
        return state["session"]

    def setUserSessionId(self,userid,session):
        state=self.getUserState(userid)
        state["session"]=session
        self.redis.hset("cloudrobot:users:state",userid,json.dumps(state))

    def setUserSessionState(self,userid,sessionstate):
        state=self.getUserState(userid)
        state["state"]=sessionstate
        self.redis.hset("cloudrobot:users:state",userid,json.dumps(state))

    def setUserSessionLoglevel(self,userid,loglevel):
        state=self.getUserState(userid)
        state["loglevel"]=int(loglevel)
        self.redis.hset("cloudrobot:users:state",userid,json.dumps(state))

    def setUserSessionChannel(self,userid,channel):
        state=self.getUserState(userid)
        state["channel"]=channel
        self.redis.hset("cloudrobot:users:state",userid,json.dumps(state))

    def getUserGlobals(self,userid):
        state=self.getUserState(userid)
        key="%s_%s"%(userid,state["session"])
        if not self.redis.hexists("cloudrobot:users:globals",key):
            self.redis.hset("cloudrobot:users:globals",key,json.dumps({}))
        gglobals=json.loads(self.redis.hget("cloudrobot:users:globals",key))
        return gglobals

    def setUserGlobals(self,userid,args={}):
        key="%s_%s"%(userid,self.getUserSessionId(userid))
        gglobals=self.getUserGlobals(userid)
        gglobals.update(args)

        for item in ["msg_jobguid"]:
            if gglobals.has_key(item):
                gglobals.pop(item)
        self.redis.hset("cloudrobot:users:globals",key,json.dumps(gglobals))

    def clearUserGlobals(self,userid):
        key="%s_%s"%(userid,self.getUserSessionId(userid))
        self.redis.hset("cloudrobot:users:globals",key,json.dumps({}))
