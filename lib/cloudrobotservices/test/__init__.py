from JumpScale import j
j.base.loader.makeAvailable(j, 'robots')

from .TestRobot import TestRobot
j.robots.test = TestRobot()

