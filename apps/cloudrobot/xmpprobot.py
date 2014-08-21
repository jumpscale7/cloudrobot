

from JumpScale import j



import JumpScale.lib.cloudrobots

import sys

args=sys.argv

from robots import *

login=j.servers.cloudrobot.hrd.get("cloudrobot.xmpp.login")
passwd=j.servers.cloudrobot.hrd.get("cloudrobot.xmpp.passwd")

print login
print passwd
j.servers.cloudrobot.startXMPPRobot(login,passwd,robots=robots)

j.application.stop(0)
