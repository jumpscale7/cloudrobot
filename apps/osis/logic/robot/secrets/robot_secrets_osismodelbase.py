from JumpScale import j

class robot_secrets_osismodelbase(j.code.classGetJSRootModelBase()):
    def __init__(self):
        self._P_user=""
    
        self._P_secrets=""
    
        self._P_id=0
    
        self._P_guid=""
    
        self._P__meta=list()
    
        self._P__meta=["osismodel","robot","secrets",1] #@todo version not implemented now, just already foreseen
    

        pass

    @property
    def user(self):
        return self._P_user
    @user.setter
    def user(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property user input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: secrets, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_user=value
    @user.deleter
    def user(self):
        del self._P_user


    @property
    def secrets(self):
        return self._P_secrets
    @secrets.setter
    def secrets(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property secrets input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: secrets, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_secrets=value
    @secrets.deleter
    def secrets(self):
        del self._P_secrets


    @property
    def id(self):
        return self._P_id
    @id.setter
    def id(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property id input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: secrets, value was:" + str(value)
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
                msg="property guid input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: secrets, value was:" + str(value)
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
                msg="property _meta input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: secrets, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P__meta=value
    @_meta.deleter
    def _meta(self):
        del self._P__meta

