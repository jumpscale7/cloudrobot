from gevent import monkey
monkey.patch_all()

from JumpScale import j
j.application.start('filerobot')

import JumpScale.lib.cloudrobots

from robots import *

j.servers.cloudrobot.robots
j.servers.cloudrobot.robotspath=j.system.fs.joinPaths(j.dirs.baseDir,"apps","cloudrobot","robots.py")
j.servers.cloudrobot.startFileRobot()

j.application.stop(0)
