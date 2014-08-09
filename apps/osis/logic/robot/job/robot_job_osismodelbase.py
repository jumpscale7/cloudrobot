from JumpScale import j

class robot_job_osismodelbase(j.code.classGetJSRootModelBase()):
    def __init__(self):
        self._P_uid=""
    
        self._P_rscript_channel=""
    
        self._P_rscript_name=""
    
        self._P_rscript_content=""
    
        self._P_onetime=True
    
        self._P_user=""
    
        self._P_result=""
    
        self._P_log=""
    
        self._P_state=""
    
        self._P_start=0
    
        self._P_end=0
    
        self._P_id=0
    
        self._P_guid=""
    
        self._P__meta=list()
    
        self._P__meta=["osismodel","robot","job",1] #@todo version not implemented now, just already foreseen
    

        pass

    @property
    def uid(self):
        return self._P_uid
    @uid.setter
    def uid(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property uid input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: job, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_uid=value
    @uid.deleter
    def uid(self):
        del self._P_uid


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
    def user(self):
        return self._P_user
    @user.setter
    def user(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property user input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: job, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_user=value
    @user.deleter
    def user(self):
        del self._P_user


    @property
    def result(self):
        return self._P_result
    @result.setter
    def result(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property result input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: job, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_result=value
    @result.deleter
    def result(self):
        del self._P_result


    @property
    def log(self):
        return self._P_log
    @log.setter
    def log(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property log input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: job, value was:" + str(value)
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

