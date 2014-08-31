from JumpScale import j
import JumpScale.lib.txtrobot
import ujson as json
import JumpScale.lib.cloudrobots
import time

robotdefinition="""

user (u,users)
- list (l)
-- company #optional

- error

- new (n)
-- firstname
-- lastname
-- ulogin           #7 last letters of lastname, first letter of firstname (if not give then calculated)
-- upasswd
-- company          #comma separated 
-- email            #comma separated list (most relevant email first)
-- alias            #comma separated
-- jabber           #is e.g. main gmail email name 
-- mobile           #comma separated
-- skype
-- role             #ceo,developer,teamlead,sales,syseng,supportl1,supportl2,supportl3,admin,legal,finance (mark all)
-- bitbucketlogin   #login on bitbucket
-- linkedin         #id on linkedin
-- dsakey           #key for sshaccess (pub)
-- gmail            #main gmail account, if not filled in will take first email add
-- dropbox

- get (g)
-- ulogin


- check (c)

"""
import JumpScale.portal

class TestRobot(object):
    def getRobot(self):
        robot = j.tools.txtrobot.get(robotdefinition)
        cmds = UserCmds()
        robot.addCmdClassObj(cmds)
        return robot

class UserCmds():
    def __init__(self):
        self.alwaysdie=False
        self.channel="test"
        self.redis=j.clients.redis.getRedisClient("127.0.0.1", 7768)        


    def user__new(self, **args):
        return 'User created successfully.'


    def user__error(self):
        raise RuntimeError("just an error")

    def user__list(self,**args):       
        out=""
        for i in range(10):
            out+=self.user__get()
            out+="\n"
                
        return out


    def user__get(self, **args):    
        out="""
name=aperson
tel=atel
emails=1,2
"""
        return out

    def user__check(self,**args):
        return "OK"

