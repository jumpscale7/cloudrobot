
from JumpScale import j
import yaml
import JumpScale.grid.osis
import JumpScale.lib.cloudrobots

OSISObjManipulatorClass=j.cloudrobot.getOSISObjManipulatorClass()

def Cmds(OSISObjManipulatorClass):
    
    def __init__(self):    
        self.osisclient = j.core.osis.getClientForNamespace('oss')    
        self.model=self.osisclient.organization
        self.spec="""
model:
- {default: '', descr: domain, isdict: false, islist: false, name: name, optional: false,
  tags: domain, type: str}
- {default: '', descr: '', isdict: false, islist: false, name: id, optional: false,
  tags: '', type: int}
- {default: '', descr: '', isdict: false, islist: false, name: description, optional: false,
  tags: '', type: str}
- {default: '', descr: optional name, isdict: false, islist: false, name: companyname,
  optional: true, tags: optional name, type: str}
- {default: '', descr: organization can belong to other organization, isdict: false,
  islist: false, name: parent, optional: false, tags: organization can belong to other
    organization, type: str}
- {default: '', descr: '', isdict: false, islist: false, name: parent_name, optional: false,
  tags: '', type: str}
- {default: '', descr: reference to addresses (guid), isdict: false, islist: true,
  name: addresses, optional: false, tags: reference to addresses (guid), type: str}
- {default: '', descr: reference to contactmethod (guid), isdict: false, islist: true,
  name: contactmethods, optional: false, tags: reference to contactmethod (guid),
  type: str}
- {default: '', descr: '', isdict: false, islist: false, name: vatnr, optional: false,
  tags: '', type: str}
- {default: '', descr: source(s) where data comes from (reference), isdict: false,
  islist: true, name: datasources, optional: false, tags: source(s) where data comes
    from (reference), type: str}
- {default: '', descr: dict where key is name of group; value is R/W/E (E=Execute),
  isdict: true, islist: false, name: acl, optional: false, tags: dict where key is
    name of group; value is R/W/E (E=Execute), type: str}
- {default: '', descr: reference to comments, isdict: false, islist: true, name: comments,
  optional: false, tags: reference to comments, type: str}
propname_longest: 14
        
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
                      

        