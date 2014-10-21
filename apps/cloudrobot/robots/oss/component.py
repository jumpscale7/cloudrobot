
from JumpScale import j
import yaml
import JumpScale.grid.osis
import JumpScale.lib.cloudrobots

OSISObjManipulatorClass=j.cloudrobot.getOSISObjManipulatorClass()

def Cmds(OSISObjManipulatorClass):
    
    def __init__(self):    
        self.osisclient = j.core.osis.getClientForNamespace('oss')    
        self.model=self.osisclient.component
        self.spec="""
model:
- {default: '', descr: '', isdict: false, islist: false, name: type, optional: false,
  tags: '', type: str}
- {default: '', descr: amount of component e.g. 2 CPU, isdict: false, islist: false,
  name: nr, optional: false, tags: amount of component e.g. 2 CPU, type: int}
- {default: '', descr: '', isdict: false, islist: false, name: brand, optional: false,
  tags: '', type: str}
- {default: '', descr: '', isdict: false, islist: false, name: model, optional: false,
  tags: '', type: str}
- {default: '', descr: '', isdict: false, islist: false, name: description, optional: false,
  tags: '', type: str}
- {default: '', descr: '', isdict: false, islist: false, name: supportremarks, optional: false,
  tags: '', type: str}
- {default: '', descr: reference to comments, isdict: false, islist: true, name: comments,
  optional: false, tags: reference to comments, type: str}
- {default: '', descr: Auto generated id @optional, isdict: false, islist: false,
  name: id, optional: false, tags: Auto generated id @optional, type: int}
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
                      

        