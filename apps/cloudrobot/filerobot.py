from JumpScale import j
j.application.start('filerobot')

import JumpScale.lib.cloudrobots

j.servers.cloudrobot.init()
j.servers.cloudrobot.startFileRobot()

j.application.stop(0)
