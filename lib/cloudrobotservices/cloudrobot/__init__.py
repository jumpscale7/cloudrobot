from JumpScale import j
j.base.loader.makeAvailable(j, 'robots')

from .CloudRobot import CloudRobot
j.robots.cloudrobot = CloudRobot()