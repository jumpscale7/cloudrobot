from JumpScale import j

# import ujson as json
# import JumpScale.baselib.redis

# import JumpScale.portal
import JumpScale.lib.ms1

class Cmds():
    
    def getfree_ip_port(self,**args):
        
        res=j.tools.ms1.getFreeIpPort(**args)
        out=""
        for key,val in res.iteritems():
            j.cloudrobot.vars[key]=val
            out+="$%s=%s\n"%(key,val)
        return out


