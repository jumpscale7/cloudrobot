from JumpScale import j
import yaml
import JumpScale.baselib.hash
from TxtRobotHelp import TxtRobotHelp
import JumpScale.baselib.mailclient
import JumpScale.lib.cloudrobots

import JumpScale.baselib.redis
import copy

class TxtRobotFactory(object):

    def __init__(self):
        pass
        
    def get(self, definition):
        """
        example definition:
        
        project (proj,p)
        - list (l)
        - delete (del,d)
        -- name (n)
        user (u)
        - list (l)
        """
        return TxtRobot(definition)

class TxtRobot():
    def __init__(self,definition):
        self.definition=definition
        self.cmdAlias={}
        self.entityAlias={}
        self.entities=[]
        self.cmds={}
        self.cmdobj=None
        self._initCmds(definition)
        self.cmdsToImpl={}
        self.help=TxtRobotHelp()
        # self.snippet = TxtRobotSnippet()
        self.redis=j.clients.redis.getRedisClient("localhost",7768)
        self.codeblocks={}
        alias={}
        alias["l"]="login"
        alias["p"]="passwd"
        alias["pwd"]="passwd"
        alias["password"]="passwd"
        self.argsAlias=alias

        self.osis = j.core.osis.getClient(user='root')
        self.osis_system_user=j.core.osis.getClientForCategory(self.osis, 'system', 'user')

    def _initCmds(self,definition):

        for line in definition.split("\n"):
            # print line
            line=line.strip()
            if line=="":
                continue
            if line[0]=="#":
                continue

            if line.find("****")<>-1:
                break

            if line[0]<>"-":
                if line.find(" ")<>-1:
                    ent,remainder=line.split(" ",1)
                else:
                    ent=line
                    remainder=""
                ent=ent.lower().strip()
                self.entities.append(ent)
                if remainder.find("(")<>-1 and remainder.find(")")<>-1:
                    r=remainder.strip("(")
                    r=r.strip(")")
                    r=r.strip()
                    for alias in r.split(","):
                        alias=alias.lower().strip()
                        self.entityAlias[alias]=ent

            if line[0]=="-" and line[1]<>"-":
                if ent=="":
                    raise RuntimeError("entity cannot be '', line:%s"%line)
                line=line.strip("-")
                line=line.strip()
                if line.find(" ")==-1:
                    cmd=line
                    remainder=""
                else:
                    cmd,remainder=line.split(" ",1)
                cmd=cmd.lower().strip()
                if not self.cmds.has_key(ent):
                    self.cmds[ent]=[]
                if not self.cmdAlias.has_key(ent):
                    self.cmdAlias[ent]={}
                if cmd not in self.cmds[ent]:
                    self.cmds[ent].append(cmd)

                if remainder.find("(")<>-1 and remainder.find(")")<>-1:
                    r=remainder.strip("(")
                    r=r.strip(")")
                    r=r.strip()
                    for alias in r.split(","):
                        alias=alias.lower().strip()
                        self.cmdAlias[ent][alias]=cmd                

    def _processGlobalArg(self,obj,line):
        # print "GARG:%s"%line
        res={}
        out=""
        alias=self.argsAlias
        if line.find("=")<>-1:
            name,data=line.split("=",1)
                                    
            name=name.lower().strip("@")
            if alias.has_key(name):
                name=alias[name]

            val=data.strip().replace("\\n","\n")

            if val.find("#")<>-1:
                val=val.split("#",1)[0].strip()        

            obj.vars[name]=val
        return obj
        
    # def message2session(self,result):
    #     if self.args.has_key("msg_userid"):
    #         j.servers.cloudrobot.sendUserMessage(self.args["msg_userid"],result)

    def _longTextTo1Line(self,txt):
        txt=txt.rstrip("\n")
        state="start"
        out=""
        lt=""
        ltstart=""
        for line in txt.split("\n"):
            line=line.strip()
            if state=="LT":
                if len(line)>0 and line.find("...")==0:
                    #means we reached end of block
                    state="start"
                    out+="%s%s\n"%(ltstart,lt)
                    ltstart=""
                    lt=""
                    continue
                else:
                    lt+="%s\\n"%line
                    continue      
            if len(line)>0 and line[0]=="#":
                continue      
            if state=="start" and line.find("=")<>-1:
                before,after=line.split("=",1)                
                if after.strip()[0:3]=="...":
                    state="LT"
                    ltstart="%s="%before
                    continue

            out+="%s\n"%line
            
        return out

    def _findCodeBlocks(self,txt):
        cbname=""
        out=""
        cb=""
        txt=txt.rstrip("\n")
        for line in txt.split("\n"):
            line2=line.lower()
            if line2.find("@end")==0:
                if cbname=="MAIN":
                    #means we will only deal with main block, all the rest is irrelevant
                    return cb
                cb=cb.strip()
                self.codeblocks[cbname.lower()]=cb
                #do not put codeblock in out

                cb=""
                cbname=""
                continue

            if cbname<>"":
                #we are in block so remember
                cb+="%s\n"%line
                continue

            if line2.find("@start")==0:
                cbname=line2.split("@start")[1].strip()
                if cbname=="":
                    #do not remember prev lines because found main block
                    out=""
                    cbname="MAIN"
                continue
            out+="%s\n"%line
        return out

    # def response(self,cblock,result):
    #     if cblock.strip()<>"":
    #         out=j.tools.text.prefix("< ",cblock)
    #     else:
    #         out=""
    #     if out=="":
    #         return ""
    #     if out[-1]<>"\n":
    #         out+="\n"
    #     if result<>"":
    #         out+=j.tools.text.prefix("> ",result)
    #     if out[-1]<>"\n":
    #         out+="\n"
    #     return out

    # def responseError(self,cblock,result):
    #     out=cblock            
    #     if out.strip()<>"" and out[-1]<>"\n":
    #         out+="\n"        
    #     if result<>"":
    #         out+=j.tools.text.prefix(">ERROR: ",result)
    #     if out.strip()<>"" and out[-1]<>"\n":
    #         out+="\n" 
    #     self.message2session("ERROR:%s\n"%out)
    #     print out
    #     return out

    def _processSnippets(self,txt):
        out=""
        txt=txt.rstrip("\n")
        for line in txt.split("\n"):
            if line.find("!snippet.get")==0:
                remainder=line.split("!snippet.get",1)[1]
                md5=remainder.strip()
                snippet = self.redis.hget("robot:snippets", md5)
                if snippet==None:
                    out+=self.responseError(line,"Could not find snippet with key:%s"%md5)
                else:
                    out+="%s\n"%snippet
                continue
            out+="%s\n"%line
        return out

    def _snippetCreate(self,name):
        name=name.lower()
        if not self.codeblocks.has_key(name):
            return self.responseError("","Could not find codeblock with name:'%s'"%name)
        else:
            snippet=self.codeblocks[name]
            md5=j.tools.hash.md5_string(snippet)
        self.redis.hset("robot:snippets", md5, snippet)
        return "snippetkey=%s"%md5

    def process(self, txt,userid,sessionid,jobguid):
                
        session=j.servers.cloudrobot.sessionGet(userid,sessionid)
        job=session.jobGet(jobguid)

        txt=self._findCodeBlocks(txt)        
        txt=self._longTextTo1Line(txt)
        txt=self._processSnippets(txt) #replace snippets 

        entity=""
        args={}
        cmds=list()
        cmd=""
        out=""

        txt=txt.rstrip("\n")
        splitted=txt.split("\n")

        cmdfound=False

        rc=0

        for line in splitted:
            print "process:%s"%line
            line=line.strip()

            if line.find(">ERROR:")==0:
                continue

            if line=="" or line[0]=="#" or line[0]==">" or line[0]=="<":
                out+="%s\n"%line
                continue

            #DEAL WITH HELP CMDS
            if line=="?" or line=="h" or line=="help":
                out+=self.response("help",self.help.help())
                continue
            if line.find("help.syntax")<>-1:
                out+=self.response("!help.syntax",self.help.help_definition())
                continue
            if line.find("help.cmds")<>-1:
                out+=self.response("!help.cmds",self.definition)
                # out+= '%s\n' % self.definition  #<br/>
                continue

            if line.find("robot.stop")<>-1:
                # out+= '%s\n' % self.definition  #<br/>
                break

            if cmd<>"" and (line[0]=="!" or line[0]=="@" or line.find("******")<>-1):
                #end of cmd block                
                cmdfound=True
                res2,rc=self.processCmd(cmdblock,entity, cmd, args,gargs)
                out+=res2
                
                if rc>0 and session.alwaysdie:
                    break

                cmdblock=""
                cmd=""                

            if line.find("******")<>-1:
                break #end of message

            #DEAL WITH SNIPPET CREATE CMD
            if line.find("!snippet.create")==0:
                remainder=line.split("!snippet.create",1)[1]
                out+=self.response(line,self._snippetCreate(remainder.strip()))
                continue

            if line.find("@")==0:                
                #session args                
                session=self._processGlobalArg(session,line)
                out+="%s\n"%line
                continue

            if cmd=="" and line.find("=")<>-1:
                #job args                
                job=self._processGlobalArg(job,line)
                out+="%s\n"%line
                continue

            #process cmd
            if line[0]=="!":
                #CMD
                entity=""
                cmd=""
                args={}
                line2=line.strip("!")
                line2=line2.strip()
                if line2.find(".")==-1:
                    # raise RuntimeError("format needs to be !entity.cmd (here:%s)"%line2)
                    out+=job.raiseError("format needs to be !entity.cmd on line:%s"%line2)                    
                    if session.alwaysdie:
                        break
                entity,cmd=line2.split(".",1)
                entity=entity.lower().strip()
                if cmd.find(" ")<>-1:
                    cmd,remainder=cmd.split(" ",1)
                    args["name"]=remainder.strip()
                cmd=cmd.lower().strip()
                cmdblock=""
                if self.entityAlias.has_key(entity):
                    entity=self.entityAlias[entity]

                if not entity=="robot":

                    if not entity in self.entities:
                        # out+= '%s\n' % self.error(,help=True)
                        out+=job.raiseError("Could not find entity:'%s' on line:%s"%(entity,line2))
                        if session.alwaysdie:
                            break
                        continue

                    if self.cmdAlias[entity].has_key(cmd):
                        cmd=self.cmdAlias[entity][cmd]

                    if not cmd in self.cmds[entity]:
                        out+=job.raiseError("Could not understand command '%s' line:%s"%(cmd,line2))
                        if session.alwaysdie:
                            break                    
                        continue

                if line.find(" ")<>-1:
                    remainder=line.split(" ",1)[1]
                    args["name"]=remainder.strip()

            if cmd<>"":
                cmdblock+="%s\n"%line

            #process argument for cmd 
            if line.find("=")<>-1 and cmd<>"":
                name,data=line.split("=",1)
                name=name.lower()
                # print "args:%s:%s '%s'"%(name,data,line)
                args[name]=data.strip().replace("\\n","\n")

        if cmd<>"" and rc==0:
            #end of cmd block
            cmdfound=True
            action=self.processCmd(cmdblock,entity, cmd, args,session,job)            
            out+=action.model.result

        out=out.strip()+"\n"

        # for cbname,cblock in self.codeblocks.iteritems():            
        #     out="@START %s\n%s\n@END\n\n%s"%(cbname,cblock,out)

        # out=out.strip()

        while out.find("\n\n\n")<>-1:
            out=out.replace("\n\n\n","\n\n")

        job.model.state="OK"
        job.model.end=j.base.time.getTimeEpoch()
        job.model.out=out
        job.save()        
        
        # if cmdfound==False: 
        #     self.args2session(gargs)
        #     out+= self.responseError("\n","Did not find a command to execute.")

        # if gargs.has_key("mail_from"):
        #     ffrom=gargs["mail_from"]
        #     subject=gargs["mail_subject"]
        #     mail_robot=gargs["mail_robot"]
        #     out2=""
        #     for line in out.split("\n"):
        #         if line.find("@mail_")==0:
        #             continue
        #         out2+="%s\n"%line            
        #     j.clients.email.send([ffrom], mail_robot, subject, out2)

        return out

    def processCmd(self, cmdblock,entity, cmd, args,session,job):
        print "EXECUTE:\n%s"%cmdblock

        action=job.actionNew(name=cmd, code=cmdblock, vars=args)
        
        args=action._processVars(session,job)
                        
        session.sendUserMessage("CMD:%s"%cmd)

        result=None

        if entity=="robot":
            result=self.processRobotCmd(cmdblock,cmd, args)
            if str(result).find("E:")==0:
                # j.errorconditionhandler.processPythonExceptionObject(e)
                result=str(result)[2:]
                print result
                return self.responseError(cmdblock,"Cannot execute: !%s.%s\nERROR:%s"%(entity,cmd,result)),1
        else:
            key="%s__%s"%(entity,cmd)
            if self.cmdobj<>None:
                if hasattr(self.cmdobj,key):
                    try:
                        method=eval("self.cmdobj.%s"%key)
                    except Exception,e:
                        action.raiseError("could not eval code.")
                        return action
                    #now execute the code
                    try:
                        result=method(**args)
                    except Exception,e:
                        if str(e).find("E:")==0 or str(e).find("F:")==0:
                            # j.errorconditionhandler.processPythonExceptionObject(e)
                            e=str(e)[2:]
                            # print e
                            action.raiseError("execution error")
                            return action                            
                        else:
                            j.errorconditionhandler.processPythonExceptionObject(e)
                            action.raiseError("bug:%s"%e)
                            return action
                else:
                    action.raiseError("bug:did not attr:'%s' on self.cmdobj"%key)
                    return action        
            else:
                action.raiseError("bug:did not find self.cmdobj")
                return action


        if result==None:
            action.raiseError("method not found on robot.")
            return action            

        if not j.basetype.string.check(result):
            resultstr=yaml.dump(result, default_flow_style=False).replace("!!python/unicode ","")
            action.model.result=json.dumps(result)
        else:
            resultstr=result
            action.model.result=result

        action.state="OK"
        action.save()

        # if out.find("$")<>-1:
        #     for toreplace,replace in j.cloudrobot.vars.iteritems():
        #         out=out.replace("$%s"%toreplace,str(replace))
        #     for toreplace,replace in gargs.iteritems():
        #         out=out.replace("$%s"%toreplace,str(replace))  
        #     for toreplace,replace in args.iteritems():
        #         out=out.replace("$%s"%toreplace,str(replace))  

        session.sendUserMessage("result:\n%s"%resultstr)
        return action

    def processRobotCmd(self,cmdblock,cmd, args):
        
        # for key,val in args.iteritems():
        #     if val.find("$")<>-1:
        #         for toreplace,replace in j.cloudrobot.vars.iteritems():
        #             val=val.replace("$%s"%toreplace,str(replace))
        #         for toreplace,replace in args.iteritems():
        #             val=val.replace("$%s"%toreplace,str(replace))           
        for key in args.keys():
            if args[key].find("#")<>-1:
                args[key]=args[key].split("#",1)[0].strip()

        out=""
        if cmd=="print":
            if not args.has_key("msg"):
                return "E:there should be msg argument."            
            out=args["msg"]
        elif cmd=="printvars":
            for key,val in j.cloudrobot.vars.iteritems():
                out+="$%s=%s\n"%(key,val)
                
        elif cmd=="verbosity":
            j.cloudrobot.verbosity=int(args["name"])

        elif cmd=="mail":
            if args.has_key("to"):
                recipients=args["to"]
            else:
                raise RuntimeError("not implemented yet, goal is to send email to who started the script")
                # users = self.osis_system_user.simpleSearch({'id': username})
                # if len(users)>0:
                #     user=users[0]["id"]
                # else:
                #     raise RuntimeError("Authentication error: user not found.")    
            if args.has_key("from"):
                ffrom=args["from"]
            else:
                ffrom="%s@%s"%(self.cmdobj.channel,j.servers.cloudrobot.domain)

            if args.has_key("subject"):
                subject=args["subject"]
            elif args.has_key("rscriptname"):
                subject=args["rscriptname"]                
            else:
                subject="cloudrobot for channel:%s"%self.cmdobj.channel         

            j.clients.email.send(recipients=recipients, sender=ffrom, subject=subject, message=args['msg'], files=None)
            
        else:
            return "E:could not find cmd:%s"%(cmd)
        return out
     
    def addCmdClassObj(self,cmdo):
        cmdo.txtrobot=self
        self.cmdobj=cmdo

