from JumpScale import j

from .FileRobot import FileRobot

import JumpScale.baselib.redis
import ujson as json
import time
import JumpScale.baselib.redisworker
import JumpScale.grid.osis
import yaml
import sys
from OSISObjManipulatorClass import OSISObjManipulatorClass

class Empty():
    pass

class Session():
    def __init__(self,ddict={}):
        if ddict<>{}:
            self.__dict__=ddict
        else:
            self.name=""
            self.userid=""
            self.moddate=j.base.time.getTimeEpoch()
            self.retchannels=["xmpp"]
            self.loglevel=5
            self.channel=""
            self.jobs=[]
            self.userXmpp=[]
            self.outpath=""
            self.vars={}
        self.alwaysdie=True
        self.reservedCmds=["print","loglevel","vars","channel","help"]

    def jobNew(self,channel,msg,rscriptname,args={}):
        job=Job()        
        job.model.rscript_channel=channel
        job.model.rscript_content=msg
        job.model.rscript_name=rscriptname
        job.model.sessionid=self.name
        job.model.userid=self.userid        
        job.vars=args
        job.save()        
        job.session=self
        self.jobs.append(job.model.guid)
        while len(self.jobs)>50:
            self.jobs.pop(0)

        return job

    def jobGet(self,guid):
        job =Job(jobguid=guid)
        job.session=self
        job.model.sessionid=self.name
        job.model.userid=self.userid
        return job

    def jobGetLast(self):
        if len(self.jobs)>0:
            jobguid=self.jobs[-1]  
            return self.jobGet(jobguid)            

    def save(self):
        j.servers.cloudrobot.redis.hset("cloudrobot:sessions:%s"%(self.userid),self.name,json.dumps(self.__dict__))


    def sendUserMessage(self,msg,html=False):     
        if msg.strip()=="":
            return
        msg=msg.strip()
        msg+="\n"
        msg=msg.replace("\n\n\n","\n\n")
        msg=msg.replace("\n\n\n","\n\n")

        if "xmpp" in self.retchannels:
            if self.userXmpp==[]:
                user=j.servers.cloudrobot.userGet(self.userid)
                self.userXmpp=user.xmpp
                self.save()
            for xmpp in self.userXmpp:
                if html:
                    j.servers.cloudrobot.redisq_xmpp.put("2:%s:%s"%(xmpp,str(msg)))
                else:
                    j.servers.cloudrobot.redisq_xmpp.put("1:%s:%s"%(xmpp,str(msg)))
        elif "file" in self.retchannels:
            j.system.fs.writeFile(self.outpath, msg, append=True)

    def process(self,msg,channel=None,scriptname="unknown",args={}):
        if msg.find("session")==0:
            self.sendUserMessage("your current session:%s\n"%self.name)
            return
        
        if msg.find("channel")==0:
            channel=msg.replace("channel","").strip().lower().strip(":=").strip()
            if channel<>"":
                self.channel=channel
                self.save()
            self.sendUserMessage("your current channel:%s\n"%self.channel)
            return

        #FIND ROBOT CMDS
        if msg.strip() in self.reservedCmds:                
            self._processRobotCmd(msg,"")
        if msg.find(" ")<>-1 and msg[0]<>"!" and msg[0]<>"#":
            cmd=msg.split(" ")[0].lower()
            if cmd in self.reservedCmds:
                arg=line.split(" ",1)[1]
                self.processRobotCmd(cmd,arg)

        foundcmd=False
        foundvars=False
        #now find vars
        state="init"
        lastvar=""
        msg = msg.replace(' /n', '\n')
        for line in msg.split("\n"):
            line=line.strip()
            if line=="" or line[0]=="#":
                continue
            if line.find("!")==0:
                foundcmd=True
                break

            if state=="invar":
                if line.find("...")==0:
                    state="init"
                    lastvar=lastvar.strip()+"\n"
                    self.vars[name]=lastvar
                    lastvar=""
                else:
                    lastvar+="%s\n"%line

            if line.find("=")<>-1:
                if line.find("...")<>-1:
                    #multiline var
                    name,val=line.split("=",1)
                    state="invar"
                    foundvars=True
                else:
                    foundvars=True
                    name,val=line.split("=",1)
                    name=name.strip()
                    val=val.strip()
                    self.vars[name]=val

        if foundvars:
            self.save()

        if foundcmd:
            if channel==None:
                channel=self.channel

            if channel=="":
                self.sendUserMessage("Error:channel not defined, please use channel cmd.")
                return

            job=self.jobNew(channel, msg=msg, rscriptname=scriptname, args=args)
            job.executeAsync()

            return job

    def _processRobotCmd(self,cmd,arg):
        print "ROBOTCMD:%s %s"%(cmd,arg)
        if cmd=="print":
            self.sendUserMessage(arg)
            return
        elif cmd=="vars":
            out=""
            if self.vars<>{}:
                out+="Session Vars:\n"
                out+="%s\n\n"%j.db.serializers.hrd.dumps(self.vars)
            self.sendUserMessage(out)

        elif cmd=="channel":
            if arg=="":
                robots="\n".join(j.servers.cloudrobot.robots.keys())
                self.sendUserMessage("Available robot channels:\n%s"%robots)
            else:
                self.channel=arg.strip().lower()
                self.save()
                self.sendUserMessage("Channel is now:%s"%self.channel)
                
        elif cmd=="loglevel":
            self.loglevel=int(arg)
            self.save()
            self.sendUserMessage("Loglevel is now:%s"%self.loglevel)           

    def __repr__(self):
        return str(self.__dict__)

    __str__=__repr__
            
class Job():
    def __init__(self,jobguid=None):
        cl = j.servers.cloudrobot.osis_robot_job
        if jobguid==None:
            job = cl.new()    
            self.model=job        
            self.model.start = j.base.time.getTimeEpoch()
            self.model.state = "INIT"
            self.model.guid=j.base.idgenerator.generateGUID().replace("-","")
            self.vars={}
        else:
            job=cl.get(jobguid)
            self.model=job
            self.vars=json.loads(self.model.vars)

    def raiseError(self,msg,end=True):
        self.model.error=msg
        msg="ERROR:%s"%msg
        self.session.sendUserMessage(msg)
        self.session.state="ERROR"
        self.model.state="ERROR"
        if end:
            self.model.end=j.base.time.getTimeEpoch()
        self.session.save()
        self.save()
        if msg[-1]<>"\n":
            msg+="\n"
        return msg

    def _getQueue(self):    
        queue=j.clients.redis.getRedisQueue("127.0.0.1", 7768, "robot:%s" % self.model.guid)
        return queue

    def _executePrepare(self):
        msg=self.model.rscript_content
        if msg.strip()=="":
            raise RuntimeError("Cannot be empty msg")
        return msg

    def executeAsync(self):
        self._executePrepare()

        def execRobotJob(msg,channel,userid,sessionid,jobguid):
            #DEBUG NOW
            if not j.__dict__.has_key("servers") or not j.servers.__dict__.has_key("cloudrobot"):
                import JumpScale.lib.cloudrobots
                j.servers.cloudrobot.init()
            result=j.servers.cloudrobot.robots[channel].process(msg,userid,sessionid,jobguid)

        msg=self._executePrepare()

        jobredis=j.clients.redisworker.execFunction(execRobotJob,msg=msg,channel=self.model.rscript_channel,\
            userid=self.model.userid,sessionid=self.model.sessionid,jobguid=self.model.guid,\
            _category="robot", _organization="jumpscale",_timeout=600,\
            _queue="io",_log=True,_sync=False)

    def getAsMsg(self):
        premsg=""
        if msg[-1]<>"\n":
            msg+="\n"
        for key in self.vars.keys():
            premsg+="@%s=%s\n"%(key,self.vars[key])
        msg="%s\n%s\n"%(premsg,msg)

    def _done(self):
        if not j.servers.cloudrobot.redis.exists("queues:robot:%s"%self.model.guid):    
            n=j.base.time.getTimeEpoch()
            print "QUEUE OK"
            q=self._getQueue()
            q.put(str(n))
            q.set_expire(n+120)

    def save(self):
        
        #save job in osis
        cl = j.servers.cloudrobot.osis_robot_job
        self.model.vars=json.dumps(self.vars)
        cl.set(self.model)

        if self.model.end<>0:
            self._done()
        
            
        #     if j.servers.cloudrobot.redis.hexists("robot:jobs",self.guid):
        #         j.servers.cloudrobot.redis.hdel("robot:jobs",self.guid)
        # else:
        #     data=json.dumps(self.__dict__)        
        #     j.servers.cloudrobot.redis.hset("robot:jobs",self.model.guid,data)

    def waitExecutionDone(self,updateSelf=True):
        print "wait for job:%s"%self.model.guid
        # while q.empty():
        #     print "queue empty for %s"%jobguid
        #     time.sleep(0.1)
        q=self._getQueue()
        q.get()
        j.servers.cloudrobot.redis.delete("queues:robot:%s" % self.model.guid)
        if updateSelf:
            cl = j.servers.cloudrobot.osis_robot_job
            job=cl.get(self.model.guid)
            self.model=job
            self.vars=json.loads(self.model.vars)

    def actionNew(self,name="",code="",vars={}):
        action=Action()        
        action.model.jobguid=self.model.guid
        action.model.rscript_channel=self.model.rscript_channel
        action.model.rscript_name=self.model.rscript_name
        action.model.userid=self.model.userid
        action.model.code=code              
        action.vars=vars
        action.save()        
        self.model.actions.append(action.model.guid)
        action.session=self.session
        action.job=self
        return action

    def sendUserMessage(self,msg,html=False):   
        if msg.strip()=="":
            return
        if msg[-1]<>"\n":
            msg+="\n"
        self.session.sendUserMessage(msg,html=html)
        self.model.out+=msg

    def actionGet(self,guid):
        action =Action(guid=guid)
        action.session=self.session
        action.job=self
        return action

    def __repr__(self):       
        return str(self.model)

    __str__=__repr__

class Action():
    def __init__(self,guid=None):
        cl = j.servers.cloudrobot.osis_robot_action
        if guid==None:
            model = cl.new()    
            self.model=model        
            self.model.start = j.base.time.getTimeEpoch()
            self.model.state = "INIT"
            self.vars={}
            self.model.guid=j.base.idgenerator.generateGUID().replace("-","")
        else:
            model=cl.get(guid)
            self.model=model
            self.vars=json.loads(self.model.vars)

    # def getAsMsg(self):
    #     premsg=""
    #     if msg[-1]<>"\n":
    #         msg+="\n"
    #     for key in args.keys():
    #         premsg+="@%s=%s\n"%(key,args[key])
    #     msg="%s\n%s\n"%(premsg,msg)

    def save(self):
                
        #save job in osis
        cl = j.servers.cloudrobot.osis_robot_action
        self.model.vars=json.dumps(self.vars)
        cl.set(self.model)

    def raiseError(self,msg,end=True):
        self.model.error=msg
        msg2="ERROR:%s"%msg
        self.session.sendUserMessage(msg2)
        self.session.state="ERROR"
        self.job.model.state="ERROR"
        self.model.state="ERROR"
        self.model.end=j.base.time.getTimeEpoch()        
        if end:            
            self.job.model.end=j.base.time.getTimeEpoch()
            self.job.model.error+=msg
        self.session.save()
        self.job.save()
        self.save()
        if msg[-1]<>"\n":
            msg+="\n"
        return msg

    def sendUserMessage(self,msg,html=False):   
        if msg.strip()=="":
            return
        if msg[-1]<>"\n":
            msg+="\n"
        self.job.sendUserMessage(msg,html=html)
        self.model.out+=msg

    def _processVars(self,session,job):
        def process(vars,session,job,varsout,changeVars=False):
            for key,val in vars.iteritems():
                if str(val).find("#")<>-1:
                    val=val.split("#",1)[0].strip()                
                if str(val).find("$")<>-1:
                    for toreplace,replace in job.vars.iteritems():
                        val=val.replace("$%s"%toreplace,str(replace))
                    for toreplace,replace in session.vars.iteritems():
                        val=val.replace("$%s"%toreplace,str(replace))
                    if changeVars:
                        vars[key]=val
                varsout[key]=val
            return vars,varsout
        
        varsout={}
        tmp,varsout=process(session.vars,session,job,varsout)
        tmp,varsout=process(job.vars,session,job,varsout)
        tmp,varsout=process(self.vars,session,job,varsout)
        # self.vars,varsout=process(self.vars,session,job,True)
        self.vars=varsout

        return varsout



    def __repr__(self):       
        return str(self.model)

    __str__=__repr__


class CloudRobotFactory(object):
    def __init__(self):
        self.hrd=None
        # self.robotspath=None
        self._inited=False

    def init(self): 
        if not self._inited:
            self.init()
            self._inited=True

    def getOSISObjManipulatorClass(self):
        return OSISObjManipulatorClass

    def _init(self):
        # j.cloudrobot=Empty()        

        # ppath="%s/apps/cloudrobot/"%j.dirs.baseDir
        # if ppath not in sys.path:
        #     sys.path.append(ppath)

        # self.robotspath="%s/%s"%(ppath,"robots.py")
        # from robots import robots
        # self.robots=robots

        if self.hrd==None: #hrd is loaded where we import robots
            raise RuntimeError("hrd not specified yet.")
        osisinstance=self.hrd.get("cloudrobot.osis.connection")
        self.osis =j.core.osis.getClientByInstance(osisinstance)        
        self.osis_robot_job = j.core.osis.getClientForCategory(self.osis, 'robot', 'job')
        self.osis_robot_action = j.core.osis.getClientForCategory(self.osis, 'robot', 'action')
        self.osis_oss_user = j.core.osis.getClientForCategory(self.osis, 'oss', 'user')
        self.osis_system_user = j.core.osis.getClientForCategory(self.osis, 'system', 'user')
        self.redis=j.clients.redis.getRedisClient("127.0.0.1", 7768)
        

    def startMailServer(self):
        self.init()
        self.domain=self.hrd.get("cloudrobot.mail.domain")
        from .MailRobot import MailRobot
        robot = MailRobot(('0.0.0.0', 25),hrd_instance=self.hrd)
        print "start server on port:25"
        robot.serve_forever()

    def startHTTP(self, addr='0.0.0.0', port=8099):
        self.init()
        from .HTTPRobot import HTTPRobot
        robot=HTTPRobot(addr=addr, port=port)
        robot.start()

    def startXMPPRobot(self,username,passwd):
        self.init()
        self.redisq_xmpp=j.clients.redis.getRedisQueue("127.0.0.1", 7768,"xmpp")
        from .XMPPRobot import XMPPRobot        
        robot=XMPPRobot(username=username, passwd=passwd)
        robot.init()     

    def startFileRobot(self):
        self.init()
        robot=FileRobot()
        robot.start()

    def userIdGetFromXmpp(self,xmpp=""):
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
            
    def sessionGet(self,userid,name=None,reset=False):
        # print "redis:'cloudrobot:sessions:%s' name:%s"%(userid,name)
        if name==None:
            #look at default session or see if there is one
            name=self.getUserSession(userid,reset=reset)

        if reset or not self.redis.hexists("cloudrobot:sessions:%s"%(userid),name):
            session=Session()
            session.userid=userid
            session.name=name
            session.save()
        else:
            data=json.loads(self.redis.hget("cloudrobot:sessions:%s"%(userid),name))
            session=Session(ddict=data)
        
        return session

    def userGet(self,userid):
        # if not self.redis.hexists("cloudrobot:users:obj",userid):
        res=self.osis_system_user.simpleSearch({"id":userid})
        if len(res)==0:
            j.events.inputerror_critical("Could not find user with id:%s"%userid,"cloudrobot.auth")            
        user=self.osis_system_user.get(res[0]["guid"])
        # self.redis.hset("cloudrobot:users:obj",userid,json.dumps(user.__dict__))
        # obj=json.loads(self.redis.hget("cloudrobot:users:obj",userid))
        return user

    def setUserSession(self,userid,name):
        self.redis.hset("cloudrobot:currentsessions",userid,name.lower().strip())

    def getUserSession(self,userid,reset=False):
        if reset or not self.redis.hexists("cloudrobot:currentsessions",userid):
            self.redis.hset("cloudrobot:currentsessions",userid,"default")        
        return self.redis.hget("cloudrobot:currentsessions",userid)

    def reset(self,userid):
        self.redis.hdel("cloudrobot:currentsessions",userid)
        #@todo remove sessions for the user

    def obj2out(self,obj):
        if not j.basetype.string.check(obj):
            resultstr=yaml.dump(obj, default_flow_style=False).replace("!!python/unicode ","")
            resultstr=resultstr.replace("'","")
            return resultstr
        return obj