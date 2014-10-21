from JumpScale import j

# import ujson as json
# import JumpScale.baselib.redis

# import JumpScale.portal
import JumpScale.lib.ms1

class Cmds():

    # def __init__(self):
    #     self.redis=j.clients.redis.getRedisClient("127.0.0.1", 7768)

    def new(self, **args):
        
        template=args["template"]        
        res=j.tools.ms1.listImages(**args)
        try:
            templateid=int(template)
        except:
            templateid=0
        if templateid==0:
            if not res.has_key(template.lower().strip()):
                raise RuntimeError("E:Cannot find template with name %s, please use !template.list to find available templates."%template)
            else:
                templateid=res[template.lower().strip()][0]           
            
        machine_id = j.tools.ms1.deployMachineDeck(templateid=templateid,**args)
        return 'Machine created successfully. Machine ID: %s ' % machine_id

    def get(self, **args):
        
        machineId=args["name"]        
        
        out=""
        machine=j.tools.ms1.getMachineObject(**args)

        machine.pop('accounts')

        out+=j.servers.cloudrobot.obj2out(machine)+"\n"

        items=j.tools.ms1.listPortforwarding(**args)

        out+="PORTFORWARDING RULES:\n"
        out+=j.servers.cloudrobot.obj2out(items)+"\n"

        return out

    def list(self, **args):
        
        res=j.tools.ms1.listMachinesInSpace(**args)
        out=""
        for item in res:            
            if len(item["nics"])>0:
                ipaddr=item["nics"][0]['ipAddress']
            else:
                ipaddr=""
            out+="%-20s %-20s %s\n"%(item["name"],ipaddr,item["status"])
        return out
        
    def delete(self, **args):
        
        res=j.tools.ms1.deleteMachine(**args)
        if res=="NOTEXIST":
            return "Machine did not exist, no need to delete"
        else:
            return 'Machine %s was deleted successfully ' % args['name']

    def start(self, **args):
        
        status = j.tools.ms1.startMachine(**args)
        return 'Machine %s was started successfully.' % (args['name'])        

    def stop(self, **args):
        
        status = j.tools.ms1.stopMachine(**args)
        return 'Machine %s was stopped successfully.' % (args['name'])        

    def snapshot(self, **args):
        
        status = j.tools.ms1.snapshotMachine(**args)
        return 'Snapshot %s for %s was successfull.' % (args['snapshotname'],args['name'])

    def tcpportforward(self, **args):
        
        status = j.tools.ms1.createTcpPortForwardRule(**args)
        return 'Port-forwarding rule was created successfully.' 

    def udpportforward(self, **args):
        
        status = j.tools.ms1.createUdpPortForwardRule(**args)
        return 'Port-forwarding rule was created successfully.' 

    def execssh(self, **args):
        if args.has_key("default"):
            args["script"]=args["default"]
        
        return j.tools.ms1.execSshScript(**args)

    def deploysshkey(self,**args):
        

        tocheck=["spacesecret","name"]
        for item in tocheck:
            if not args.has_key(item):
                raise RuntimeError("E:Could not find argument:'%s', please specify"%item)

        spacesecret=args.pop("spacesecret")        
        name=args.pop("name")
        ssh=j.tools.ms1._getSSHConnection(spacesecret,name,**args)        

        if args.has_key("key"):
            key=args["key"]
        else:
            if args.has_key("user"):
                user=args["user"]        
            else:
                user=str(self.action.job.session.userid)


            data=self.redis.hget("users",user)
            if data==None:
                raise RuntimeError("E:Could not find user %s, make sure ossusers are synced, can do in channel user: !oss.sync")

            user=json.loads(data)
            key=user["sshpubkey"]

        rloc="/root/.ssh/authorized_keys"
        C=ssh.file_read(rloc)

        idkey=key.split(" ")[-1]
        if idkey.find("@")<>-1:        
            if C.find(idkey)==-1:
                print "add key"
                C+="\nkey\n"
                ssh.file_write(rloc,key)
                return "key deployed"
        return "key was already deployed"

