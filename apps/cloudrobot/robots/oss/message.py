
from JumpScale import j
import yaml
import JumpScale.grid.osis
import JumpScale.lib.cloudrobots

OSISObjManipulatorClass=j.cloudrobot.getOSISObjManipulatorClass()

def Cmds(OSISObjManipulatorClass):
    
    def __init__(self):    
        self.osisclient = j.core.osis.getClientForNamespace('oss')    
        self.model=self.osisclient.message
        self.spec="""
model:
- {default: '', descr: '', isdict: false, islist: false, name: subject, optional: false,
  tags: '', type: str}
- {default: '', descr: '', isdict: false, islist: false, name: message, optional: false,
  tags: '', type: str}
- {default: '', descr: '', isdict: false, islist: true, name: destination, optional: false,
  tags: '', type: str}
- {default: '', descr: epoch, isdict: false, islist: false, name: time, optional: false,
  tags: epoch, type: int}
- {default: '', descr: 'types are: email;sms;gtalk;tel', isdict: false, islist: false,
  name: type, optional: false, tags: 'types are: email;sms;gtalk;tel', type: str}
- {default: '', descr: ' html;confl;md;text default is text', isdict: false, islist: false,
  name: format, optional: false, tags: ' html;confl;md;text default is text', type: str}
- {default: '', descr: '', isdict: false, islist: false, name: ticket, optional: false,
  tags: '', type: int}
- {default: '', descr: reference to comments, isdict: false, islist: true, name: comments,
  optional: false, tags: reference to comments, type: str}
- {default: '', descr: Auto generated id @optional, isdict: false, islist: false,
  name: id, optional: false, tags: Auto generated id @optional, type: int}
propname_longest: 11
        
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
                      

        