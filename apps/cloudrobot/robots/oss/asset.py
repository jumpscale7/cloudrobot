
from JumpScale import j
import yaml
import JumpScale.grid.osis
import JumpScale.lib.cloudrobots

OSISObjManipulatorClass=j.cloudrobot.getOSISObjManipulatorClass()

def Cmds(OSISObjManipulatorClass):
    
    def __init__(self):    
        self.osisclient = j.core.osis.getClientForNamespace('oss')    
        self.model=self.osisclient.asset
        self.spec="""
model:
- {default: '', descr: '', isdict: false, islist: false, name: id, optional: false,
  tags: '', type: int}
- {default: '', descr: id of organization which owns the asset if any, isdict: false,
  islist: false, name: organization, optional: false, tags: id of organization which
    owns the asset if any, type: str}
- {default: '', descr: comma separated list of name, isdict: false, islist: false,
  name: organization_names, optional: false, tags: comma separated list of name, type: str}
- {default: '', descr: '', isdict: false, islist: false, name: label, optional: false,
  tags: '', type: str}
- {default: '', descr: '', isdict: false, islist: false, name: parent, optional: false,
  tags: '', type: str}
- {default: '', descr: '', isdict: false, islist: false, name: parent_name, optional: false,
  tags: '', type: str}
- {default: '', descr: '', isdict: false, islist: false, name: description, optional: false,
  tags: '', type: str}
- {default: '', descr: '', isdict: false, islist: false, name: type, optional: false,
  tags: '', type: str}
- {default: '', descr: '', isdict: false, islist: false, name: brand, optional: false,
  tags: '', type: str}
- {default: '', descr: '', isdict: false, islist: false, name: model, optional: false,
  tags: '', type: str}
- {default: '', descr: '', isdict: false, islist: true, name: interfaces, optional: false,
  tags: '', type: str}
- {default: '', descr: '', isdict: false, islist: true, name: components, optional: false,
  tags: '', type: str}
- {default: '', descr: ' link to other assets (what does it need to work)', isdict: false,
  islist: true, name: depends, optional: false, tags: ' link to other assets (what
    does it need to work)', type: str}
- {default: '', descr: '', isdict: false, islist: true, name: depends_names, optional: false,
  tags: '', type: str}
- {default: '', descr: '', isdict: false, islist: false, name: rack, optional: false,
  tags: '', type: str}
- {default: '', descr: '', isdict: false, islist: false, name: datacenter_name, optional: false,
  tags: '', type: str}
- {default: '', descr: '', isdict: false, islist: false, name: pod_name, optional: false,
  tags: '', type: str}
- {default: '', descr: '', isdict: false, islist: false, name: rack_name, optional: false,
  tags: '', type: str}
- {default: '', descr: '', isdict: false, islist: false, name: datacenter_label, optional: false,
  tags: '', type: str}
- {default: '', descr: '', isdict: false, islist: false, name: pod_label, optional: false,
  tags: '', type: str}
- {default: '', descr: '', isdict: false, islist: false, name: rack_label, optional: false,
  tags: '', type: str}
- {default: '', descr: how many U taken, isdict: false, islist: false, name: u, optional: false,
  tags: how many U taken, type: int}
- {default: '', descr: ' how many U starting from bottomn', isdict: false, islist: false,
  name: rackpos, optional: false, tags: ' how many U starting from bottomn', type: int}
- {default: '', descr: dict where key is name of group; value is R/W/E (E=Execute),
  isdict: true, islist: false, name: acl, optional: false, tags: dict where key is
    name of group; value is R/W/E (E=Execute), type: str}
- {default: '', descr: reference to comments, isdict: false, islist: true, name: comments,
  optional: false, tags: reference to comments, type: str}
propname_longest: 18
        
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
                      

        