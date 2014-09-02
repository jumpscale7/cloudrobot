

from JumpScale import j



import JumpScale.lib.cloudrobots

j.servers.cloudrobot.init()

login=j.servers.cloudrobot.hrd.get("cloudrobot.xmpp.login")
passwd=j.servers.cloudrobot.hrd.get("cloudrobot.xmpp.passwd")

print login
print passwd
j.servers.cloudrobot.startXMPPRobot(login,passwd)

j.application.stop(0)
