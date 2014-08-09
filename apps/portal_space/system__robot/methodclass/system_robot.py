from JumpScale import j
import JumpScale.baselib.redis
import ujson as json
import JumpScale.lib.cloudrobots
import sys
sys.path.append("/opt/jumpscale/apps/cloudrobot/")
import robots
import grequests as requests

class system_robot(j.code.classGetBase()):
    """
    list the robot scripts
    
    """
    def __init__(self):
        
        self._te={}
        self.actorname="robot"
        self.appname="system"
        #system_robot_osis.__init__(self)
        self.osis = j.core.osis.getClient(user='root')
        self.osis_rscript=j.core.osis.getClientForCategory(self.osis, 'robot', 'rscript')
        self.osis_job=j.core.osis.getClientForCategory(self.osis, 'robot', 'job')
        self.osis_user=j.core.osis.getClientForCategory(self.osis, 'system', 'user')
        self.robots=robots.robots
        self.redis=j.clients.redis.getGeventRedisClient('127.0.0.1', 7768)

    def authenticate(self, user=None, password=None, **kwargs):
        ctx = kwargs['ctx']
        if ctx.env['beaker.session']['user'] and ctx.env['beaker.session']['user'] != 'guest':
            ctx.start_response('200 OK', (('Content-type', 'application/json'),))
            return ctx.env['beaker.session']['user']
        if not(user and password) or (not ctx.env['beaker.session']['user'] or ctx.env['beaker.session']['user'] == 'guest'):
            ctx.start_response('401 Unauthorized', (('Content-type', 'application/json'),))
            return 'Please login'
        result = self.osis_user.authenticate(user, password)
        if result['authenticated']:
            ctx.start_response('200 OK', (('Content-type', 'application/json'),))
            return result['authkey']
        elif result['exists']:
            ctx.start_response('401 Unauthorized', (('Content-type', 'application/json'),))
            return 'Password is not correct. Pease try again'
        else:
            ctx.start_response('404 Not Found', (('Content-type', 'application/json'),))
            return 'User name %s does not exist' % user

    def job_get(self, jobguid, **kwargs):
        """
        param:jobguid 
        result str
        """
        job=None
        if self.redis.hexists("robot:jobs",jobguid):
            jobdata=self.redis.hget("robot:jobs",jobguid)
            job=json.loads(jobdata)
            if job.has_key('_P_id'):
                self.redis.hdel("robot:jobs",jobguid)            
        else:
            job=self.osis_job.get(jobguid)
            if not job:
                return "No job with guid '%s' found" % jobguid
            job=job.obj2dict()
        if job.has_key("_meta"):
            job.pop("_meta")
        if job.has_key("_meta"):            
            job.pop("_meta")
        return job

    def log_get(self, jobguid, level, fromline, **kwargs):
        """
        param:jobguid 
        param:level 1-5 (1=public;2=out;3=error;4=internal;5=debug)
        param:category optional
        param:fromline 
        result str
        """
        job=self.job_get(jobguid)
        log=job["log"]
        if level==None:
            level=0
        level=int(level)
        if fromline==None:
            fromline=0
        out=""
        linenr=0
        for item in log.split("\n"):
            linenr+=1
            if item.strip()=="":
                continue
            level0,line=item.split(":",1)
            level0=int(level)            
            if linenr>fromline:
                if level0>level:
                    out+="%s\n"%line
        return out

    def rscript_delete(self, name, channel, secrets, **kwargs):
        """
        delete a robot script
        param:name 
        param:channel channel e.g. machine,youtrack
        param:secrets secrets used if any; scripts can have secrets attached to them (comma separated)
        result str
        """
        result=self._rscriptfind(name,filter="", channel=channel, secrets=secrets)
        if len(result)>1:
            #raise RuntimeError("Too many results, can only get 1, be more specific.")
            return "TOOMANY" 
        elif len(result)==1:
            self.osis_rscript.delete(key=result[0]["guid"])
            return "OK"
        else:
            return "NOTFOUND"

    def _parsetree(self, value, result, fullresult=[], secrets=[]):
        result = list()
        def processNode(val, children):
            for key, v in val.iteritems():
                newchildren = list()
                node = {'roleName': key, 'children': newchildren}
                children.append(node)
                if 'secretsoftherscriptset' in v:
                    scriptsecrets = v.pop('secretsoftherscriptset')
                    sentsecrets = [str(secret) for secret in secrets.split(',')] if secrets else []
                    sentsecrets.append('')
                    scriptsecrets = scriptsecrets or []
                    node['secrets'] = list(set(sentsecrets).intersection(set(scriptsecrets)))

                if v:
                    processNode(v, newchildren)

        processNode(value, result)
        return result

    def rscript_treeview(self, secrets, **kwargs):
        """
        build treeview of rscripts
        param:secrets secrets used if any; scripts can have secrets attached to them (comma separated)
        result dict
        """              

        result = self._rscriptfind(secrets=secrets)
        result2 = dict()
        for item in result:
            result2.setdefault(item['channel'], {})
            t = result2[item['channel']]
            for part in item['name'].split('.'):
                t = t.setdefault(part, {})
            t.setdefault('secretsoftherscriptset', item['secrets'])

        result = list()
        for channel, children in result2.iteritems():
            result.append(self._parsetree({channel:children}, [], secrets=secrets))

        return result  

    def rscript_execute(self, name, channel, secrets, wait=1,**kwargs):
        """
        execute a script, returns job_longid
        param:name 
        param:channel channel e.g. machine,youtrack
        param:secrets secrets used if any; scripts can have secrets attached to them (comma separated)
        result str which is guid of job
        """
        result=self._rscriptfind(name,filter="", channel=channel, secrets=secrets)
        if len(result)>1:
            #raise RuntimeError("Too many results, can only get 1, be more specific.")
            return "TOOMANY"
        elif len(result)==0:
            #raise RuntimeError("Could not find %s/%s"%(name, channel))
            return "NOTFOUND"
        snippet = result[0]['content']
        ctx=kwargs["ctx"]
        username = ctx.env["beaker.session"]["user"]

        users = self.osis_user.simpleSearch({'id': username})
        if len(users)>0:
            user=users[0]["id"]
        else:
            raise RuntimeError("Authentication error: user not found.")

        channel = result[0]['channel']


        jobguid=j.servers.cloudrobot.toFileRobot(channel,snippet,user,name)

        if str(wait)=="1":
            j.servers.cloudrobot.jobWait(jobguid)
            job=self.job_get(jobguid)
            return job
        else:
            return jobguid
    
    def rscript_execute_once(self, name,channel,rscript, wait=1, **kwargs):
        """
        execute a script, returns job_longid
        param:rscript the content of the script
        result str
        """
        if name=="" or name==None:
            name="unknown"


        ctx=kwargs["ctx"]
        username = ctx.env["beaker.session"]["user"]
        users = self.osis_user.simpleSearch({'id': username})
        if len(users)>0:
            user=users[0]["id"]
        else:
            raise RuntimeError("Authentication error: user not found.")

        jobguid=j.servers.cloudrobot.toFileRobot(channel,rscript,user,name)

        if str(wait)=="1":
            j.servers.cloudrobot.jobWait(jobguid)
            job=self.job_get(jobguid)
            return job
        else:
            return jobguid

    def rscript_exists(self, name, channel, secrets, **kwargs):
        """
        check if rscript exists
        param:name 
        param:channel channel e.g. machine,youtrack
        param:secrets secrets used if any; scripts can have secrets attached to them (comma separated)
        result bool
        """
        result=self._rscriptfind(name,filter="", channel=channel, secrets=secrets)
        return len(result)==1

    def rscript_get(self, name, channel, secrets, **kwargs):
        """
        get a robot script
        param:name 
        param:channel channel e.g. machine,youtrack
        param:secrets secrets used if any; scripts can have secrets attached to them (comma separated)
        result str
        """
        result=self._rscriptfind(name,filter="", channel=channel, secrets=secrets)
        if len(result)>1:
            #raise RuntimeError("Too many results, can only get 1, be more specific.")
            return "TOOMANY"
        elif len(result)==0:
            #raise RuntimeError("Could not find %s/%s"%(name, channel))
            return "NOTFOUND"

        item = result[0]
        item.pop("_ckey")
        item.pop("guid")

        sentsecrets = [str(secret) for secret in secrets.split(',')] if secrets else []
        sentsecrets.append('')
        item['secrets'] = [str(secret) for secret in item['secrets']] if item['secrets'] else []
        item['secrets'] = list(set(sentsecrets).intersection(set(item['secrets'])))
        return item
    

    def rscript_list(self, filter, channel, secrets, **kwargs):
        """
        param:filter any part of name (^machine. would mean at start of name)
        param:channel channel e.g. machine,youtrack
        param:type optional category
        param:secrets secrets used if any; scripts can have secrets attached to them (comma separated)
        result list
        """
        result=self._rscriptfind("",filter, channel, secrets)
        result2=[]
        for item in result:
            item.pop("_ckey")
            item.pop("guid")
            result2.append(item)
        return result2

    def _rscriptfind(self, name="",filter="", channel="", secrets=""):
        cl=self.osis_rscript
        query=dict()
        if name==None:
            name=""
        if name<>"":
            query['name']=name
        if filter==None:
            filter=""        
        if channel==None:
            channel=""
        if channel<>"":
            query['channel']=channel
        
        
        if secrets == None:
            secrets = ''
        secrets = [secret.strip() for secret in secrets.split(',')]
        secrets.append('') if not '' in secrets else ''

        result=[]
        total, items = cl.simpleSearch(query, withtotal=True)
        for item in items:
            found=True
            if secrets<>[] and item["secrets"]<>[]:                
                sfound=False
                for secrToCheck in secrets:
                    if secrToCheck in item["secrets"]:
                        sfound=True
                if not sfound:
                    found=False
            elif secrets==[] and item["secrets"]<>[]:
                found=False
            if filter<>"":
                ffound=False
                if filter[0]=="^":
                    filter=filter[1:]
                    if item["name"].find(filter)==0:
                        ffound=True
                else:
                    if item["name"].find(filter)<>-1:
                        ffound=True
                if not ffound:
                    found=False
            if found:
                result.append(item)
        return result

    def _jobfind(self, filter="", channel="", secrets="",ago=0):
        jobs=[]
        rscripts=self._rscriptfind(filter=filter, channel=channel, secrets=secrets)
        cl=self.osis_job
        if ago==None or ago=="":
            ago=0
        if ago<>0:
            ago=j.base.time.getEpochAgo(ago)

        for rscript in rscripts:
            query = {"rscript_name": rscript["name"], "rscript_channel": rscript["channel"]}
            if ago:
                query.update({'start': {'eq': 'from', 'value': ago, 'name':'start'}})
            for job in cl.simpleSearch(query):
                if isinstance(job, dict):
                    jobs.append(job)

        return jobs

                        
    def rscript_set(self, name, channel, rscript, secrets, **kwargs):
        """
        write a robot script
        tip: use dot notation  e.g. machine.create.york.kds
        param:name 
        param:channel channel e.g. machine,youtrack
        param:rscript the content of the script
        param:secrets secrets used if any; scripts can have secrets attached to them (comma separated)
        result str
        """
        if secrets == None:
            secrets = ''
        exists = self._rscriptfind(name=name, channel=channel, secrets=secrets)
        secrets = [secret.strip() for secret in secrets.split(',')]
        if exists:
            exists = exists[0]
            exists['rscript'] = rscript
            exists['secrets'].extend(secrets)
            exists['secrets'] = list(set(exists['secrets']))
            self.osis_rscript.set(exists)
            return "Updated"
        rs = self.osis_rscript.new()
        rs.name = name
        rs.channel = channel
        rs.content = rscript
        rs.secrets = secrets
        self.osis_rscript.set(rs)
        return "OK"

    def secrets_get(self, **kwargs):
        """
        secrets which belong to user are retrieved
        result str
        """
        ctx = kwargs['ctx']
        user_id = ctx.env["beaker.session"]["user"]        
        if self.redis.hexists('oss:users', user_id):
            ctx.start_response('200 OK', (('Content-type', 'application/json'),))
            return json.loads(self.redis.hget('oss:users', user_id))
        else:
            ctx.start_response('404 Not Found', (('Content-type', 'application/json'),))
            return 'User %s does not have secrets. Please call secrets_set first' % user_id

    def secrets_set(self, secrets, **kwargs):
        """
        secrets which will be remembered per user
        param:secrets 
        result str
        """
        ctx = kwargs['ctx']
        user_id = ctx.env["beaker.session"]["user"] 
        self.redis.hset('oss:users', user_id, json.dumps(secrets))
        ctx.start_response('200 OK', (('Content-type', 'application/json'),))
        return 'User %s secrets were set successfully' % user_id

    def syntax_channel_get(self, channel, **kwargs):
        """
        get syntax for channel
        param:channel channel e.g. machine,youtrack
        result str
        """
        robot=self.robots[channel]
        return robot.definition    

    def syntax_help(self, **kwargs):
        """
        generic help text for syntax format
        result str
        """        
        robot=self.robots["machine"]
        out=""
        out+=robot.help.help()
        out+="\n\nHELP ON THE SYNTAX FILE FOR A ROBOT CHANNEL:\n"
        out+="============================================\n"
        out+=robot.help.help_definition()
        out+="\n\n"
        print out
        return out    

    def job_list(self, channel, filter, secrets, ago, **kwargs):
        """
        jobs are listed which belong to user
        param:channel channel e.g. machine,youtrack
        param:filter any part of name (^machine. would mean at start of name)
        param:from examples -4d;-4h
        result str
        """
        return self._jobfind(filter=filter, channel=channel, secrets=secrets,ago=ago)
    
