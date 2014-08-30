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

    def save(self):
        j.servers.cloudrobot.redis.hset("cloudrobot:sessions:%s"%(self.userid),self.name,json.dumps(self.__dict__))

    def sendUserMessage(self,msg,html=False):                
        if "xmpp" in self.retchannel:
            if self.userXmpp==[]:
                user=j.servers.cloudrobot.userGet(self.userid)
                self.userXmpp=user.xmpp
                self.save()
            for xmpp in self.userXmpp:
                if html:
                    j.servers.cloudrobot.redisq_xmpp.put("2:%s:%s"%(xmpp,str(msg)))
                else:
                    j.servers.cloudrobot.redisq_xmpp.put("1:%s:%s"%(xmpp,str(msg)))
        elif "file" in self.retchannel:
            from IPython import embed
            print "DEBUG NOW msg to file"
            embed()

    def __repr__(self):
        return str(self.__dict__)

    __str__=__repr__
            

class Job():
    def __init__(self,ddict={}):
        if ddict=={}:        
            cl = j.servers.cloudrobot.osis_robot_job
            print "new job"
            job = cl.new()            
            self.model=job
            self.model.start = j.base.time.getTimeEpoch()
            self.model.state = "INIT"
        else:
            self.__dict__=ddict

    def _getQueue(self):    
        queue=j.clients.redis.getGeventRedisQueue("127.0.0.1", 7768, "robot:queues:%s" % self.guid)
        return queue

    def _executePrepare(self):
        msg=self.model.rscript_content
        if msg.strip()=="":
            raise RuntimeError("Cannot be empty msg")



        return guid

    def executeAsync(self,job):
        self._executePrepare()

        def execRobotJob(robotspath):
            from IPython import embed
            print "DEBUG NOW ooo"
            embed()
        
        job=j.clients.redisworker.execFunction(atest,robotspath=j.servers.cloudrobot.robotspath,\
            _category="robot", _organization="jumpscale",_timeout=600,\
            _queue="io",_log=True,_sync=False)



    def getAsMsg(self):
        premsg=""
        if msg[-1]<>"\n":
            msg+="\n"
        for key in args.keys():
            premsg+="@%s=%s\n"%(key,args[key])
        msg="%s\n%s\n"%(premsg,msg)



    def save(self):
        
        if self.model.end<>0:
            n=j.base.time.getTimeEpoch()
            print "QUEUE OK"
            q=self._getQueue()
            q.put(str(n))
            q.set_expire(n+120)
            #save job in osis

            from IPython import embed
            print "DEBUG NOW save"
            embed()
            
            if j.servers.cloudrobot.redis.hexists("robot:jobs",self.guid):
                j.servers.cloudrobot.redis.hdel("robot:jobs",self.guid)
        else:
            data=json.dumps(self.model.__dict__)        
            j.servers.cloudrobot.redis.hset("robot:jobs",self.guid,data)

    def waitExecutionDone(self,jobguid):
        print "wait for job:%s"%jobguid
        # while q.empty():
        #     print "queue empty for %s"%jobguid
        #     time.sleep(0.1)
        q=self._getQueue(job)
        q.get()
        return 

    def __repr__(self):       
        return str(self.model)

    __str__=__repr__



class CloudRobotFactory(object):
    def __init__(self):
        self.hrd=None
        
    def init(self,robots):
        self.robots=robots
        return self._init()

    def _init(self):
        j.cloudrobot=Empty()
 
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

    def jobNew(self,channel,msg,rscriptname,args={},userid=None,sessionid=None):
        job=Job()
        job.rscript_channel=channel
        job.rscript_content=msg
        job.rscript_name=rscriptname
        job.session=sessionid
        job.user=userid
        job.guid=j.base.idgenerator.generateGUID()
        job.save()
        return job

    def jobGet(self,guid):
        if self.redis.hexists("robot:jobs",self.guid):
            data=self.redis.hget("robot:jobs",self.guid)
            job=Job(ddict=ujson.loads(data))
        else:
            from IPython import embed
            print "DEBUG NOW jobgetosis"
            embed()
            
  
        
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

    def sessionGetVar(self,userid,session,key):
        data=self.redis.hset("cloudrobot:sessionvars:%s:%s"%(userid,session),key)
        return json.loads(data)

    def sessionSetVar(self,userid,session,key,value):
        self.redis.hset("cloudrobot:sessionvars:%s:%s"%(userid,session),key,json.dumps(value))

    def sessionClear(self,userid,session):
        self.redis.delete("cloudrobot:sessionvars:%s:%s"%(userid,session))
        self.redis.hdel("cloudrobot:sessions:%s"%(userid),session)
