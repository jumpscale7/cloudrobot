
from JumpScale import j
import yaml
import JumpScale.grid.osis
import JumpScale.lib.cloudrobots

OSISObjManipulatorClass=j.cloudrobot.getOSISObjManipulatorClass()

def Cmds(OSISObjManipulatorClass):
    
    def __init__(self):    
        self.osisclient = j.core.osis.getClientForNamespace('oss')    
        self.model=self.osisclient.pod
        self.spec="""
model:
- {default: '', descr: '', isdict: false, islist: false, name: id, optional: false,
  tags: '', type: int}
- {default: '', descr: '', isdict: false, islist: false, name: name, optional: false,
  tags: '', type: str}
- {default: '', descr: '', isdict: false, islist: false, name: label, optional: false,
  tags: '', type: str}
- {default: '', descr: id of organization which owns the pod if any, isdict: false,
  islist: false, name: organization, optional: false, tags: id of organization which
    owns the pod if any, type: str}
- {default: '', descr: '', isdict: false, islist: false, name: organization_name,
  optional: false, tags: '', type: str}
- {default: '', descr: '', isdict: false, islist: false, name: datacenter, optional: false,
  tags: '', type: str}
- {default: '', descr: '', isdict: false, islist: false, name: datacenter_name, optional: false,
  tags: '', type: str}
- {default: '', descr: '', isdict: false, islist: false, name: description, optional: false,
  tags: '', type: str}
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
                      

        