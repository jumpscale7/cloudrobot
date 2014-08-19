from JumpScale import j

class system_robot(j.code.classGetBase()):
    """
    authenticates a user and returns their authkey
    
    """
    def __init__(self):
        
        self._te={}
        self.actorname="robot"
        self.appname="system"
        #system_robot_osis.__init__(self)
    

        pass

    def authenticate(self, user, password, **kwargs):
        """
        param:user 
        param:password 
        result str
        """
        #put your code here to implement this method
        raise NotImplementedError ("not implemented method authenticate")
    

    def job_get(self, jobguid, **kwargs):
        """
        param:jobguid 
        result str
        """
        #put your code here to implement this method
        raise NotImplementedError ("not implemented method job_get")
    

    def job_list(self, channel, secrets, prefix, ago, **kwargs):
        """
        jobs are listed which belong to user
        param:channel channel e.g. machine,youtrack
        param:secrets secrets used if any; scripts can have secrets attached to them (comma separated)
        param:prefix start of name sequence (or full)
        param:ago examples -4d;-4h
        result str
        """
        #put your code here to implement this method
        raise NotImplementedError ("not implemented method job_list")
    

    def log_get(self, jobguid, level, fromline, **kwargs):
        """
        param:jobguid 
        param:level 1-5 (1=public;2=out;3=error;4=internal;5=debug)
        param:fromline 
        result str
        """
        #put your code here to implement this method
        raise NotImplementedError ("not implemented method log_get")
    

    def rscript_delete(self, name, channel, secrets, **kwargs):
        """
        delete a robot script
        param:name 
        param:channel channel e.g. machine,youtrack
        param:secrets secrets used if any; scripts can have secrets attached to them (comma separated)
        result str
        """
        #put your code here to implement this method
        raise NotImplementedError ("not implemented method rscript_delete")
    

    def rscript_execute(self, name, channel, secrets, content, wait=1, **kwargs):
        """
        execute a script, returns job_longid
        param:name 
        param:channel channel e.g. machine,youtrack
        param:secrets secrets used if any; scripts can have secrets attached to them (comma separated)
        param:content 
        param:wait 1 means yes; 0 no default=1
        result str
        """
        #put your code here to implement this method
        raise NotImplementedError ("not implemented method rscript_execute")
    

    def rscript_execute_once(self, content, name, channel, wait=1, **kwargs):
        """
        execute a script, returns job_longid
        param:content the content of the script
        param:name 
        param:channel channel e.g. machine,youtrack
        param:wait 1 means yes; 0 no default=1
        result str
        """
        #put your code here to implement this method
        raise NotImplementedError ("not implemented method rscript_execute_once")
    

    def rscript_exists(self, name, channel, secrets, **kwargs):
        """
        check if rscript exists
        param:name 
        param:channel channel e.g. machine,youtrack
        param:secrets secrets used if any; scripts can have secrets attached to them (comma separated)
        result bool
        """
        #put your code here to implement this method
        raise NotImplementedError ("not implemented method rscript_exists")
    

    def rscript_get(self, name, channel, secrets, **kwargs):
        """
        get a robot script
        param:name 
        param:channel channel e.g. machine,youtrack
        param:secrets secrets used if any; scripts can have secrets attached to them (comma separated)
        result str
        """
        #put your code here to implement this method
        raise NotImplementedError ("not implemented method rscript_get")
    

    def rscript_list(self, filter, channel, secrets, **kwargs):
        """
        list the robot scripts
        param:filter any part of name (^machine. would mean at start of name)
        param:channel channel e.g. machine,youtrack
        param:secrets secrets used if any; scripts can have secrets attached to them (comma separated)
        result list
        """
        #put your code here to implement this method
        raise NotImplementedError ("not implemented method rscript_list")
    

    def rscript_set(self, name, channel, secrets2access, content, secrets, **kwargs):
        """
        write a robot script
        tip: use dot notation  e.g. machine.create.york.kds
        param:name 
        param:channel channel e.g. machine,youtrack
        param:secrets2access secret which is needed to be able to retrieve rscript
        param:content the content of the script
        param:secrets secrets used if any; scripts can have secrets attached to them (comma separated)
        result str
        """
        #put your code here to implement this method
        raise NotImplementedError ("not implemented method rscript_set")
    

    def rscript_treeview(self, secrets, **kwargs):
        """
        build treeview of rscripts
        param:secrets secrets used if any; scripts can have secrets attached to them (comma separated)
        result dict
        """
        #put your code here to implement this method
        raise NotImplementedError ("not implemented method rscript_treeview")
    

    def secrets_get(self, **kwargs):
        """
        secrets which belong to user are retrieved
        result str
        """
        #put your code here to implement this method
        raise NotImplementedError ("not implemented method secrets_get")
    

    def secrets_set(self, secrets, **kwargs):
        """
        secrets which will be remembered per user
        param:secrets 
        result str
        """
        #put your code here to implement this method
        raise NotImplementedError ("not implemented method secrets_set")
    

    def syntax_channel_get(self, channel, **kwargs):
        """
        get syntax for channel
        param:channel channel e.g. machine,youtrack
        result str
        """
        #put your code here to implement this method
        raise NotImplementedError ("not implemented method syntax_channel_get")
    

    def syntax_help(self, **kwargs):
        """
        generic help text for syntax format
        result str
        """
        #put your code here to implement this method
        raise NotImplementedError ("not implemented method syntax_help")
    
