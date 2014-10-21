
from JumpScale import j
import yaml
import JumpScale.grid.osis
import JumpScale.lib.cloudrobots

OSISObjManipulatorClass=j.cloudrobot.getOSISObjManipulatorClass()

def Cmds(OSISObjManipulatorClass):
    
    def __init__(self):    
        self.osisclient = j.core.osis.getClientForNamespace('oss')    
        self.model=self.osisclient.service
        self.spec="""
model:
- {default: '', descr: '', isdict: false, islist: false, name: id, optional: false,
  tags: '', type: int}
- {default: '', descr: '', isdict: false, islist: false, name: name, optional: false,
  tags: '', type: str}
- {default: '', descr: id of organization which owns the service if any, isdict: false,
  islist: false, name: organization, optional: false, tags: id of organization which
    owns the service if any, type: str}
- {default: '', descr: '', isdict: false, islist: false, name: organization_name,
  optional: false, tags: '', type: str}
- {default: '', descr: '', isdict: false, islist: false, name: label, optional: false,
  tags: '', type: str}
- {default: '', descr: '', isdict: false, islist: false, name: parent, optional: false,
  tags: '', type: int}
- {default: '', descr: '', isdict: false, islist: false, name: parent_name, optional: false,
  tags: '', type: str}
- {default: '', descr: '', isdict: false, islist: false, name: description, optional: false,
  tags: '', type: str}
- {default: '', descr: '', isdict: false, islist: false, name: type, optional: false,
  tags: '', type: str}
- {default: '', descr: '', isdict: false, islist: true, name: serviceports, optional: false,
  tags: '', type: str}
- {default: '', descr: ' link to other services (what does it need to work)', isdict: false,
  islist: true, name: depends, optional: false, tags: ' link to other services (what
    does it need to work)', type: str}
- {default: '', descr: '', isdict: false, islist: true, name: depends_names, optional: false,
  tags: '', type: str}
- {default: '', descr: who is machine hosting this service, isdict: false, islist: false,
  name: machinehost, optional: false, tags: who is machine hosting this service, type: int}
- {default: '', descr: in GB, isdict: false, islist: false, name: memory, optional: false,
  tags: in GB, type: int}
- {default: '', descr: in GB, isdict: false, islist: false, name: ssdcapacity, optional: false,
  tags: in GB, type: int}
- {default: '', descr: in GB, isdict: false, islist: false, name: hdcapacity, optional: false,
  tags: in GB, type: int}
- {default: '', descr: in mhz, isdict: false, islist: false, name: cpumhz, optional: false,
  tags: in mhz, type: int}
- {default: '', descr: '', isdict: false, islist: false, name: nrcores, optional: false,
  tags: '', type: int}
- {default: '', descr: '', isdict: false, islist: false, name: nrcpu, optional: false,
  tags: '', type: int}
- {default: '', descr: name of admin e.g. admin or root, isdict: false, islist: false,
  name: admin_name, optional: false, tags: name of admin e.g. admin or root, type: str}
- {default: '', descr: encrypted root passwd, isdict: false, islist: false, name: admin_passwd,
  optional: false, tags: encrypted root passwd, type: str}
- {default: '', descr: dict where key is name of group; value is R/W/E (E=Execute),
  isdict: true, islist: false, name: acl, optional: false, tags: dict where key is
    name of group; value is R/W/E (E=Execute), type: str}
- {default: '', descr: reference to comments, isdict: false, islist: true, name: comments,
  optional: false, tags: reference to comments, type: str}
propname_longest: 17
        
""" 
        self.spec=yaml.load(self.spec)       

    def trigger_set(self,obj,args):        
        """
        overrule this method to do some business logic when setting or after setting
        """
        self.model.set(obj)

    def trigger_delete(self,obj):
        """
        overrule this method to list other properties (this is called per item in the list, when return None then will not be shown)
        return what needs to be returned to user who called robot (per line)
        """
        self.model.delete(obj.guid)

    def trigger_list(self,obj):
        """
        overrule this method to list other properties (this is called per item in the list, when return None then will not be shown)
        return what needs to be returned to user who called robot (per line)
        """
        out="%-7s %-15s %-10s %s"%(obj.id,obj.name,obj.description,obj.type)
        return out
                      

        