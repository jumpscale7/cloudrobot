from JumpScale import j

class robot_rscript_history_osismodelbase(j.code.classGetJSRootModelBase()):
    def __init__(self):
        self._P_name=""
    
        self._P_content=""
    
        self._P_channel=""
    
        self._P_descr=""
    
        self._P_modtime=""
    
        self._P_user=""
    
        self._P_id=0
    
        self._P_guid=""
    
        self._P__meta=list()
    
        self._P__meta=["osismodel","robot","rscript_history",1] #@todo version not implemented now, just already foreseen
    

        pass

    @property
    def name(self):
        return self._P_name
    @name.setter
    def name(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property name input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: rscript_history, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_name=value
    @name.deleter
    def name(self):
        del self._P_name


    @property
    def content(self):
        return self._P_content
    @content.setter
    def content(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property content input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: rscript_history, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_content=value
    @content.deleter
    def content(self):
        del self._P_content


    @property
    def channel(self):
        return self._P_channel
    @channel.setter
    def channel(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property channel input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: rscript_history, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_channel=value
    @channel.deleter
    def channel(self):
        del self._P_channel


    @property
    def descr(self):
        return self._P_descr
    @descr.setter
    def descr(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property descr input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: rscript_history, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_descr=value
    @descr.deleter
    def descr(self):
        del self._P_descr


    @property
    def modtime(self):
        return self._P_modtime
    @modtime.setter
    def modtime(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property modtime input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: rscript_history, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_modtime=value
    @modtime.deleter
    def modtime(self):
        del self._P_modtime


    @property
    def user(self):
        return self._P_user
    @user.setter
    def user(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property user input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: rscript_history, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_user=value
    @user.deleter
    def user(self):
        del self._P_user


    @property
    def id(self):
        return self._P_id
    @id.setter
    def id(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property id input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: rscript_history, value was:" + str(value)
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
                msg="property guid input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: rscript_history, value was:" + str(value)
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
                msg="property _meta input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: rscript_history, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P__meta=value
    @_meta.deleter
    def _meta(self):
        del self._P__meta

