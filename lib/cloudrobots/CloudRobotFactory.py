from JumpScale import j

from .FileRobot import FileRobot

import JumpScale.baselib.redis
import ujson as json
import time

import JumpScale.grid.osis

import sys

class Empty():
    pass

class Session():
    def __init__(self,ddict={}):
        if ddict<>{}:
            self__dict__=ddict
        self.name=""
        self.userid=""
        self.moddate=j.base.time.getTimeEpoch()
        self.retchannels=["xmpp"]
        self.loglevel=5
        self.channel="ms1_iaas"
        self.jobs=[]
        self.userXmpp=[]

    def save(self):
        self.redis.hset("cloudrobot:sessions:%s"%(self.userid),self.name),json.dumps(self.__dict__))

    def sendUserMessage(self,msg,html=False):                
        if self.retchannel=="xmpp":
            if self.userXmpp==[]:
                user=j.servers.cloudrobot.userGet(self.userid)
                self.userXmpp=user.xmpp
                self.save()
            for xmpp in self.userXmpp:
                if html:
                    self.redisq_xmpp.put("2:%s:%s"%(xmpp,str(msg)))
                else:
                    self.redisq_xmpp.put("1:%s:%s"%(xmpp,str(msg)))

class Job():
    def __init__(self,ddict={}):
        if ddict=={}:        
            cl = j.servers.cloudrobot.osis_robot_job
            print "new job"
            job = cl.new()
            self.__dict__=job.__dict__
            self.start = j.base.time.getTimeEpoch()
            self.state = "INIT"
        else:
            self.__dict__=ddict

    def _getQueue(self,job):    
        queue=j.clients.redis.getGeventRedisQueue("127.0.0.1", 7768, "robot:queues:%s" % job.guid)

    def save(self):
        q=self._getQueue(job)
        data=json.dumps(self.__dict__)
        
        if self.end<>0:
            n=j.base.time.getTimeEpoch()
            print "QUEUE OK"
            q.put(str(n))
            q.set_expire(n+120)
            if j.servers.cloudrobot.redis.hexists("robot:jobs",self.guid):
                j.servers.cloudrobot.redis.hdel("robot:jobs",self.guid)
        else:
            j.servers.cloudrobot.redis.hset("robot:jobs",self.guid,data)

    def waitExecutionDone(self,jobguid):
        print "wait for job:%s"%jobguid
        # while q.empty():
        #     print "queue empty for %s"%jobguid
        #     time.sleep(0.1)
        q=self._getQueue(job)
        q.get()
        return 



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

    def jobNew(self,channel,msg,rscriptname,args={},userid=None,sessionid=None):
        job=Job()
        job.rscript_channel=channel
        job.rscript_content=msg
        job.rscript_name=rscriptname
        job.session=sessionid
        job.user=userid
        job.guid=j.base.idgenerator.generateGUID()
        job.save()
        return job.guid

    def jobGet(self,guid):
        if self.redis.hexists("robot:jobs",self.guid):
            data=self.redis.hget("robot:jobs",self.guid)
            job=Job(ddict=ujson.loads(data))
        else:
            from IPython import embed
            print "DEBUG NOW jobgetosis"
            embed()
            
    def toFileRobot(self,job):
        from IPython import embed
        print "DEBUG NOW toFileRobot"
        embed()
        
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
            
    def sessionGet(self,userid,session):
        if not self.redis.hexists("cloudrobot:sessions:%s"%(userid),session):
            session=Session()
            session.userid=userid
            session.name=name
            session.save()
        else:
            data=json.loads(self.redis.hget("cloudrobot:sessions:%s"%(userid),session))
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
        self.redis.hdel("cloudrobot:sessions:%s"%(userid),session))
