from JumpScale import j


# import ujson as json
# import JumpScale.baselib.redis

# import JumpScale.portal
import JumpScale.lib.ms1

class Cmds():

    def login(self, **args):
        
        result = j.tools.ms1.setClouspaceSecret(**args)
        return "spacesecret=%s" % (result)

