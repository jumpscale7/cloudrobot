from JumpScale import j
import JumpScale.lib.txtrobot
import ujson as json
import JumpScale.lib.cloudrobots

robotdefinition="""

script (s,scripts)
- list (l)
-- channel          #optional
-- secrets          #secret used in scripts

- execute (e)
-- name 
-- channel

- get (g)
-- name 
-- channel

"""
import JumpScale.portal

class RobotMgmt(object):
    def getRobot(self):
        robot = j.tools.txtrobot.get(robotdefinition)
        cmds = RobotMgmtCmds()
        robot.addCmdClassObj(cmds)
        return robot

class RobotMgmtCmds():
    def __init__(self):
        self.channel="mgmt"
        self.redis=j.clients.redis.getRedisClient("127.0.0.1", 7768)        

