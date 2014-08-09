[actor] 
    """
    """

    method:authenticate @noauth
        """
        authenticates a user and returns their authkey
        """
        var:user str,, @tags: optional
        var:password str,, @tags: optional
        result:str

    method:rscript_list @noauth
        """     
        list the robot scripts
        """
        var:filter str,,any part of name (^machine. would mean at start of name) @tags: optional 
        var:channel str,,channel e.g. machine,youtrack @tags: optional 
        var:secrets str,,secrets used if any; scripts can have secrets attached to them (comma separated) @tags: optional
        result:list

    method:rscript_treeview @noauth
        """     
        build treeview of rscripts
        """
        var:secrets str,,secrets used if any; scripts can have secrets attached to them (comma separated) @tags: optional
        result:dict


    method:rscript_get @noauth
        """     
        get a robot script
        """
        var:name str,,@tags: optional
        var:channel str,,channel e.g. machine,youtrack @tags: optional 
        var:secrets str,,secrets used if any; scripts can have secrets attached to them (comma separated) @tags: optional
        result:str


    method:rscript_set @noauth
        """     
        write a robot script
        tip: use dot notation  e.g. machine.create.york.kds
        """
        var:name str,,
        var:channel str,,channel e.g. machine,youtrack
        var:rscript str,,the content of the script
        var:secrets str,,secrets used if any; scripts can have secrets attached to them (comma separated) @tags: optional
        result:str

    method:rscript_delete @noauth
        """     
        delete a robot script
        """
        var:name str,,
        var:channel str,,channel e.g. machine,youtrack @tags: optional 
        var:secrets str,,secrets used if any; scripts can have secrets attached to them (comma separated) @tags: optional
        result:str        

    method:rscript_execute @noauth
        """     
        execute a script, returns job_longid
        """
        var:name str,,@tags: optional 
        var:channel str,,channel e.g. machine,youtrack @tags: optional 
        var:secrets str,,secrets used if any; scripts can have secrets attached to them (comma separated) @tags: optional
        var:wait int,1,1 means yes; 0 no@tags: optional 
        result:str

    method:rscript_execute_once @noauth
        """     
        execute a script, returns job_longid
        """        
        var:rscript str,,the content of the script
        var:name str,,@tags: optional 
        var:channel str,,channel e.g. machine,youtrack        
        var:wait int,1,1 means yes; 0 no@tags: optional 
        result:str

    method:syntax_channel_get @noauth
        """     
        get syntax for channel
        """        
        var:channel str,,channel e.g. machine,youtrack 
        result:str

    method:syntax_help @noauth
        """     
        generic help text for syntax format
        """        
        result:str

    method: secrets_get @noauth
        """
        secrets which belong to user are retrieved
        """
        result:str

    method: secrets_set @noauth
        """
        secrets which will be remembered per user
        """
        var:secrets str,,
        result:str


    method:rscript_exists @noauth
        """     
        check if rscript exists
        """
        var:name str,,
        var:channel str,,channel e.g. machine,youtrack @tags: optional 
        var:secrets str,,secrets used if any; scripts can have secrets attached to them (comma separated) @tags: optional
        result:bool

    method:log_get @noauth
        var:jobguid str,,
        var:level int,,1-5 (1=public;2=out;3=error;4=internal;5=debug) @tags: optional 
        var:fromline int,, @tags: optional 
        result:str

    method:job_get @noauth
        var:jobguid str,,
        result:str

    method:job_list @noauth
        """
        jobs are listed which belong to user
        """
        var:channel str,,channel e.g. machine,youtrack @tags: optional 
        var:secrets str,,secrets used if any; scripts can have secrets attached to them (comma separated) @tags: optional
        var:filter str,,any part of name (^machine. would mean at start of name) @tags: optional
        var:ago str,,examples -4d;-4h  @tags: optional
        result:str
