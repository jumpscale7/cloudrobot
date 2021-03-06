from JumpScale import j

class robot_job_osismodelbase(j.code.classGetJSRootModelBase()):
    def __init__(self):
        self._P_guid=""
    
        self._P_rscript_channel=""
    
        self._P_rscript_name=""
    
        self._P_rscript_content=""
    
        self._P_vars=""
    
        self._P_sessionid=""
    
        self._P_onetime=True
    
        self._P_userid=""
    
        self._P_state=""
    
        self._P_start=0
    
        self._P_end=0
    
        self._P_actions=list()
    
        self._P_error=""
    
        self._P_out=""
    
        self._P_id=0
    
        self._P__meta=list()
    
        self._P__meta=["osismodel","robot","job",1] #@todo version not implemented now, just already foreseen
    

        pass

    @property
    def guid(self):
        return self._P_guid
    @guid.setter
    def guid(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property guid input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: job, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_guid=value
    @guid.deleter
    def guid(self):
        del self._P_guid


    @property
    def rscript_channel(self):
        return self._P_rscript_channel
    @rscript_channel.setter
    def rscript_channel(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property rscript_channel input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: job, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_rscript_channel=value
    @rscript_channel.deleter
    def rscript_channel(self):
        del self._P_rscript_channel


    @property
    def rscript_name(self):
        return self._P_rscript_name
    @rscript_name.setter
    def rscript_name(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property rscript_name input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: job, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_rscript_name=value
    @rscript_name.deleter
    def rscript_name(self):
        del self._P_rscript_name


    @property
    def rscript_content(self):
        return self._P_rscript_content
    @rscript_content.setter
    def rscript_content(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property rscript_content input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: job, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_rscript_content=value
    @rscript_content.deleter
    def rscript_content(self):
        del self._P_rscript_content


    @property
    def vars(self):
        return self._P_vars
    @vars.setter
    def vars(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property vars input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: job, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_vars=value
    @vars.deleter
    def vars(self):
        del self._P_vars


    @property
    def sessionid(self):
        return self._P_sessionid
    @sessionid.setter
    def sessionid(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property sessionid input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: job, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_sessionid=value
    @sessionid.deleter
    def sessionid(self):
        del self._P_sessionid


    @property
    def onetime(self):
        return self._P_onetime
    @onetime.setter
    def onetime(self, value):
        
        if not isinstance(value, bool) and value is not None:
            if isinstance(value, basestring) and j.basetype.boolean.checkString(value):
                value = j.basetype.boolean.fromString(value)
            else:
                msg="property onetime input error, needs to be bool, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: job, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_onetime=value
    @onetime.deleter
    def onetime(self):
        del self._P_onetime


    @property
    def userid(self):
        return self._P_userid
    @userid.setter
    def userid(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property userid input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: job, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_userid=value
    @userid.deleter
    def userid(self):
        del self._P_userid


    @property
    def state(self):
        return self._P_state
    @state.setter
    def state(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property state input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: job, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_state=value
    @state.deleter
    def state(self):
        del self._P_state


    @property
    def start(self):
        return self._P_start
    @start.setter
    def start(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property start input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: job, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_start=value
    @start.deleter
    def start(self):
        del self._P_start


    @property
    def end(self):
        return self._P_end
    @end.setter
    def end(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property end input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: job, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_end=value
    @end.deleter
    def end(self):
        del self._P_end


    @property
    def actions(self):
        return self._P_actions
    @actions.setter
    def actions(self, value):
        
        if not isinstance(value, list) and value is not None:
            if isinstance(value, basestring) and j.basetype.list.checkString(value):
                value = j.basetype.list.fromString(value)
            else:
                msg="property actions input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: job, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_actions=value
    @actions.deleter
    def actions(self):
        del self._P_actions


    @property
    def error(self):
        return self._P_error
    @error.setter
    def error(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property error input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: job, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_error=value
    @error.deleter
    def error(self):
        del self._P_error


    @property
    def out(self):
        return self._P_out
    @out.setter
    def out(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property out input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: job, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_out=value
    @out.deleter
    def out(self):
        del self._P_out


    @property
    def id(self):
        return self._P_id
    @id.setter
    def id(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property id input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: job, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_id=value
    @id.deleter
    def id(self):
        del self._P_id


    @property
    def _meta(self):
        return self._P__meta
    @_meta.setter
    def _meta(self, value):
        
        if not isinstance(value, list) and value is not None:
            if isinstance(value, basestring) and j.basetype.list.checkString(value):
                value = j.basetype.list.fromString(value)
            else:
                msg="property _meta input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: job, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P__meta=value
    @_meta.deleter
    def _meta(self):
        del self._P__meta

