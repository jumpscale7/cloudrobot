from JumpScale import j

class robot_provider_osismodelbase(j.code.classGetJSRootModelBase()):
    def __init__(self):
        self._P_name=""
    
        self._P_type=""
    
        self._P_descr=""
    
        self._P_acl=list()
    
        self._P_id=0
    
        self._P_guid=""
    
        self._P__meta=list()
    
        self._P__meta=["osismodel","robot","provider",1] #@todo version not implemented now, just already foreseen
    

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
                msg="property name input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: provider, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_name=value
    @name.deleter
    def name(self):
        del self._P_name


    @property
    def type(self):
        return self._P_type
    @type.setter
    def type(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property type input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: provider, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_type=value
    @type.deleter
    def type(self):
        del self._P_type


    @property
    def descr(self):
        return self._P_descr
    @descr.setter
    def descr(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property descr input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: provider, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_descr=value
    @descr.deleter
    def descr(self):
        del self._P_descr


    @property
    def acl(self):
        return self._P_acl
    @acl.setter
    def acl(self, value):
        
        if not isinstance(value, list) and value is not None:
            if isinstance(value, basestring) and j.basetype.list.checkString(value):
                value = j.basetype.list.fromString(value)
            else:
                msg="property acl input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: provider, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_acl=value
    @acl.deleter
    def acl(self):
        del self._P_acl


    @property
    def id(self):
        return self._P_id
    @id.setter
    def id(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property id input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: provider, value was:" + str(value)
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
                msg="property guid input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: provider, value was:" + str(value)
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
                msg="property _meta input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: provider, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P__meta=value
    @_meta.deleter
    def _meta(self):
        del self._P__meta


    def new_acl(self,value=None):

        if value==None:
            value2=j.core.codegenerator.getClassJSModel("osismodel","robot","ace")()
        else:
            value2=value
        
        self._P_acl.append(value2)
        if self._P_acl[-1].__dict__.has_key("_P_id"):
            self._P_acl[-1].id=len(self._P_acl)
        return self._P_acl[-1]
        
    
