from JumpScale import j

from .FileRobot import FileRobot

import JumpScale.baselib.redis
import ujson as json
import time
import JumpScale.baselib.redisworker
import JumpScale.grid.osis

import sys

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
            self.channel="ms1_iaas"
            self.jobs=[]
            self.userXmpp=[]
            self.outpath=""
            self.vars={}
        self.alwaysdie=True

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
        return job

    def jobGet(self,guid):
        job =Job(jobguid=guid)
        job.session=self
        job.model.sessionid=self.name
        job.model.userid=self.userid
        return job

    def save(self):
        j.servers.cloudrobot.redis.hset("cloudrobot:sessions:%s"%(self.userid),self.name,json.dumps(self.__dict__))


    def sendUserMessage(self,msg,html=False):                
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
            if msg.strip()=="":
                return
            if msg[-1]<>"\n":
                msg+="\n"
            j.system.fs.writeFile(self.outpath, msg, append=True)

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

    def waitExecutionDone(self):
        print "wait for job:%s"%self.model.guid
        # while q.empty():
        #     print "queue empty for %s"%jobguid
        #     time.sleep(0.1)
        q=self._getQueue()
        q.get()
        j.servers.cloudrobot.redis.delete("queues:robot:%s" % self.model.guid)
        return 

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


    def _processVars(self,session,job):
        def process(vars,session,job,varsout,changeVars=False):
            for key,val in vars.iteritems():
                if val.find("#")<>-1:
                    val=val.split("#",1)[0].strip()                
                if val.find("$")<>-1:
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
            self._init()
            self._inited=True

    def _init(self):
        # j.cloudrobot=Empty()
 
        self.redisq_xmpp=j.clients.redis.getRedisQueue("127.0.0.1", 7768,"xmpp")
        ppath="%s/apps/cloudrobot/"%j.dirs.baseDir
        if ppath not in sys.path:
            sys.path.append(ppath)
        # self.robotspath="%s/%s"%(ppath,"robots.py")
        from robots import robots
        self.robots=robots
        if self.hrd==None: #hrd is loaded where we import robots
            raise RuntimeError("hrd not specified yet.")
        osisinstance=self.hrd.get("cloudrobot.osis.connection")
        self.osis =j.core.osis.getClientByInstance(osisinstance)        
        self.osis_robot_job = j.core.osis.getClientForCategory(self.osis, 'robot', 'job')
        self.osis_robot_action = j.core.osis.getClientForCategory(self.osis, 'robot', 'action')
        self.osis_oss_user = j.core.osis.getClientForCategory(self.osis, 'oss', 'user')
        self.osis_system_user = j.core.osis.getClientForCategory(self.osis, 'system', 'user')
        self.redis=j.clients.redis.getRedisClient("127.0.0.1", 7768)
        self.domain=self.hrd.get("cloudrobot.mail.domain")

    def startMailServer(self):
        self._init()
        from .MailRobot import MailRobot
        robot = MailRobot(('0.0.0.0', 25),hrd_instance=self.hrd)
        print "start server on port:25"
        robot.serve_forever()

    def startHTTP(self, addr='0.0.0.0', port=8099):
        self._init()
        from .HTTPRobot import HTTPRobot
        robot=HTTPRobot(addr=addr, port=port)
        robot.start()

    def startXMPPRobot(self,username,passwd):
        self._init()
        from .XMPPRobot import XMPPRobot        
        robot=XMPPRobot(username=username, passwd=passwd)
        robot.init()     

    def startFileRobot(self):
        self._init()
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
            
    def sessionGet(self,userid,name,reset=False):
        # print "redis:'cloudrobot:sessions:%s' name:%s"%(userid,name)
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

