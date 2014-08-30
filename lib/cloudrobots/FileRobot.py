from JumpScale import j
import JumpScale.lib.cloudrobots
import time

class FileRobot():
    def __init__(self):
        self.basepath="%s/cloudrobot"%j.dirs.varDir
        self.robots = {}


    def findGlobal(self,C,name):
        for line in C.split("\n"):
            line=line.strip()
            print line    
            if line.find("@%s"%name)==0:
                name,val=line.split("=",1)
                return val.strip()
        return None

    def start(self):

        for channel in self.robots.keys():
            for item in ["in","out","err","draft"]:  #,"jobs"
                j.system.fs.createDir("%s/%s/%s"%(self.basepath,channel,item))

        print "Started"

        while True:
            # channels=j.system.fs.listDirsInDir("data",False,True)

            #is to get access to the other robots from a robot
            for channel in self.robots.keys():
                self.robots[channel].robots=self.robots
                # for channel in channels:                
                for path in j.system.fs.listFilesInDir("%s/%s/in/"%(self.basepath,channel)):
                    name0=j.system.fs.getBaseName(path).replace(".txt","").replace(".py","")
                    C=j.system.fs.fileGetContents(path)            

                    userid=self.findGlobal(C,"msg_userid")
                    if userid==None:
                        userid="robot"

                    name="%s_%s_%s_%s.txt"%(j.base.time.getTimeEpoch(),j.base.time.getLocalTimeHRForFilesystem(),name0,userid)
                    # j.system.fs.writeFile("%s/%s/jobs/%s"%(self.basepath,channel,name),C)

                    print "PROCESS:%s"%path            

                    session=j.servers.cloudrobot.sessionGet(userid,"file",reset=True)
                    session.channel=channel
                    session.outpath="%s/%s/out/%s"%(self.basepath,channel,name)
                    session.retchannels=["file"]
                    session.userid=userid
                    session.save()                    

                    job=j.servers.cloudrobot.jobNew(channel, msg=C, rscriptname=name0, args={}, userid=userid, sessionid=session.name)

                    from IPython import embed
                    print "DEBUG NOW ooo"
                    embed()
                    

                    result=self.robots[channel].process(C)

                    j.system.fs.remove(path)

                    if jobguid<>None:
                        job.result = result
                        job.end = j.base.time.getTimeEpoch()
                    
                    if result.find(">ERROR:")<>-1:
                        print "ERROR, see %s"%path
                        if jobguid<>None:
                            job.state = "ERROR"
                        path="%s/%s/err/%s"%(self.basepath,channel,name)
                        j.system.fs.writeFile(path,result)
                    else:
                        if jobguid<>None:
                            job.state = "OK"
                        path="%s/%s/out/%s"%(self.basepath,channel,name)
                        j.system.fs.writeFile(path,result)

                    # if userid<>"":
                    #     j.servers.cloudrobot.sendUserMessage(userid,result)                         

                    if jobguid<>None:
                        tmp, tmp, guid = cl.set(job)
                        j.servers.cloudrobot.job2redis(job)

            time.sleep(0.5)

