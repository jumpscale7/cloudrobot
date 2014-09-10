from JumpScale import j
import JumpScale.lib.txtrobot
import ujson as json
import JumpScale.lib.cloudrobots

robotdefinition = """

rscript (rscripts)
- list (l)
-- name             #optional
-- channel          #optional
-- secrets          #secret used in scripts

- get (g)
-- guid

- delete (d, remove)
-- guid

- new (n, create, c)
-- name 
-- content 
-- channel 
-- descr 
-- secrets


job (jobs)
- list (l)
-- rscript_channel 
-- rscript_name 
-- state           #(ERROR,OK,RUNNING,PENDING)

- get (g)
-- guid 

- delete (d, remove)
-- guid

- new (n, create, c)
-- rscript_channel 
-- rscript_name 
-- rscript_content 
-- vars 
-- sessionid 
-- onetime
-- userid 
-- state            #(ERROR,OK,RUNNING,PENDING)
-- start 
-- end 
-- actions 
-- error 
-- out 


action (actions)
- list (l)
-- rscript_channel 
-- rscript_name 
-- jobguid
-- state           #(ERROR,OK,RUNNING,PENDING)

- get (g)
-- guid 

- delete (d, remove)
-- guid

- new (n, create, c)
-- jobguid 
-- rscript_channel 
-- rscript_name     
-- userid 
-- name 
-- code 
-- vars 
-- result 
-- log 
-- state  
-- start 
-- end
-- error 

provider (providers)
- list (l)
-- type 
-- location 
-- secret

- get (g)
-- guid 

- delete (d, remove)
-- guid

- new (n, create, c)
-- name 
-- type                    #amazon;digitalocean;google;dedicated;ms1
-- location
-- descr 
-- acl 
-- login 
-- secret 
-- params

resourcemachine (resourcemachines)
- list (l)
-- name 
-- provider 
-- location

- get (g)
-- guid 

- delete (d, remove)
-- guid

- new (n, create, c)
-- name 
-- descr 
-- provider 
-- location 
-- acl 
-- ipv4 
-- ipv6 
-- rootpasswd 
-- cpucores 
-- cpumhz 
-- ssd_size 
-- disk_size 
-- mem_size 
-- cost 
-- ssd_used 
-- disk_used 
-- mem_used 
-- cpu_used 
-- cost_distr_ssd 
-- cost_distr_disk 
-- cost_distr_compute 
"""
import JumpScale.portal
import JumpScale.lib.cloudrobots
import JumpScale.grid.osis
import json


class CloudRobot(object):

    def getRobot(self):
        robot = j.tools.txtrobot.get(robotdefinition)
        cmds = CloudRobotCmds()
        robot.addCmdClassObj(cmds)
        return robot


class CloudRobotCmds():

    def __init__(self):
        self.robotclient = j.core.osis.getClientForNamespace('robot', None)
        j.servers.cloudrobot.init()

    def rscript__new(self, **args):
        secrets = json.loads(args.get('secrets', '[]'))
        rscript = self.robotclient.rscript.new()
        rscript.channel = args.get('channel', None)
        rscript.content = args.get('content', None)
        rscript.descr = args.get('descr', None)
        rscript.name = args.get('name', None)
        rscript.secrets = secrets
        guid = self.robotclient.rscript.set(rscript)[0]
        return 'RScript created successfully. RScript GUID: %s ' % guid

    def rscript__list(self, **args):
        secrets = json.loads(args.get('secrets', '[]'))
        rscripts = self.robotclient.rscript.simpleSearch({'channel': args.get(
            'channel', None), 'name': args.get('name', None), 'secrets': secrets})
        return rscripts

    def rscript__delete(self, **args):
        try:
            self.robotclient.rscript.delete(args.get('guid', None))
            return 'RScript with GUID "%s" has been successfully deleted.' % args.get('guid', None)
        except Exception:
            return 'RScript with GUID "%s" could not be deleted.' % args.get('guid', None)

    def rscript__get(self, **args):
        try:
            rscript = self.robotclient.rscript.get(args.get('guid', None))
            return rscript.dump()
        except Exception:
            return 'RScript with GUID "%s" could not be found.' % args.get('guid', None)

    def job__new(self, **args):
        job = j.servers.cloudrobot.osis_robot_job.new()
        job.rscript_channel = args.get('rscript_channel', None)
        job.rscript_content = args.get('rscript_content', None)
        job.vars = args.get('vars', None)
        job.rscript_name = args.get('rscript_name', None)
        job.sessionid = args.get('sessionid', None)
        job.onetime = args.get('onetime', None)
        job.userid = args.get('userid', None)
        job.state = args.get('state', None)
        job.start = args.get('start', None)
        job.end = args.get('end', None)
        job.actions = json.loads(args.get('actions', '[]'))
        job.error = args.get('error', None)
        job.out = args.get('out', None)
        guid = j.servers.cloudrobot.osis_robot_job.set(job)[0]
        return 'Job created successfully. Job GUID: %s ' % guid

    def job__list(self, **args):
        jobs = j.servers.cloudrobot.osis_robot_job.simpleSearch({'rscript_channel': args.get(
            'rscript_channel', None), 'rscript_name': args.get('rscript_name', None), 'state': args.get('state', None)})
        return jobs

    def job__delete(self, **args):
        try:
            j.servers.cloudrobot.osis_robot_job.delete(args.get('guid', None))
            return 'Job with GUID "%s" has been successfully deleted.' % args.get('guid', None)
        except Exception:
            return 'Job with GUID "%s" could not be deleted.' % args.get('guid', None)

    def job__get(self, **args):
        try:
            job = j.servers.cloudrobot.osis_robot_job.get(args.get('guid', None))
            return job.dump()
        except Exception:
            return 'Job with GUID "%s" could not be found.' % args.get('guid', None)

    def action__new(self, **args):
        action = j.servers.cloudrobot.osis_robot_action.new()
        action.jobguid = args.get('jobguid', None)
        action.rscript_channel = args.get('rscript_channel', None)
        action.vars = args.get('vars', None)
        action.rscript_name = args.get('rscript_name', None)
        action.result = args.get('result', None)
        action.code = args.get('code', None)
        action.userid = args.get('userid', None)
        action.name = args.get('name', None)
        action.start = args.get('start', None)
        action.end = args.get('end', None)
        action.error = args.get('error', None)
        action.log = args.get('log', None)
        guid = self.robotclient.action.set(action)[0]
        return 'Action created successfully. Action GUID: %s ' % guid

    def action__list(self, **args):
        actions = j.servers.cloudrobot.osis_robot_action.simpleSearch({'rscript_channel': args.get('rscript_channel', None), 'rscript_name': args.get(
            'rscript_name', None), 'state': args.get('state', None), 'jobguid': args.get('jobguid', None)})
        return actions

    def action__delete(self, **args):
        try:
            j.servers.cloudrobot.osis_robot_action.delete(args.get('guid', None))
            return 'Action with GUID "%s" has been successfully deleted.' % args.get('guid', None)
        except Exception:
            return 'Action with GUID "%s" could not be deleted.' % args.get('guid', None)

    def action__get(self, **args):
        try:
            action = j.servers.cloudrobot.osis_robot_action.get(
                args.get('guid', None))
            return action.dump()
        except Exception:
            return 'Action with GUID "%s" could not be found.' % args.get('guid', None)

    def provider__new(self, **args):
        provider = self.robotclient.provider.new()
        provider.name = args.get('name', None)
        provider.type = args.get('type', None)
        provider.location = args.get('location', None)
        provider.descr = args.get('descr', None)
        provider.acl = args.get('acl', None)
        provider.login = args.get('login', None)
        provider.secret = args.get('secret', None)
        provider.params = args.get('params', None)
        guid = self.robotclient.provider.set(provider)[0]
        return 'Provider created successfully. Provider GUID: %s ' % guid

    def provider__list(self, **args):
        providers = self.robotclient.provider.simpleSearch({'type': args.get('type', None), 'location': args.get(
            'location', None), 'state': args.get('state', None), 'jobguid': args.get('jobguid', None)})
        return providers

    def provider__delete(self, **args):
        try:
            self.robotclient.provider.delete(args.get('guid', None))
            return 'Provider with GUID "%s" has been successfully deleted.' % args.get('guid', None)
        except Exception:
            return 'provider with GUID "%s" could not be deleted.' % args.get('guid', None)

    def provider__get(self, **args):
        try:
            provider = self.robotclient.provider.get(args.get('guid', None))
            return provider.dump()
        except Exception:
            return 'Provider with GUID "%s" could not be found.' % args.get('guid', None)

    def resourcemachine__new(self, **args):
        resourcemachine = self.robotclient.resourcemachine.new()
        resourcemachine.name = args.get('name', None)
        resourcemachine.provider = args.get('provider', None)
        resourcemachine.location = args.get('location', None)
        resourcemachine.descr = args.get('descr', None)
        resourcemachine.acl = args.get('acl', None)
        resourcemachine.ipv4 = args.get('ipv4', None)
        resourcemachine.ipv6 = args.get('ipv6', None)
        resourcemachine.rootpasswd = args.get('rootpasswd', None)
        resourcemachine.cpucores = args.get('cpucores', None)
        resourcemachine.cpumhz = args.get('cpumhz', None)
        resourcemachine.ssd_size = args.get('ssd_size', None)
        resourcemachine.disk_size = args.get('disk_size', None)
        resourcemachine.mem_size = args.get('mem_size', None)
        resourcemachine.cost = args.get('cost', None)
        resourcemachine.ssd_used = args.get('ssd_used', None)
        resourcemachine.disk_used = args.get('disk_used', None)
        resourcemachine.mem_used = args.get('mem_used', None)
        resourcemachine.cpu_used = args.get('cpu_used', None)
        resourcemachine.cost_distr_ssd = args.get('cost_distr_ssd', None)
        resourcemachine.cost_distr_disk = args.get('cost_distr_disk', None)
        resourcemachine.cost_distr_compute = args.get(
            'cost_distr_compute', None)
        guid = self.robotclient.resourcemachine.set(resourcemachine)[0]
        return 'resourcemachine created successfully. resourcemachine GUID: %s ' % guid

    def resourcemachine__list(self, **args):
        resourcemachines = self.robotclient.resourcemachine.simpleSearch({'name': args.get(
            'name', None), 'location': args.get('location', None), 'provider': args.get('provider', None)})
        return resourcemachines

    def resourcemachine__delete(self, **args):
        try:
            self.robotclient.resourcemachine.delete(args.get('guid', None))
            return 'resourcemachine with GUID "%s" has been successfully deleted.' % args.get('guid', None)
        except Exception:
            return 'resourcemachine with GUID "%s" could not be deleted.' % args.get('guid', None)

    def resourcemachine__get(self, **args):
        try:
            resourcemachine = self.robotclient.resourcemachine.get(
                args.get('guid', None))
            return resourcemachine.dump()
        except Exception:
            return 'resourcemachine with GUID "%s" could not be found.' % args.get('guid', None)
