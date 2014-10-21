
from JumpScale import j
import yaml
import JumpScale.grid.osis
import JumpScale.lib.cloudrobots

OSISObjManipulatorClass=j.cloudrobot.getOSISObjManipulatorClass()

def Cmds(OSISObjManipulatorClass):
    
    def __init__(self):    
        self.osisclient = j.core.osis.getClientForNamespace('oss')    
        self.model=self.osisclient.ticket
        self.spec="""
model:
- {default: '', descr: '', isdict: false, islist: false, name: id, optional: false,
  tags: '', type: int}
- {default: '', descr: '', isdict: false, islist: false, name: name, optional: false,
  tags: '', type: str}
- {default: '', descr: '', isdict: false, islist: false, name: description, optional: false,
  tags: '', type: str}
- {default: '', descr: level 0-4 (4 is most urgent), isdict: false, islist: false,
  name: priority, optional: false, tags: level 0-4 (4 is most urgent), type: int}
- {default: '', descr: link to project, isdict: false, islist: false, name: project,
  optional: false, tags: link to project, type: str}
- {default: '', descr: '', isdict: false, islist: false, name: project_name, optional: false,
  tags: '', type: str}
- {default: '', descr: '', isdict: false, islist: false, name: type, optional: false,
  tags: '', type: str}
- {default: '', descr: '', isdict: false, islist: false, name: parent, optional: false,
  tags: '', type: str}
- {default: '', descr: '', isdict: false, islist: false, name: parent_name, optional: false,
  tags: '', type: str}
- {default: '', descr: this task depends on, isdict: false, islist: true, name: depends,
  optional: false, tags: this task depends on, type: str}
- {default: '', descr: '', isdict: false, islist: true, name: depends_names, optional: false,
  tags: '', type: str}
- {default: '', descr: epoch of when task needs to be done, isdict: false, islist: false,
  name: deadline, optional: false, tags: epoch of when task needs to be done, type: int}
- {default: '', descr: list of duplicates to this issue, isdict: false, islist: true,
  name: duplicate, optional: false, tags: list of duplicates to this issue, type: str}
- {default: '', descr: '', isdict: false, islist: true, name: duplicate_names, optional: false,
  tags: '', type: str}
- {default: '', descr: owner of task (user), isdict: false, islist: false, name: taskowner,
  optional: false, tags: owner of task (user), type: str}
- {default: '', descr: owner of task (user), isdict: false, islist: false, name: taskowner_name,
  optional: false, tags: owner of task (user), type: str}
- {default: '', descr: owner of task (user), isdict: false, islist: false, name: source,
  optional: false, tags: owner of task (user), type: str}
- {default: '', descr: 'name of user where request came from (can be email, username,
    ...)', isdict: false, islist: false, name: source_name, optional: false, tags: 'name
    of user where request came from (can be email, username, ...)', type: str}
- {default: '', descr: '', isdict: false, islist: false, name: sprint, optional: false,
  tags: '', type: str}
- {default: '', descr: '', isdict: false, islist: false, name: sprint_name, optional: false,
  tags: '', type: str}
- {default: '', descr: ' link to organization if any', isdict: false, islist: false,
  name: organization, optional: false, tags: ' link to organization if any', type: str}
- {default: '', descr: '', isdict: false, islist: false, name: organization_name,
  optional: false, tags: '', type: str}
- {default: '', descr: date for next day to continue with this ticket, isdict: false,
  islist: false, name: nextstepdate, optional: false, tags: date for next day to continue
    with this ticket, type: int}
- {default: '', descr: current active workflow, isdict: false, islist: false, name: workflow,
  optional: false, tags: current active workflow, type: str}
- {default: '', descr: 'values are:', isdict: false, islist: false, name: job_status,
  optional: false, tags: 'values are:', type: str}
- {default: '', descr: link to workflows, isdict: false, islist: true, name: jobs,
  optional: false, tags: link to workflows, type: str}
- {default: '', descr: '', isdict: false, islist: false, name: time_created, optional: false,
  tags: '', type: int}
- {default: '', descr: '', isdict: false, islist: false, name: time_lastmessage, optional: false,
  tags: '', type: int}
- {default: '', descr: '', isdict: false, islist: false, name: time_lastresponse,
  optional: false, tags: '', type: int}
- {default: '', descr: '', isdict: false, islist: false, name: time_closed, optional: false,
  tags: '', type: int}
- {default: '', descr: ' reference to message', isdict: false, islist: true, name: messages,
  optional: false, tags: ' reference to message', type: str}
- {default: '', descr: reference to comments, isdict: false, islist: true, name: comments,
  optional: false, tags: reference to comments, type: str}
- {default: '', descr: source(s) where data comes from (reference), isdict: false,
  islist: true, name: datasources, optional: false, tags: source(s) where data comes
    from (reference), type: str}
- {default: '', descr: dict where key is name of group; value is R/W/E (E=Execute),
  isdict: true, islist: false, name: acl, optional: false, tags: dict where key is
    name of group; value is R/W/E (E=Execute), type: str}
- {default: '', descr: json representation of dict which has all arguments required
    for this ticket, isdict: false, islist: false, name: params, optional: false,
  tags: json representation of dict which has all arguments required for this ticket,
  type: str}
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
                      

        