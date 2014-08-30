from JumpScale import j
j.base.loader.makeAvailable(j, 'robots')

from .RobotMgmt import RobotMgmt
j.robots.mgmt = RobotMgmt()

