from JumpScale import j

class robot_action_osismodelbase(j.code.classGetJSRootModelBase()):
    def __init__(self):
        self._P_guid=""
    
        self._P_jobguid=""
    
        self._P_rscript_channel=""
    
        self._P_rscript_name=""
    
        self._P_userid=""
    
        self._P_name=""
    
        self._P_code=""
    
        self._P_vars=""
    
        self._P_result=""
    
        self._P_out=""
    
        self._P_log=""
    
        self._P_state=""
    
        self._P_start=0
    
        self._P_end=0
    
        self._P_error=""
    
        self._P_id=0
    
        self._P__meta=list()
    
        self._P__meta=["osismodel","robot","action",1] #@todo version not implemented now, just already foreseen
    

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
                msg="property guid input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: action, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_guid=value
    @guid.deleter
    def guid(self):
        del self._P_guid


    @property
    def jobguid(self):
        return self._P_jobguid
    @jobguid.setter
    def jobguid(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property jobguid input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: action, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_jobguid=value
    @jobguid.deleter
    def jobguid(self):
        del self._P_jobguid


    @property
    def rscript_channel(self):
        return self._P_rscript_channel
    @rscript_channel.setter
    def rscript_channel(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property rscript_channel input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: action, value was:" + str(value)
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
                msg="property rscript_name input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: action, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_rscript_name=value
    @rscript_name.deleter
    def rscript_name(self):
        del self._P_rscript_name


    @property
    def userid(self):
        return self._P_userid
    @userid.setter
    def userid(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property userid input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: action, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_userid=value
    @userid.deleter
    def userid(self):
        del self._P_userid


    @property
    def name(self):
        return self._P_name
    @name.setter
    def name(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property name input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: action, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_name=value
    @name.deleter
    def name(self):
        del self._P_name


    @property
    def code(self):
        return self._P_code
    @code.setter
    def code(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property code input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: action, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_code=value
    @code.deleter
    def code(self):
        del self._P_code


    @property
    def vars(self):
        return self._P_vars
    @vars.setter
    def vars(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property vars input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: action, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_vars=value
    @vars.deleter
    def vars(self):
        del self._P_vars


    @property
    def result(self):
        return self._P_result
    @result.setter
    def result(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property result input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: action, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_result=value
    @result.deleter
    def result(self):
        del self._P_result


    @property
    def out(self):
        return self._P_out
    @out.setter
    def out(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property out input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: action, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_out=value
    @out.deleter
    def out(self):
        del self._P_out


    @property
    def log(self):
        return self._P_log
    @log.setter
    def log(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property log input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: action, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_log=value
    @log.deleter
    def log(self):
        del self._P_log


    @property
    def state(self):
        return self._P_state
    @state.setter
    def state(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property state input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: action, value was:" + str(value)
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
                msg="property start input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: action, value was:" + str(value)
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
                msg="property end input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: action, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_end=value
    @end.deleter
    def end(self):
        del self._P_end


    @property
    def error(self):
        return self._P_error
    @error.setter
    def error(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property error input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: action, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_error=value
    @error.deleter
    def error(self):
        del self._P_error


    @property
    def id(self):
        return self._P_id
    @id.setter
    def id(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property id input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: action, value was:" + str(value)
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
                msg="property _meta input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: action, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P__meta=value
    @_meta.deleter
    def _meta(self):
        del self._P__meta

