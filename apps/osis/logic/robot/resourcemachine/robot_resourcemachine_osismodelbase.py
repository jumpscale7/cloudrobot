from JumpScale import j

class robot_resourcemachine_osismodelbase(j.code.classGetJSRootModelBase()):
    """
    can be virtual or physical
    
    """
    def __init__(self):
        self._P_name=""
    
        self._P_descr=""
    
        self._P_provider=""
    
        self._P_location=""
    
        self._P_acl=list()
    
        self._P_ipv4=""
    
        self._P_ipv6=""
    
        self._P_rootpasswd=""
    
        self._P_cpucores=0
    
        self._P_cpumhz=0
    
        self._P_ssd_size=0
    
        self._P_disk_size=0
    
        self._P_mem_size=0
    
        self._P_cost=0
    
        self._P_ssd_used=0
    
        self._P_disk_used=0
    
        self._P_mem_used=0
    
        self._P_cpu_used=list()
    
        self._P_cost_distr_ssd=0
    
        self._P_cost_distr_disk=0
    
        self._P_cost_distr_compute=0
    
        self._P_id=0
    
        self._P_guid=""
    
        self._P__meta=list()
    
        self._P__meta=["osismodel","robot","resourcemachine",1] #@todo version not implemented now, just already foreseen
    

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
                msg="property name input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: resourcemachine, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_name=value
    @name.deleter
    def name(self):
        del self._P_name


    @property
    def descr(self):
        return self._P_descr
    @descr.setter
    def descr(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property descr input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: resourcemachine, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_descr=value
    @descr.deleter
    def descr(self):
        del self._P_descr


    @property
    def provider(self):
        return self._P_provider
    @provider.setter
    def provider(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property provider input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: resourcemachine, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_provider=value
    @provider.deleter
    def provider(self):
        del self._P_provider


    @property
    def location(self):
        return self._P_location
    @location.setter
    def location(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property location input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: resourcemachine, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_location=value
    @location.deleter
    def location(self):
        del self._P_location


    @property
    def acl(self):
        return self._P_acl
    @acl.setter
    def acl(self, value):
        
        if not isinstance(value, list) and value is not None:
            if isinstance(value, basestring) and j.basetype.list.checkString(value):
                value = j.basetype.list.fromString(value)
            else:
                msg="property acl input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: resourcemachine, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_acl=value
    @acl.deleter
    def acl(self):
        del self._P_acl


    @property
    def ipv4(self):
        return self._P_ipv4
    @ipv4.setter
    def ipv4(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property ipv4 input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: resourcemachine, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_ipv4=value
    @ipv4.deleter
    def ipv4(self):
        del self._P_ipv4


    @property
    def ipv6(self):
        return self._P_ipv6
    @ipv6.setter
    def ipv6(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property ipv6 input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: resourcemachine, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_ipv6=value
    @ipv6.deleter
    def ipv6(self):
        del self._P_ipv6


    @property
    def rootpasswd(self):
        return self._P_rootpasswd
    @rootpasswd.setter
    def rootpasswd(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property rootpasswd input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: resourcemachine, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_rootpasswd=value
    @rootpasswd.deleter
    def rootpasswd(self):
        del self._P_rootpasswd


    @property
    def cpucores(self):
        return self._P_cpucores
    @cpucores.setter
    def cpucores(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property cpucores input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: resourcemachine, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_cpucores=value
    @cpucores.deleter
    def cpucores(self):
        del self._P_cpucores


    @property
    def cpumhz(self):
        return self._P_cpumhz
    @cpumhz.setter
    def cpumhz(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property cpumhz input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: resourcemachine, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_cpumhz=value
    @cpumhz.deleter
    def cpumhz(self):
        del self._P_cpumhz


    @property
    def ssd_size(self):
        return self._P_ssd_size
    @ssd_size.setter
    def ssd_size(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property ssd_size input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: resourcemachine, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_ssd_size=value
    @ssd_size.deleter
    def ssd_size(self):
        del self._P_ssd_size


    @property
    def disk_size(self):
        return self._P_disk_size
    @disk_size.setter
    def disk_size(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property disk_size input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: resourcemachine, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_disk_size=value
    @disk_size.deleter
    def disk_size(self):
        del self._P_disk_size


    @property
    def mem_size(self):
        return self._P_mem_size
    @mem_size.setter
    def mem_size(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property mem_size input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: resourcemachine, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_mem_size=value
    @mem_size.deleter
    def mem_size(self):
        del self._P_mem_size


    @property
    def cost(self):
        return self._P_cost
    @cost.setter
    def cost(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property cost input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: resourcemachine, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_cost=value
    @cost.deleter
    def cost(self):
        del self._P_cost


    @property
    def ssd_used(self):
        return self._P_ssd_used
    @ssd_used.setter
    def ssd_used(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property ssd_used input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: resourcemachine, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_ssd_used=value
    @ssd_used.deleter
    def ssd_used(self):
        del self._P_ssd_used


    @property
    def disk_used(self):
        return self._P_disk_used
    @disk_used.setter
    def disk_used(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property disk_used input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: resourcemachine, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_disk_used=value
    @disk_used.deleter
    def disk_used(self):
        del self._P_disk_used


    @property
    def mem_used(self):
        return self._P_mem_used
    @mem_used.setter
    def mem_used(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property mem_used input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: resourcemachine, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_mem_used=value
    @mem_used.deleter
    def mem_used(self):
        del self._P_mem_used


    @property
    def cpu_used(self):
        return self._P_cpu_used
    @cpu_used.setter
    def cpu_used(self, value):
        
        if not isinstance(value, list) and value is not None:
            if isinstance(value, basestring) and j.basetype.list.checkString(value):
                value = j.basetype.list.fromString(value)
            else:
                msg="property cpu_used input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: resourcemachine, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_cpu_used=value
    @cpu_used.deleter
    def cpu_used(self):
        del self._P_cpu_used


    @property
    def cost_distr_ssd(self):
        return self._P_cost_distr_ssd
    @cost_distr_ssd.setter
    def cost_distr_ssd(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property cost_distr_ssd input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: resourcemachine, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_cost_distr_ssd=value
    @cost_distr_ssd.deleter
    def cost_distr_ssd(self):
        del self._P_cost_distr_ssd


    @property
    def cost_distr_disk(self):
        return self._P_cost_distr_disk
    @cost_distr_disk.setter
    def cost_distr_disk(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property cost_distr_disk input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: resourcemachine, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_cost_distr_disk=value
    @cost_distr_disk.deleter
    def cost_distr_disk(self):
        del self._P_cost_distr_disk


    @property
    def cost_distr_compute(self):
        return self._P_cost_distr_compute
    @cost_distr_compute.setter
    def cost_distr_compute(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property cost_distr_compute input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: resourcemachine, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_cost_distr_compute=value
    @cost_distr_compute.deleter
    def cost_distr_compute(self):
        del self._P_cost_distr_compute


    @property
    def id(self):
        return self._P_id
    @id.setter
    def id(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property id input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: resourcemachine, value was:" + str(value)
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
                msg="property guid input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: resourcemachine, value was:" + str(value)
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
                msg="property _meta input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/robot/model.spec, name model: resourcemachine, value was:" + str(value)
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
        
    
