
from JumpScale import j
import yaml
import JumpScale.grid.osis
import JumpScale.lib.cloudrobots

OSISObjManipulatorClass=j.cloudrobot.getOSISObjManipulatorClass()

def Cmds(OSISObjManipulatorClass):
    
    def __init__(self):    
        self.osisclient = j.core.osis.getClientForNamespace('oss')    
        self.model=self.osisclient.useridentification
        self.spec="""
model:
- {default: '', descr: ' reference to user', isdict: false, islist: false, name: userid,
  optional: false, tags: ' reference to user', type: int}
- {default: '', descr: ' PASSPORT:ID:DRIVINGLICENSE', isdict: false, islist: false,
  name: type, optional: false, tags: ' PASSPORT:ID:DRIVINGLICENSE', type: str}
- {default: '', descr: e.g. passport nr, isdict: false, islist: false, name: identificationnr,
  optional: false, tags: e.g. passport nr, type: str}
- {default: '', descr: ' epoch', isdict: false, islist: false, name: registrationdate,
  optional: false, tags: ' epoch', type: int}
- {default: '', descr: ' epoch', isdict: false, islist: false, name: expirationdate,
  optional: false, tags: ' epoch', type: int}
- {default: '', descr: '', isdict: false, islist: false, name: description, optional: false,
  tags: '', type: str}
- {default: '', descr: 'VALID:EXPIRED:ERROR', isdict: false, islist: false, name: status,
  optional: false, tags: 'VALID:EXPIRED:ERROR', type: str}
- {default: '', descr: Auto generated id @optional, isdict: false, islist: false,
  name: id, optional: false, tags: Auto generated id @optional, type: int}
propname_longest: 16
        
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
                      

        