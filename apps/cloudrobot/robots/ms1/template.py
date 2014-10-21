from JumpScale import j

# import ujson as json
# import JumpScale.baselib.redis

# import JumpScale.portal
import JumpScale.lib.ms1

class Cmds():

    def list(self, **args):
        
        out=""
        res=j.tools.ms1.listImages(**args)

        keys=res.keys()
        keys.sort()
        
        for key in keys:
            id,fullname=res[key]
            out+="%-20s (%-2s) %s\n"%(key,id,fullname)
        return out

