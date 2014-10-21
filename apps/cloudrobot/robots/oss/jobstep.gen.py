
from JumpScale import j
import yaml
import JumpScale.grid.osis
import JumpScale.lib.cloudrobots

OSISObjManipulatorClass=j.cloudrobot.getOSISObjManipulatorClass()

def Cmds(OSISObjManipulatorClass):
    
    def __init__(self):    
        self.osisclient = j.core.osis.getClientForNamespace('oss')    
        self.model=self.osisclient.jobstep
        self.spec="""
model:
- {default: '', descr: reference to job, isdict: false, islist: false, name: jobguid,
  optional: false, tags: reference to job, type: str}
- {default: '', descr: '', isdict: false, islist: false, name: workflow, optional: false,
  tags: '', type: str}
- {default: '', descr: reference to workflowstep which started this jobsteps, isdict: false,
  islist: false, name: workflowstep, optional: false, tags: reference to workflowstep
    which started this jobsteps, type: str}
- {default: '', descr: '', isdict: false, islist: false, name: workflowstep_name,
  optional: false, tags: '', type: str}
- {default: '', descr: '', isdict: false, islist: false, name: description, optional: false,
  tags: '', type: str}
- {default: '', descr: order in which the steps where executed, isdict: false, islist: false,
  name: order, optional: false, tags: order in which the steps where executed, type: int}
- {default: '', descr: json representation of dict which has all arguments, isdict: false,
  islist: false, name: params, optional: false, tags: json representation of dict
    which has all arguments, type: str}
- {default: '', descr: ' time that this step can take till warning (in sec)', isdict: false,
  islist: false, name: warningtime, optional: false, tags: ' time that this step can
    take till warning (in sec)', type: int}
- {default: '', descr: ' time that this step can take', isdict: false, islist: false,
  name: criticaltime, optional: false, tags: ' time that this step can take', type: int}
- {default: '', descr: '', isdict: false, islist: false, name: startdate, optional: false,
  tags: '', type: int}
- {default: '', descr: '', isdict: false, islist: false, name: enddate, optional: false,
  tags: '', type: int}
- {default: '', descr: script which was executed, isdict: false, islist: false, name: jscript,
  optional: false, tags: script which was executed, type: str}
- {default: '', descr: 'values are:', isdict: false, islist: false, name: status,
  optional: false, tags: 'values are:', type: str}
- {default: '', descr: 'after resolving the script next steps which were triggered
    (so is after execution), is references to other jobsteps (guid)', isdict: false,
  islist: true, name: nextsteps, optional: false, tags: 'after resolving the script
    next steps which were triggered (so is after execution), is references to other
    jobsteps (guid)', type: str}
- {default: '', descr: '', isdict: false, islist: false, name: logs, optional: false,
  tags: '', type: str}
- {default: '', descr: Auto generated id @optional, isdict: false, islist: false,
  name: id, optional: false, tags: Auto generated id @optional, type: int}
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
                      

        