from JumpScale import j
import JumpScale.lib.txtrobot
import JumpScale.grid.osis
import ujson as json


initcmds="""



##############################################################################
organization
- create (c,n,new,update,u)
-- id
-- name
-- description
-- companyname
-- parent #specify part of name or id of organization
-- vatnr
-- acl                  #as tags 'admin:RW guest:R'

- address
-- orgid #id of org 
-- orgname #name or part of name of org (if id not used)
-- country
-- city
-- citycode
-- zone
-- region
-- street
-- nr
-- floor

- datasource
-- id
-- name #name or part of name of org (if id not used)
-- datasourcename

- contactmethod
-- orgid #id of org
-- name #name or part of name of org (if id not used)
-- type #phone;mobile;email;skype
-- value

- export 
-- filter (f) #is filter which is query str for osis

- list (l)
-- max #max amount of items
-- start #startpoint e.g. 10 is id
-- filter (f) #is filter which is query str for osis
-- verbose (v) #1-3 3 being most verbose

- delete (d,del)
-- id

- comment
-- id #id of org 
-- name #name or part of name of org (if id not used)
-- comment
-- created
-- author

##############################################################################
user
- create (c,n,new,update,u)
-- id
-- name
-- organization
-- acl                  #as tags 'admin:RW guest:R'

- address
-- userid #id of user 
-- username #name or part of name of user (if userid not used)
-- country
-- city
-- citycode
-- zone
-- region
-- street
-- nr
-- floor

- datasource
-- id
-- name
-- datasourcename

- contactmethod
-- userid #id of user
-- name #name or part of name of user (if id not used)
-- type #phone;mobile;email;skype
-- value

- export 
-- filter (f) #is filter which is query str for osis

- list (l)
-- max #max amount of items
-- start #startpoint e.g. 10 is id
-- filter (f) #is filter which is query str for osis
-- verbose (v) #1-3 3 being most verbose

- delete (d,del)
-- id

- comment
-- id #id of user 
-- name #name or part of name of user (if id not used)
-- comment
-- created
-- author


##############################################################################
group
- create (c,n,new,update,u)
-- id
-- name
-- datasources #comma separated list of datasources
-- acl                  #as tags 'admin:RW guest:R'

- member
-- groupid
-- group #name of group (if groupid not used)
-- user #id or part of name

- contactmethod
-- id #id of group
-- name #name or part of name of group (if id not used)
-- type #phone;mobile;email;skype
-- value

- datasource
-- id
-- name
-- datasourcename

- export 
-- filter (f) #is filter which is query str for osis

- list (l)
-- max #max amount of items
-- start #startpoint e.g. 10 is id
-- filter (f) #is filter which is query str for osis
-- verbose (v) #1-3 3 being most verbose

- delete (d,del)
-- id

- comment
-- id #id of group 
-- name #name or part of name of group (if id not used)
-- comment
-- created
-- author


##############################################################################
project
- create (c,n,new,update,u)
-- id
-- name
-- description
-- deadline #as epoch or as future notation  e.g. +4d
-- acl                  #as tags 'admin:RW guest:R'

- export 
-- filter (f) #is filter which is query str for osis

- list (l)
-- max #max amount of items
-- start #startpoint e.g. 10 is id
-- filter (f) #is filter which is query str for osis
-- verbose (v) #1-3 3 being most verbose

- delete (d,del)
-- id

- organization
-- id
-- name
-- organization

- datasource
-- id
-- name
-- datasourcename

- comment
-- id #id of group 
-- name #name or part of name of group (if id not used)
-- comment
-- created
-- author


##############################################################################
sprint
- create (c,n,new,update,u)
-- name
-- description
-- organizations #comma separated list of orgs (as id, name part of name)
-- start #as epoch or as future notation  e.g. +4d
-- stop #as epoch or as future notation  e.g. +4d
-- id
-- datasources #comma separated list of datasources
-- acl                  #as tags 'admin:RW guest:R'

- export 
-- filter (f) #is filter which is query str for osis

- list (l)
-- max #max amount of items
-- start #startpoint e.g. 10 is id
-- filter (f) #is filter which is query str for osis
-- verbose (v) #1-3 3 being most verbose

- delete (d,del)
-- id

- comment
-- id #id of group 
-- name #name or part of name of group (if id not used)
-- comment
-- created
-- author

##############################################################################
datacenter
- create (c,n,new,update,u)
-- id
-- name
-- label
-- description
-- organization #id of org which owns the dc
-- datasources #comma separated list of datasources
-- acl                  #as tags 'admin:RW guest:R'

- address
-- id #id of datacenter 
-- name #name or part of name of datacenter (if id not used)
-- country
-- city
-- citycode
-- street
-- nr

- export 
-- filter (f) #is filter which is query str for osis

- list (l)
-- max #max amount of items
-- start #startpoint e.g. 10 is id
-- filter (f) #is filter which is query str for osis
-- verbose (v) #1-3 3 being most verbose

- delete (d,del)
-- id

- comment
-- id #id of group 
-- name #name or part of name of group (if id not used)
-- comment
-- created
-- author

##############################################################################
pod
- create (c,n,new,update,u)
-- id
-- name
-- label
-- description
-- organizations #comma separated list of orgs (as id, name part of name)
-- datacenters #comma separated list of datacenters (as id, name part of name)
-- datasources #comma separated list of datasources
-- acl                  #as tags 'admin:RW guest:R'

- export 
-- filter (f) #is filter which is query str for osis

- list (l)
-- max #max amount of items
-- start #startpoint e.g. 10 is id
-- filter (f) #is filter which is query str for osis
-- verbose (v) #1-3 3 being most verbose

- delete (d,del)
-- id

- comment
-- id #id of group 
-- name #name or part of name of group (if id not used)
-- comment
-- created
-- author

##############################################################################
rack
- create (c,n,new,update,u)
-- id
-- name
-- label
-- description
-- organization #comma separated list of orgs (as id, name part of name)
-- datacenter #comma separated list of datacenters (as id, name part of name, part of label)
-- pod #comma separated list of pods (as id, name part of name, part of label)
-- datasources #comma separated list of datasources
-- acl                  #as tags 'admin:RW guest:R'

- export 
-- filter (f) #is filter which is query str for osis

- list (l)
-- max #max amount of items
-- start #startpoint e.g. 10 is id
-- filter (f) #is filter which is query str for osis
-- verbose (v) #1-3 3 being most verbose

- delete (d,del)
-- id

- comment
-- id #id of group 
-- name #name or part of name of group (if id not used)
-- comment
-- created
-- author

##############################################################################
asset
- create (c,n,new,update,u)
-- id
-- name
-- label
-- description
-- organization
-- rack #as id name or part of name or part of label
-- U    #height in U
-- pos (position,rackpos)  #position in rack in U from bottomn
-- brand
-- model
-- type
-- parent       #id,name or label (or part of) of parent asset
-- depends      #comma separated list of id's or names/labels of assets depend on 
-- datasources  #comma separated list of datasources
-- acl                  #as tags 'admin:RW guest:R'

- export 
-- filter (f) #is filter which is query str for osis

- list (l)
-- max #max amount of items
-- start #startpoint e.g. 10 is id
-- filter (f) #is filter which is query str for osis
-- verbose (v) #1-3 3 being most verbose

- delete (d,del)
-- id

- comment
-- id #id of group 
-- name #name or part of name of group (if id not used)
-- comment
-- created
-- author

##############################################################################
machine
- create (c,n,new,update,u)
-- id
-- name
-- label
-- description
-- memory
-- ssdcapacity
-- hdcapacity
-- cpumhz
-- nrcores
-- nrcpu
-- organization    #comma separated list of orgs (as id, name part of name)
-- interfaces       #comma separated list of interfaceids
-- assethost        #name, part of name, id, label, part of label of asset
-- parent           #name, part of name, id, label, part of label of machine
-- type
-- depends          #comma separed list of machines we depend on (name, part of name, id, label, part of label of machine)
-- acl              #as tags 'admin:RW guest:R'

- export 
-- filter (f) #is filter which is query str for osis

- list (l)
-- max #max amount of items
-- start #startpoint e.g. 10 is id
-- filter (f) #is filter which is query str for osis
-- verbose (v) #1-3 3 being most verbose

- delete (d,del)
-- id

- interface
-- id
-- name
-- interface

- datasource
-- id
-- name
-- datasourcename

- depend
-- id
-- name (n) #speciy name or part of name
-- on #depend on (speciy name or part of name or id)

- comment
-- id #id of group 
-- name #name or part of name of group (if id not used)
-- comment
-- created
-- author


##############################################################################
service
- create (c,n,new,update,u)
-- id
-- name
-- organization
-- label
-- description
-- type
-- machinehost
-- memory
-- ssdcapacity
-- hdcapacity
-- cpumhz
-- nrcores
-- nrcpu
-- admin_name
-- admin_passwd
-- acl              #as tags 'admin:RW guest:R'

- export 
-- filter (f) #is filter which is query str for osis

- list (l)
-- max #max amount of items
-- start #startpoint e.g. 10 is id
-- filter (f) #is filter which is query str for osis
-- verbose (v) #1-3 3 being most verbose

- delete (d,del)
-- id

- serviceport
-- id
-- name
-- serviceport

- depend
-- id
-- name (n) #speciy name or part of name
-- on #depend on (speciy name or part of name or id)

- comment
-- id #id of group 
-- name #name or part of name of group (if id not used)
-- comment
-- created
-- author

##############################################################################
document
- create (c,n,new,update,u)
-- id
-- name
-- description
-- creationdate
-- moddate
-- type
-- ext
-- contents
-- objstorid
-- parent
-- acl              #as tags 'admin:RW guest:R'

- export 
-- filter (f) #is filter which is query str for osis

- list (l)
-- max #max amount of items
-- start #startpoint e.g. 10 is id
-- filter (f) #is filter which is query str for osis
-- verbose (v) #1-3 3 being most verbose

- delete (d,del)
-- id

- comment
-- id #id of group 
-- name #name or part of name of group (if id not used)
-- comment
-- created
-- author

##############################################################################
workflow
- create (c,n,new,update,u)
-- id
-- name
-- description
-- tickettype
-- firststep
-- acl              #as tags 'admin:RW guest:R'

- export 
-- filter (f) #is filter which is query str for osis

- list (l)
-- max #max amount of items
-- start #startpoint e.g. 10 is id
-- filter (f) #is filter which is query str for osis
-- verbose (v) #1-3 3 being most verbose

- delete (d,del)
-- id

- comment
-- id #id of group 
-- name #name or part of name of group (if id not used)
-- comment
-- created
-- author

##############################################################################
workflowstep
- create (c,n,new,update,u)
-- id
-- name
-- description
-- warningtime
-- criticaltime
-- nextstep
-- nextsteps_error
-- jscript
-- acl              #as tags 'admin:RW guest:R'

- export 
-- filter (f) #is filter which is query str for osis

- list (l)
-- max #max amount of items
-- start #startpoint e.g. 10 is id
-- filter (f) #is filter which is query str for osis
-- verbose (v) #1-3 3 being most verbose

- delete (d,del)
-- id

- comment
-- id #id of group 
-- name #name or part of name of group (if id not used)
-- comment
-- created
-- author


##############################################################################
job
- create (c,n,new,update,u)
-- id
-- workflow
-- startdate
-- enddate
-- status

- export 
-- filter (f) #is filter which is query str for osis

- list (l)
-- max #max amount of items
-- start #startpoint e.g. 10 is id
-- filter (f) #is filter which is query str for osis
-- verbose (v) #1-3 3 being most verbose

- delete (d,del)
-- id


##############################################################################
jobstep
- create (c,n,new,update,u)
-- id
-- jobguid
-- workflowstep
-- description
-- order
-- params
-- warningtime
-- criticaltime
-- startdate
-- enddate
-- jscript
-- status
-- nextsteps
-- logs

- export 
-- filter (f) #is filter which is query str for osis

- list (l)
-- max #max amount of items
-- start #startpoint e.g. 10 is id
-- filter (f) #is filter which is query str for osis
-- verbose (v) #1-3 3 being most verbose

- delete (d,del)
-- id

- comment
-- id #id of group 
-- name #name or part of name of group (if id not used)
-- comment
-- created
-- author

##################################################################################
priorities:
  Show-stopper:4
  Critical:3
  Major:2
  Normal:1
  Minor:0

"""

class OSSRobot(object):

    def getRobot(self):
        robot=j.tools.txtrobot.get(initcmds)
        cmds=OSSRobotCmds()
        robot.addCmdClassObj(cmds)
        return robot

class OSSRobotCmds():
    def __init__(self):
        self.osscl = j.core.osis.getClientForNamespace('oss')

    def organization__create(self, **args):
        if args.get('id'):
            if not self.osscl.organization.exists(int(args.get('id'))):
                return 'Organization with ID %s was not found.' % args.get('id')
            organization = self.osscl.organization.get(int(args.get('id')))
        else:
            organization = self.osscl.organization.new()
        organization.name = args.get('name') if args.get('name') else organization.name
        organization.description = args.get('description') if args.get('description') else organization.description
        organization.companyname = args.get('companyname') if args.get('companyname') else organization.companyname
        parent = args.get('parent')
        nativequery={'$or':[{'guid':parent}, {'name':parent}]}
        parent = self.osscl.organization.simpleSearch({}, nativequery=nativequery)
        organization.parent = parent[0]['guid'] if parent else organization.parent
        organization.vatnr = args.get('vatnr') if args.get('vatnr') else organization.vatnr
        if args.get('acl'):
            tags = j.core.tags.getObject(args.get('acl'))
            organization.acl = tags.getDict() if tags.getDict() else organization.acl
        self.osscl.organization.set(organization)
        return 'Organization was created/updated successfully'

    def organization__address(self, **args):
        if args.get('orgid'):
            if not self.osscl.organization.exists(int(args.get('orgid'))):
                return 'Organization with ID %s was not found.' % args.get('orgid')
            organization = self.osscl.organization.get(int(args.get('orgid')))
        elif args.get('orgname'):
            organization = self.osscl.organization.simpleSearch({'name': args.get('orgname')})
            if organization:
                organization = self.osscl.organization.get(organization[0]['id'])
            else:
                return 'Organization with name %s can not be found' % args.get('orgname')
        else:
            return 'Organization ID or name must be passed'
        address = self.osscl.address.new()
        address.country = args.get('country') if args.get('country') else address.country
        address.city = args.get('city') if args.get('city') else address.city
        address.citycode = args.get('citycode') if args.get('citycode') else address.citycode
        address.zone = args.get('zone') if args.get('zone') else address.zone
        address.region = args.get('region') if args.get('region') else address.region
        address.street = args.get('street') if args.get('street') else address.street
        address.nr = args.get('nr') if args.get('nr') else address.nr
        guid,_, _ = self.osscl.address.set(address)
        organization.addresses.append(guid)
        self.osscl.organization.set(organization)
        return 'Organization address was added successfully'

    def organization__datasource(self, **args):
        if args.get('orgid'):
            if not self.osscl.organization.exists(int(args.get('orgid'))):
                return 'Organization with ID %s was not found.' % args.get('id')
            organization = self.osscl.organization.get(int(args.get('orgid')))
        elif args.get('orgname'):
            organization = self.osscl.organization.simpleSearch({'orgname': args.get('orgname')})
            if organization:
                organization = self.osscl.organization.get(organization[0]['id'])
            else:
                return 'Organization with name %s can not be found' % args.get('name')
        else:
            return 'Organization ID or name must be passed'
        datasource = organization.new_datasource()
        datasource.name = args.get('name') if args.get('name') else datasource.name
        self.osscl.organization.set(organization)
        return 'Organization datasource was added successfully'

    def organization__contactmethod(self, **args):
        if args.get('orgid'):
            if not self.osscl.organization.exists(int(args.get('orgid'))):
                return 'Organization with ID %s was not found.' % args.get('orgid')
            organization = self.osscl.organization.get(int(args.get('orgid')))
        elif args.get('name'):
            organization = self.osscl.organization.simpleSearch({'name': args.get('name')})
            if organization:
                organization = self.osscl.organization.get(organization[0]['id'])
            else:
                return 'Organization with name %s can not be found' % args.get('name')
        else:
            return 'Organization ID or name must be passed'
        contactmethod = organization.new_contactmethod()
        contactmethod.type = args.get('type') if args.get('type') else contactmethod.type
        contactmethod.value = args.get('value') if args.get('value') else contactmethod.value
        self.osscl.organization.set(organization)
        return 'Organization contactmethod was added successfully'

    def organization__list(self, **args):
        q = dict()
        if args.get('filter'):
            q = json.loads(args.get('filter'))
        start = int(args.get('start')) if args.get('start') else 0
        size = int(args.get('max')) if args.get('max') else None
        return self.osscl.organization.simpleSearch(q, start, size)

    def organization__delete(self, **args):
        self.osscl.organization.delete(int(args.get('id')))
        return 'Organization was deleted successfully'

    def organization__comment(self, **args):
        if args.get('id'):
            if not self.osscl.organization.exists(int(args.get('id'))):
                return 'Organization with ID %s was not found.' % args.get('id')
            organization = self.osscl.organization.get(int(args.get('id')))
        elif args.get('name'):
            organization = self.osscl.organization.simpleSearch({'name': args.get('name')})
            if organization:
                organization = self.osscl.organization.get(organization[0]['id'])
            else:
                return 'Organization with name %s can not be found' % args.get('name')
        else:
            return 'Organization ID or name must be passed'
        comment = organization.new_comment()
        comment.comment = args.get('comment') if args.get('comment') else comment.comment
        comment.time = args.get('created') if args.get('created') else comment.time
        author = args.get('author')
        nativequery={'$or':[{'guid':author}, {'name':author}]}
        author = self.osscl.user.simpleSearch({}, nativequery=nativequery)
        comment.author = author[0]['guid'] if author else comment.author
        self.osscl.organization.set(organization)
        return 'Organization comment was added successfully'

    def group__create(self, **args):
        if args.get('id'):
            if not self.osscl.group.exists(int(args.get('id'))):
                return 'Group with ID %s was not found.' % args.get('id')
            group = self.osscl.group.get(int(args.get('id')))
        else:
            group = self.osscl.group.new()
        group.name = args.get('name', group.name)
        group.members = args.get('members', group.members)
        if args.get('acl'):
            tags = j.core.tags.getObject(args.get('acl'))
            group.acl = tags.getDict() if tags.getDict() else group.acl
        self.osscl.group.set(group)
        return 'Group was created/updated successfully'

    def group__contactmethod(self, **args):
        if args.get('id'):
            if not self.osscl.group.exists(int(args.get('id'))):
                return 'Group with ID %s was not found.' % args.get('id')
            group = self.osscl.group.get(int(args.get('id')))
        elif args.get('name'):
            group = self.osscl.group.simpleSearch({'name': args.get('name')})
            if group:
                group = self.osscl.group.get(group[0]['id'])
            else:
                return 'Group with name %s can not be found' % args.get('name')
        else:
            return 'Group ID or name must be passed'
        contactmethod = group.new_contactmethod()
        contactmethod.type = args.get('type', contactmethod.type)
        contactmethod.value = args.get('value', contactmethod.value)
        self.osscl.group.set(group)
        return 'Group contactmethod was added successfully'

    def group__datasource(self, **args):
        if args.get('id'):
            if not self.osscl.group.exists(int(args.get('id'))):
                return 'Group with ID %s was not found.' % args.get('id')
            group = self.osscl.group.get(int(args.get('id')))
        elif args.get('name'):
            group = self.osscl.group.simpleSearch({'name': args.get('name')})
            if group:
                group = self.osscl.group.get(group[0]['id'])
            else:
                return 'Group with name %s can not be found' % args.get('name')
        else:
            return 'Group ID must be passed'
        datasource = group.new_datasource()
        datasource.name = args.get('datasourcename')
        self.osscl.group.set(group)
        return 'Group datasource was added successfully'

    def group__member(self, **args):
        if args.get('groupid'):
            if not self.osscl.group.exists(int(args.get('groupid'))):
                return 'Group with ID %s was not found.' % args.get('groupid')
            group = self.osscl.group.get(int(args.get('orgid')))
        elif args.get('group'):
            group = self.osscl.group.simpleSearch({'name': args.get('group')})
            if group:
                group = self.osscl.group.get(group[0]['id'])
            else:
                return 'Group with name %s can not be found' % args.get('name')
        else:
            return 'Group ID or name must be passed'
        user = args.get('user')
        if user:
            nativequery={'$or':[{'guid':user}, {'name':user}]}
            member = self.osscl.user.simpleSearch({}, nativequery=nativequery)
            if member:
                group.members.append(member[0]['guid'])
                self.osscl.group.set(group)
                return 'Group member was added successfully'
            else:
                return "User with this id/name not found"
        else:
            return 'User id/name must be passed'

    def group__comment(self, **args):
        if args.get('id'):
            if not self.osscl.group.exists(int(args.get('id'))):
                return 'Group with ID %s was not found.' % args.get('id')
            group = self.osscl.group.get(int(args.get('id')))
        elif args.get('name'):
            group = self.osscl.group.simpleSearch({'name': args.get('name')})
            if group:
                group = self.osscl.group.get(group[0]['id'])
            else:
                return 'Group with name %s can not be found' % args.get('name')
        else:
            return 'Group ID or name must be passed'
        comment = group.new_comment()
        comment.comment = args.get('comment') if args.get('comment') else comment.comment
        comment.time = args.get('created') if args.get('created') else comment.time
        author = args.get('author')
        nativequery={'$or':[{'guid':author}, {'name':author}]}
        author = self.osscl.user.simpleSearch({}, nativequery=nativequery)
        comment.author = author[0]['guid'] if author else comment.author
        self.osscl.group.set(group)
        return 'Group comment was added successfully'

    def group__list(self, **args):
        q = dict()
        if args.get('filter'):
            q = json.loads(args.get('filter'))
        start = int(args.get('start')) if args.get('start') else 0
        size = int(args.get('max')) if args.get('max') else None
        return self.osscl.group.simpleSearch(q, start, size)

    def group__delete(self, **args):
        self.osscl.group.delete(int(args.get('id')))
        return 'Group was deleted successfully'

    def project__create(self, **args):
        if args.get('id'):
            if not self.osscl.project.exists(int(args.get('id'))):
                return 'Project with ID %s was not found.' % args.get('id')
            project = self.osscl.project.get(int(args.get('id')))
        else:
            project = self.osscl.project.new()
        project.name = args.get('name', project.name)
        project.description = args.get('description', project.description)
        project.deadline = args.get('deadline', project.deadline)
        if args.get('acl'):
            tags = j.core.tags.getObject(args.get('acl'))
            project.acl = tags.getDict() if tags.getDict() else project.acl
        self.osscl.project.set(project)
        return 'Project was created/updated successfully'

    def project__list(self, **args):
        q = dict()
        if args.get('filter'):
            q = json.loads(args.get('filter'))
        start = int(args.get('start')) if args.get('start') else 0
        size = int(args.get('max')) if args.get('max') else None
        return self.osscl.project.simpleSearch(q, start, size)

    def project__delete(self, **args):
        self.osscl.project.delete(int(args.get('id')))
        return 'Project was deleted successfully'

    def project__comment(self, **args):
        if args.get('id'):
            if not self.osscl.project.exists(int(args.get('id'))):
                return 'Project with ID %s was not found.' % args.get('id')
            project = self.osscl.project.get(int(args.get('id')))
        elif args.get('name'):
            project = self.osscl.project.simpleSearch({'name': args.get('name')})
            if project:
                project = self.osscl.project.get(project[0]['id'])
            else:
                return 'Project with name %s can not be found' % args.get('name')
        else:
            return 'Project ID or name must be passed'
        comment = project.new_comment()
        comment.comment = args.get('comment')
        comment.time = args.get('created')
        comment.author = args.get('author')
        self.osscl.project.set(project)
        return 'Project comment was added successfully'

    def project__organization(self, **args):
        if args.get('projectid'):
            if not self.osscl.project.exists(int(args.get('projectid'))):
                return 'Group with ID %s was not found.' % args.get('projectid')
            project = self.osscl.project.get(int(args.get('orgid')))
        elif args.get('project'):
            project = self.osscl.project.simpleSearch({'project': args.get('project')})
            if project:
                project = self.osscl.project.get(project[0]['id'])
            else:
                return 'Group with name %s can not be found' % args.get('name')
        else:
            return 'Group ID or name must be passed'
        organization = args.get('organization')
        if organization:
            nativequery={'$or':[{'id':organization}, {'name':organization}]}
            org = self.osscl.organization.simpleSearch({}, nativequery=nativequery)
            if org:
                project.organizations.append(org[0]['guid'])
                self.osscl.project.set(project)
                return 'Project organization was added successfully'
            else:
                return "Organization with this id/name not found"
        else:
            return 'Organization id/name must be passed'

    def project__datasource(self, **args):
        if args.get('id'):
            if not self.osscl.project.exists(int(args.get('id'))):
                return 'Project with ID %s was not found.' % args.get('id')
            project = self.osscl.project.get(int(args.get('id')))
        elif args.get('name'):
            project = self.osscl.project.simpleSearch({'name': args.get('name')})
            if project:
                project = self.osscl.project.get(project[0]['id'])
            else:
                return 'Project with name %s can not be found' % args.get('name')
        else:
            return 'Project ID or name must be passed'
        datasource = project.new_datasource()
        datasource.name = args.get('datasourcename') if args.get('datasourcename') else datasource.name
        self.osscl.project.set(project)
        return 'Project contactmethod was added successfully'

    def user__create(self, **args):
        user = self.osscl.user.new()
        userdata = user.dump()
        for arg in args:
            if arg in userdata:
                if arg == 'acl':
                    tags = j.core.tags.getObject(args.get('acl'))
                    userdata['acl'] = tags.getDict() if tags.getDict() else userdata['acl']
                else:
                    userdata[arg] = args.get(arg)
        user.dict2obj(userdata)
        self.osscl.user.set(user)
        return 'User was added successfully'

    def user__datasource(self, **args):
        if args.get('id'):
            if not self.osscl.user.exists(int(args.get('id'))):
                return 'User with ID %s was not found.' % args.get('id')
            user = self.osscl.user.get(int(args.get('id')))
        elif args.get('name'):
            user = self.osscl.user.simpleSearch({'name': args.get('name')})
            if user:
                user = self.osscl.user.get(user[0]['id'])
            else:
                return 'User with name %s cannot be found' % args.get('name')
        else:
            return 'User ID or name must be passed'
        datasource = user.new_datasource()
        datasource.name = args.get('datasourcename') if args.get('datasourcename') else datasource.name
        self.osscl.user.set(user)
        return 'User datasource was added successfully'

    def user__address(self, **args):
        if args.get('userid'):
            if not self.osscl.user.exists(int(args.get('userid'))):
                return 'User with ID %s was not found.' % args.get('userid')
            user = self.osscl.user.get(int(args.get('userid')))
        elif args.get('username'):
            user = self.osscl.user.simpleSearch({'name': args.get('username')})
            if user:
                user = self.osscl.user.get(user[0]['id'])
            else:
                return 'User with name %s can not be found' % args.get('username')
        else:
            return 'User ID or name must be passed'
        address = self.osscl.address.new()
        address.country = args.get('country') if args.get('country') else address.country
        address.city = args.get('city') if args.get('city') else address.city
        address.citycode = args.get('citycode') if args.get('citycode') else address.citycode
        address.zone = args.get('zone') if args.get('zone') else address.zone
        address.region = args.get('region') if args.get('region') else address.region
        address.street = args.get('street') if args.get('street') else address.street
        address.nr = args.get('nr') if args.get('nr') else address.nr
        guid,_, _ = self.osscl.address.set(address)
        user.addresses.append(guid)
        self.osscl.user.set(user)
        return 'User address was added successfully'

    def user__contactmethod(self, **args):
        if args.get('id'):
            if not self.osscl.user.exists(int(args.get('id'))):
                return 'User with ID %s was not found.' % args.get('id')
            user = self.osscl.user.get(int(args.get('id')))
        elif args.get('name'):
            user = self.osscl.user.simpleSearch({'name': args.get('name')})
            if user:
                user = self.osscl.user.get(user[0]['id'])
            else:
                return 'User with name %s can not be found' % args.get('name')
        else:
            return 'User ID or name must be passed'
        contactmethod = self.osscl.contactmethod.new()
        contactmethod.type = args.get('type')
        contactmethod.value = args.get('value')
        guid, _, _ = self.osscl.contactmethod.set(contactmethod)
        user.contactmethods.append(guid)
        self.osscl.user.set(user)
        return 'User contactmethod was added successfully'

    def user__list(self, **args):
        q = dict()
        if args.get('filter'):
            q = json.loads(args.get('filter'))
        start = int(args.get('start')) if args.get('start') else 0
        size = int(args.get('max')) if args.get('max') else None
        return self.osscl.user.simpleSearch(q, start, size)

    def user__delete(self, **args):
        self.osscl.user.delete(int(args.get('id')))
        return 'User was deleted successfully'

    def user__comment(self, **args):
        if args.get('id'):
            if not self.osscl.user.exists(int(args.get('id'))):
                return 'User with ID %s was not found.' % args.get('id')
            user = self.osscl.user.get(int(args.get('id')))
        elif args.get('name'):
            user = self.osscl.user.simpleSearch({'name': args.get('name')})
            if user:
                user = self.osscl.user.get(user[0]['id'])
            else:
                return 'User with name %s can not be found' % args.get('name')
        else:
            return 'User ID or name must be passed'
        comment = user.new_comment()
        comment.comment = args.get('comment') if args.get('comment') else comment.comment
        comment.time = args.get('created') if args.get('created') else comment.time
        author = args.get('author')
        nativequery={'$or':[{'guid':author}, {'name':author}]}
        author = self.osscl.user.simpleSearch({}, nativequery=nativequery)
        comment.author = author[0]['guid'] if author else comment.author
        self.osscl.user.set(user)
        return 'User comment was added successfully'

    def ticket__create(self, **args):
        ticket = self.osscl.ticket.new()
        ticketdata = ticket.dump()
        for arg in args:
            if arg in ticketdata:
                if arg == 'acl':
                    tags = j.core.tags.getObject(args.get('acl'))
                    ticketdata['acl'] = tags.getDict() if tags.getDict() else ticketdata['acl']
                else:
                    ticketdata[arg] = args.get(arg)
        ticket.dict2obj(ticketdata)
        self.osscl.ticket.set(ticket)
        return 'Ticket was added successfully'

    def ticket__list(self, **args):
        maximum = args.get('max')
        start = args.get('start', 0)
        query = json.loads(args.get('filter', "{}"))
        tickets = self.osscl.ticket.simpleSearch(query, size=maximum, start=start)
        result = list()
        verbose = int(args.get('verbose'), 3)
        if verbose>3:
            verbose=3
        else:
            verbose=1
        if verbose>1:
            for ticket in tickets:
                result.append(ticket.dump()) 
        else:
            out=""
            for ticket in tickets:
                out+="%-7s %-15s %-10s %s\n"%(ticket.id,ticket.name,ticket.description,ticket.type)
            result=out
        return result

    def ticket__delete(self, **args):
        self.osscl.ticketid.delete(int(args.get('id')))
        return 'Ticket was deleted successfully'

    def ticket__assign(self, **args):
        assignee = args.get('taskowner')
        ticket = self.osscl.ticket.get(int(args.get('id')))
        if not ticket:
            return 'No ticket with id "%s" was found' % args.get('id')
        ticket.taskowner = assignee
        self.osscl.ticket.set(ticket)
        return 'Ticket was updated successfully'

    def ticket__duplicate(self, **args):
        machine = self.osscl.ticket.new()
        id = args.get('id')
        query = {'id':id}
        if not id:
            name = args.get('name')
            query = {'name': '*%s*' % name}
        ticket = self.osscl.ticket.simpleSearch({}, partials=query)
        duplicate = args.get('duplicate')
        if not ticket:
            return 'Ticket not found'
        ticket = ticket[0]
        ticket['duplicate'].append(int(duplicate))
        machine.dict2obj(ticket)
        self.osscl.ticket.set(ticket)
        return 'Ticket was updated successfully'

    def ticket__depend(self, **args):
        machine = self.osscl.ticket.new()
        id = args.get('id')
        query = {'id':id}
        if not id:
            name = args.get('name')
            query = {'name': '*%s*' % name}
        ticket = self.osscl.ticket.simpleSearch({}, partials=query)
        if not ticket:
            return 'Ticket not found'
        ticket = ticket[0]
        depend = args.get('on')
        ticket['depends'].append(int(depend))
        machine.dict2obj(ticket)
        self.osscl.ticket.set(ticket)
        return 'Ticket was updated successfully'

    def ticket__subtask(self,**args):
        machine = self.osscl.ticket.new()
        id = args.get('id')
        query = {'id':id}
        if not id:
            name = args.get('name')
            query = {'name': '*%s*' % name}
        ticket = self.osscl.ticket.simpleSearch({}, partials=query)
        if not ticket:
            return 'Ticket not found'
        ticket = ticket[0]
        parent = args.get('parent')
        ticket['parent'] = int(parent)
        machine.dict2obj(ticket)
        self.osscl.ticket.set(ticket)
        return 'Ticket was updated successfully'

    def ticket__get(self,**args):
        id = args.get('id')
        ticket = self.osscl.ticket.get(id)
        if not ticket:
            return 'Ticket not found'
        ticket = ticket.dump()
        out = 'Ticket:\n'
        for k, v in ticket.iteritems():
            out += '%s: %s\n' % (k, v)
        return out

    def ticket__comment(self, **args):
        if args.get('id'):
            if not self.osscl.ticket.exists(int(args.get('id'))):
                return 'Ticket with ID %s was not found.' % args.get('id')
            ticket = self.osscl.ticket.get(int(args.get('id')))
        elif args.get('name'):
            ticket = self.osscl.ticket.simpleSearch({'name': args.get('name')})
            if ticket:
                ticket = self.osscl.ticket.get(ticket[0]['id'])
            else:
                return 'Ticket with name %s can not be found' % args.get('name')
        else:
            return 'Ticket ID or name must be passed'
        comment = ticket.new_comment()
        comment.comment = args.get('comment')
        comment.time = args.get('created')
        comment.author = args.get('author')
        self.osscl.ticket.set(ticket)
        return 'Ticket comment was added successfully'

    def ticket__message(self, **args):
        if args.get('ticketid'):
            if not self.osscl.ticket.exists(int(args.get('ticketid'))):
                return 'Ticket with ID %s was not found.' % args.get('ticketid')
            ticket = self.osscl.ticket.get(int(args.get('ticketid')))
        else:
            return 'Ticket ID must be passed'
        if args.get('id') and self.osscl.message.exists(int(args.get('id'))):
            message = self.osscl.message.get(int(args.get('id')))
        else:
            message = ticket.new_message()
        message.message = args.get('message', message.message)
        message.time = args.get('created', message.time)
        message.author = args.get('author', message.author)
        self.osscl.ticket.set(ticket)
        return 'Ticket message was added successfully'

    def sprint__create(self, **args):
        if args.get('id'):
            if not self.osscl.sprint.exists(int(args.get('id'))):
                return 'Sprint with ID %s was not found.' % args.get('id')
            sprint = self.osscl.sprint.get(int(args.get('id')))
        else:
            sprint = self.osscl.sprint.new()
        sprint.name = args.get('name')
        sprint.description = args.get('description')
        sprint.organizations = args.get('organizations')
        sprint.start = args.get('start')
        sprint.stop = args.get('stop')
        # TODO set data sources
        if args.get('acl'):
            tags = j.core.tags.getObject(args.get('acl'))
            sprint.acl = tags.getDict() if tags.getDict() else sprint.acl
        self.osscl.sprint.set(sprint)
        return 'Sprint was created/updated successfully'

    def sprint__list(self, **args):
        q = dict()
        if args.get('filter'):
            q = json.loads(args.get('filter'))
        start = int(args.get('start')) if args.get('start') else 0
        size = int(args.get('max')) if args.get('max') else None
        return self.osscl.sprint.simpleSearch(q, start, size)

    def sprint__delete(self, **args):
        self.osscl.sprint.delete(int(args.get('id')))
        return 'Sprint was deleted successfully'

    def sprint__comment(self, **args):
        if args.get('id'):
            if not self.osscl.sprint.exists(int(args.get('id'))):
                return 'Sprint with ID %s was not found.' % args.get('id')
            sprint = self.osscl.sprint.get(int(args.get('id')))
        elif args.get('name'):
            sprint = self.osscl.sprint.simpleSearch({'name': args.get('name')})
            if sprint:
                sprint = self.osscl.sprint.get(sprint[0]['id'])
            else:
                return 'Sprint with name %s can not be found' % args.get('name')
        else:
            return 'Sprint ID or name must be passed'
        comment = sprint.new_comment()
        comment.comment = args.get('comment')
        comment.time = args.get('created')
        comment.author = args.get('author')
        self.osscl.sprint.set(sprint)
        return 'Sprint comment was added successfully'

    def datacenter__create(self, **args):
        if args.get('id'):
            if not self.osscl.datacenter.exists(int(args.get('id'))):
                return 'Datacenter with ID %s was not found.' % args.get('id')
            datacenter = self.osscl.datacenter.get(int(args.get('id')))
        else:
            datacenter = self.osscl.datacenter.new()
        datacenter.name = args.get('name')
        datacenter.description = args.get('description')
        datacenter.label = args.get('label')
        datacenter.organization = args.get('organization')
        # TODO set data sources
        if args.get('acl'):
            tags = j.core.tags.getObject(args.get('acl'))
            datacenter.acl = tags.getDict() if tags.getDict() else datacenter.acl
        self.osscl.datacenter.set(datacenter)
        return 'Datacenter was created/updated successfully'

    def datacenter__address(self, **args):
        if args.get('id'):
            if not self.osscl.datacenter.exists(int(args.get('id'))):
                return 'Datacenter with ID %s was not found.' % args.get('id')
            datacenter = self.osscl.datacenter.get(int(args.get('id')))
        elif args.get('name'):
            datacenter = self.osscl.datacenter.simpleSearch({'name': args.get('name')})
            if datacenter:
                datacenter = self.osscl.datacenter.get(datacenter[0]['id'])
            else:
                return 'Datacenter with name %s can not be found' % args.get('name')
        else:
            return 'Datacenter ID or name must be passed'
        address = datacenter.new_address()
        address.country = args.get('country')
        address.city = args.get('city')
        address.citycode = args.get('citycode')
        address.street = args.get('street')
        address.nr = args.get('nr')
        self.osscl.datacenter.set(datacenter)
        return 'Datacenter address was added successfully'

    def datacenter__contactmethod(self, **args):
        if args.get('id'):
            if not self.osscl.datacenter.exists(int(args.get('id'))):
                return 'Datacenter with ID %s was not found.' % args.get('id')
            datacenter = self.osscl.datacenter.get(int(args.get('id')))
        elif args.get('name'):
            datacenter = self.osscl.datacenter.simpleSearch({'name': args.get('name')})
            if datacenter:
                datacenter = self.osscl.datacenter.get(datacenter[0]['id'])
            else:
                return 'Datacenter with name %s can not be found' % args.get('name')
        else:
            return 'Datacenter ID or name must be passed'
        contactmethod = datacenter.new_contactmethod()
        contactmethod.type = args.get('type')
        contactmethod.value = args.get('value')
        self.osscl.datacenter.set(datacenter)
        return 'Datacenter contactmethod was added successfully'

    def datacenter__list(self, **args):
        q = dict()
        if args.get('filter'):
            q = json.loads(args.get('filter'))
        start = int(args.get('start')) if args.get('start') else 0
        size = int(args.get('max')) if args.get('max') else None
        return self.osscl.datacenter.simpleSearch(q, start, size)

    def datacenter__delete(self, **args):
        self.osscl.datacenter.delete(int(args.get('id')))
        return 'Datacenter was deleted successfully'

    def datacenter__comment(self, **args):
        if args.get('id'):
            if not self.osscl.datacenter.exists(int(args.get('id'))):
                return 'Datacenter with ID %s was not found.' % args.get('id')
            datacenter = self.osscl.datacenter.get(int(args.get('id')))
        elif args.get('name'):
            datacenter = self.osscl.datacenter.simpleSearch({'name': args.get('name')})
            if datacenter:
                datacenter = self.osscl.datacenter.get(datacenter[0]['id'])
            else:
                return 'Datacenter with name %s can not be found' % args.get('name')
        else:
            return 'Datacenter ID or name must be passed'
        comment = datacenter.new_comment()
        comment.comment = args.get('comment')
        comment.time = args.get('created')
        comment.author = args.get('author')
        self.osscl.datacenter.set(datacenter)
        return 'Datacenter comment was added successfully'

    def pod__create(self, **args):
        if args.get('id'):
            if not self.osscl.pod.exists(int(args.get('id'))):
                return 'Pod with ID %s was not found.' % args.get('id')
            pod = self.osscl.pod.get(int(args.get('id')))
        else:
            pod = self.osscl.pod.new()
        pod.name = args.get('name')
        pod.description = args.get('description')
        pod.label = args.get('label')
        pod.organizations = args.get('organizations')
        pod.datacenters = args.get('datacenters')
        # TODO set data sources
        if args.get('acl'):
            tags = j.core.tags.getObject(args.get('acl'))
            pod.acl = tags.getDict() if tags.getDict() else pod.acl
        self.osscl.pod.set(pod)
        return 'Pod was created/updated successfully'

    def pod__list(self, **args):
        q = dict()
        if args.get('filter'):
            q = json.loads(args.get('filter'))
        start = int(args.get('start')) if args.get('start') else 0
        size = int(args.get('max')) if args.get('max') else None
        return self.osscl.pod.simpleSearch(q, start, size)

    def pod__delete(self, **args):
        self.osscl.pod.delete(int(args.get('id')))
        return 'Pod was deleted successfully'

    def pod__comment(self, **args):
        if args.get('id'):
            if not self.osscl.pod.exists(int(args.get('id'))):
                return 'Pod with ID %s was not found.' % args.get('id')
            pod = self.osscl.pod.get(int(args.get('id')))
        elif args.get('name'):
            pod = self.osscl.pod.simpleSearch({'name': args.get('name')})
            if pod:
                pod = self.osscl.pod.get(pod[0]['id'])
            else:
                return 'Pod with name %s can not be found' % args.get('name')
        else:
            return 'Pod ID or name must be passed'
        comment = pod.new_comment()
        comment.comment = args.get('comment')
        comment.time = args.get('created')
        comment.author = args.get('author')
        self.osscl.pod.set(pod)
        return 'Pod comment was added successfully'

    def rack__create(self, **args):
        if args.get('id'):
            if not self.osscl.rack.exists(int(args.get('id'))):
                return 'Rack with ID %s was not found.' % args.get('id')
            rack = self.osscl.rack.get(int(args.get('id')))
        else:
            rack = self.osscl.rack.new()
        rack.name = args.get('name')
        rack.description = args.get('description')
        rack.label = args.get('label')
        rack.organization = args.get('organizations')
        rack.datacenter = args.get('datacenters')
        rack.pod = args.get('pods')
        # TODO set data sources
        if args.get('acl'):
            tags = j.core.tags.getObject(args.get('acl'))
            rack.acl = tags.getDict() if tags.getDict() else rack.acl
        self.osscl.rack.set(rack)
        return 'Rack was created/updated successfully'

    def rack__list(self, **args):
        q = dict()
        if args.get('filter'):
            q = json.loads(args.get('filter'))
        start = int(args.get('start')) if args.get('start') else 0
        size = int(args.get('max')) if args.get('max') else None
        return self.osscl.rack.simpleSearch(q, start, size)

    def rack__delete(self, **args):
        self.osscl.rack.delete(int(args.get('id')))
        return 'Rack was deleted successfully'

    def rack__comment(self, **args):
        if args.get('id'):
            if not self.osscl.rack.exists(int(args.get('id'))):
                return 'Rack with ID %s was not found.' % args.get('id')
            rack = self.osscl.rack.get(int(args.get('id')))
        elif args.get('name'):
            rack = self.osscl.rack.simpleSearch({'name': args.get('name')})
            if rack:
                rack = self.osscl.rack.get(rack[0]['id'])
            else:
                return 'Rack with name %s can not be found' % args.get('name')
        else:
            return 'Rack ID or name must be passed'
        comment = rack.new_comment()
        comment.comment = args.get('comment')
        comment.time = args.get('created')
        comment.author = args.get('author')
        self.osscl.rack.set(rack)
        return 'Rack comment was added successfully'

    def asset__create(self, **args):
        if args.get('id'):
            if not self.osscl.asset.exists(int(args.get('id'))):
                return 'Asset with ID %s was not found.' % args.get('id')
            asset = self.osscl.asset.get(int(args.get('id')))
        else:
            asset = self.osscl.asset.new()
        asset.name = args.get('name')
        asset.description = args.get('description')
        asset.label = args.get('label')
        asset.rack = args.get('rack')
        asset.U = args.get('U')
        asset.rackpos = args.get('pos')
        asset.brand = args.get('brand')
        asset.model = args.get('model')
        asset.type = args.get('type')
        asset.parent = args.get('parent')
        asset.depends = args.get('depends')
        # TODO set data sources
        if args.get('acl'):
            tags = j.core.tags.getObject(args.get('acl'))
            asset.acl = tags.getDict() if tags.getDict() else asset.acl
        self.osscl.asset.set(asset)
        return 'Asset was created/updated successfully'

    def asset__list(self, **args):
        q = dict()
        if args.get('filter'):
            q = json.loads(args.get('filter'))
        start = int(args.get('start')) if args.get('start') else 0
        size = int(args.get('max')) if args.get('max') else None
        return self.osscl.asset.simpleSearch(q, start, size)

    def asset__delete(self, **args):
        self.osscl.asset.delete(int(args.get('id')))
        return 'Asset was deleted successfully'

    def asset__comment(self, **args):
        if args.get('id'):
            if not self.osscl.asset.exists(int(args.get('id'))):
                return 'Asset with ID %s was not found.' % args.get('id')
            asset = self.osscl.asset.get(int(args.get('id')))
        elif args.get('name'):
            asset = self.osscl.asset.simpleSearch({'name': args.get('name')})
            if asset:
                asset = self.osscl.asset.get(asset[0]['id'])
            else:
                return 'Asset with name %s can not be found' % args.get('name')
        else:
            return 'Asset ID or name must be passed'
        comment = asset.new_comment()
        comment.comment = args.get('comment')
        comment.time = args.get('created')
        comment.author = args.get('author')
        self.osscl.asset.set(asset)
        return 'Asset comment was added successfully'

    def machine__create(self, **args):
        if args.get('id'):
            if not self.osscl.machine.exists(int(args.get('id'))):
                return 'Machine with ID %s was not found.' % args.get('id')
            machine = self.osscl.machine.get(int(args.get('id')))
        else:
            machine = self.osscl.machine.new()
        machine.name = args.get('name') if args.get('name') else machine.name
        machine.description = args.get('description') if args.get('description') else machine.description
        machine.label = args.get('label') if args.get('label') else machine.label
        machine.memory = int(args.get('memory')) if args.get('memory') else machine.memory
        machine.ssdcapacity = int(args.get('ssdcapacity')) if args.get('ssdcapacity') else machine.ssdcapacity
        machine.hdcapacity = int(args.get('hdcapacity')) if args.get('hdcapacity') else machine.hdcapacity
        machine.cpumhz = int(args.get('cpumhz')) if args.get('cpumhz') else machine.cpumhz
        machine.nrcores = int(args.get('nrcores')) if args.get('nrcores') else machine.nrcores
        machine.nrcpu = int(args.get('nrcpu')) if args.get('nrcpu') else machine.nrcpu
        organization = args.get('organization')
        org = None
        if organization:
          nativequery={'$or':[{'id':organization}, {'name':organization}]}
          org = self.osscl.organization.simpleSearch({}, nativequery=nativequery)
        orgid = org[0]['id'] if org else machine.organization
        machine.organization = orgid
        machine.assethost = int(args.get('assethost')) if args.get('assethost') else machine.assethost
        machine.parent = int(args.get('parent')) if args.get('parent') else machine.parent
        machine.type = args.get('type') if args.get('type') else machine.type
        if args.get('acl'):
            tags = j.core.tags.getObject(args.get('acl'))
            machine.acl = tags.getDict() if tags.getDict() else machine.acl
        self.osscl.machine.set(machine)
        return 'Machine was created/updated successfully'

    def machine__interface(self, **args):
        if args.get('id'):
            if not self.osscl.machine.exists(int(args.get('id'))):
                return 'Machine with ID %s was not found.' % args.get('id')
            machine = self.osscl.machine.get(int(args.get('id')))
        elif args.get('name'):
            machine = self.osscl.machine.simpleSearch({'name': args.get('name')})
            if machine:
                machine = self.osscl.machine.get(machine[0]['id'])
            else:
                return 'Machine with name %s can not be found' % args.get('name')
        else:
            return 'Machine ID or name must be passed'
        interfaceid = args.get('interface')
        if interfaceid:
            nativequery={'$or':[{'id':interfaceid}, {'name':interfaceid}]}
            interface = self.osscl.interface.simpleSearch({}, nativequery=nativequery)
            if interface:
                member = machine.new_interface()
                member.type = member[0]['type']
                member.macaddr = member[0]['macaddr']
                member.vlanid = member[0]['vlanid']
                member.organization = member[0]['organization']
                member.netaddr = member[0]['netaddr']
                member.connects = member[0]['connects']
                member.brand = member[0]['brand']
                member.model = member[0]['model']
                member.description = member[0]['description']
                member.supportremarks = member[0]['supportremarks']
                member.comments = member[0]['comments']
                self.osscl.machine.set(group)
                return 'Machine interface was added successfully'
            else:
                return "Interface with this id/name not found"
        else:
            return 'Interface id/name must be passed'

    def machine__datasource(self, **args):
        if args.get('id'):
            if not self.osscl.machine.exists(int(args.get('id'))):
                return 'Machine with ID %s was not found.' % args.get('id')
            machine = self.osscl.machine.get(int(args.get('id')))
        elif args.get('name'):
            machine = self.osscl.machine.simpleSearch({'name': args.get('name')})
            if machine:
                machine = self.osscl.machine.get(machine[0]['id'])
            else:
                return 'Machine with name %s can not be found' % args.get('name')
        else:
            return 'Machine ID or name must be passed'
        datasource = machine.new_datasource()
        datasource.name = args.get('datasourcename') if args.get('datasourcename') else datasource.name
        self.osscl.machine.set(machine)
        return 'Machine datasource was added successfully'

    def machine__depend(self, **args):
        machine = self.osscl.machine.new()
        id = args.get('id')
        query = {'id':id}
        if not id:
            name = args.get('name')
            query = {'name': '*%s*' % name}
        machine = self.osscl.machine.simpleSearch({}, partials=query)
        if not machine:
            return 'Machine not found'
        machine = machine[0]
        depend = args.get('on')
        machine['depends'].append(int(depend))
        machine.dict2obj(machine)
        self.osscl.machine.set(machine)
        return 'Machine was updated successfully'

    def machine__list(self, **args):
        q = dict()
        if args.get('filter'):
            q = json.loads(args.get('filter'))
        start = int(args.get('start')) if args.get('start') else 0
        size = int(args.get('max')) if args.get('max') else None
        return self.osscl.machine.simpleSearch(q, start, size)

    def machine__delete(self, **args):
        self.osscl.machine.delete(int(args.get('id')))
        return 'Machine was deleted successfully'

    def machine__comment(self, **args):
        if args.get('id'):
            if not self.osscl.machine.exists(int(args.get('id'))):
                return 'Machine with ID %s was not found.' % args.get('id')
            machine = self.osscl.machine.get(int(args.get('id')))
        elif args.get('name'):
            machine = self.osscl.machine.simpleSearch({'name': args.get('name')})
            if machine:
                machine = self.osscl.machine.get(machine[0]['id'])
            else:
                return 'Machine with name %s can not be found' % args.get('name')
        else:
            return 'Machine ID or name must be passed'
        comment = machine.new_comment()
        comment.comment = args.get('comment')
        comment.time = args.get('created')
        comment.author = args.get('author')
        self.osscl.machine.set(machine)
        return 'Machine comment was added successfully'

    def service__create(self, **args):
        if args.get('id'):
            if not self.osscl.service.exists(int(args.get('id'))):
                return 'Service with ID %s was not found.' % args.get('id')
            service = self.osscl.service.get(int(args.get('id')))
        else:
            service = self.osscl.service.new()
        service.name = args.get('name') if args.get('name') else service.name
        service.description = args.get('description') if args.get('description') else service.description
        service.label = args.get('label') if args.get('label') else service.label
        service.memory = int(args.get('memory')) if args.get('memory') else service.memory
        service.ssdcapacity = int(args.get('ssdcapacity')) if args.get('ssdcapacity') else service.ssdcapacity
        service.hdcapacity = int(args.get('hdcapacity')) if args.get('hdcapacity') else service.hdcapacity
        service.cpumhz = int(args.get('cpumhz')) if args.get('cpumhz') else service.cpumhz
        service.nrcores = int(args.get('nrcores')) if args.get('nrcores') else service.nrcores
        service.nrcpu = int(args.get('nrcpu')) if args.get('nrcpu') else service.nrcpu
        org = None
        organization = args.get('organization')
        if organization:
          nativequery={'$or':[{'id':organization}, {'name':organization}]}
          org = self.osscl.organization.simpleSearch({}, nativequery=nativequery)
        orgid = org[0]['id'] if org else service.organization
        service.organization = orgid
        service.assethost = int(args.get('machinehost')) if args.get('assethost') else service.machinehost
        service.parent = int(args.get('parent')) if args.get('parent') else service.parent
        service.admin_name = args.get('admin_name', service.admin_name)
        service.admin_passwd = args.get('admin_passwd', service.admin_passwd)
        service.type = args.get('type') if args.get('type') else service.type
        if args.get('acl'):
            tags = j.core.tags.getObject(args.get('acl'))
            service.acl = tags.getDict() if tags.getDict() else service.acl
        self.osscl.service.set(service)
        return 'Service was created/updated successfully'

    def service__serviceport(self, **args):
        if args.get('id'):
            if not self.osscl.service.exists(int(args.get('id'))):
                return 'Service with ID %s was not found.' % args.get('id')
            service = self.osscl.service.get(int(args.get('id')))
        elif args.get('name'):
            service = self.osscl.service.simpleSearch({'name': args.get('name')})
            if service:
                service = self.osscl.service.get(service[0]['id'])
            else:
                return 'Service with name %s can not be found' % args.get('name')
        else:
            return 'Service ID or name must be passed'
        serviceportid = args.get('serviceport')
        if serviceportid:
            nativequery={'$or':[{'id':serviceportid}, {'name':serviceportid}]}
            serviceport = self.osscl.serviceport.simpleSearch({}, nativequery=nativequery)
            if serviceport:
                guid = serviceport['guid']
                service.serviceports.append(guid)
                self.osscl.service.set(service)
                return 'Service serviceport was added successfully'
            else:
                member = self.osscl.serviceport.new()
                member.ipaddr = args.get('ipaddr')
                member.ipaddr6 = args.get('ipaddr6')
                member.url = args.get('url')
                member.port = args.get('port')
                member.type = args.get('type')
                member.description = args.get('description')
                member.supportremarks = args.get('supportremarks')
                member.comments = args.get('comments')
                guid, _, _ = self.osscl.serviceport.set(member)
                service.serviceports.append(guid)
                self.osscl.service.set(service)
                return "Service serviceport was added successfully"
        else:
            return 'serviceport id/name must be passed'

    def service__datasource(self, **args):
        if args.get('id'):
            if not self.osscl.service.exists(int(args.get('id'))):
                return 'Service with ID %s was not found.' % args.get('id')
            service = self.osscl.service.get(int(args.get('id')))
        elif args.get('name'):
            service = self.osscl.service.simpleSearch({'name': args.get('name')})
            if service:
                service = self.osscl.service.get(service[0]['id'])
            else:
                return 'Service with name %s can not be found' % args.get('name')
        else:
            return 'Service ID or name must be passed'
        datasource = service.new_datasource()
        datasource.name = args.get('datasourcename') if args.get('datasourcename') else datasource.name
        self.osscl.service.set(service)
        return 'Service datasource was added successfully'

    def service__depend(self, **args):
        service = self.osscl.service.new()
        id = args.get('id')
        query = {'id':id}
        if not id:
            name = args.get('name')
            query = {'name': '*%s*' % name}
        service = self.osscl.service.simpleSearch({}, partials=query)
        if not service:
            return 'Service not found'
        service = service[0]
        depend = args.get('on')
        service['depends'].append(int(depend))
        service.dict2obj(service)
        self.osscl.service.set(service)
        return 'Service was updated successfully'

    def service__list(self, **args):
        q = dict()
        if args.get('filter'):
            q = json.loads(args.get('filter'))
        start = int(args.get('start')) if args.get('start') else 0
        size = int(args.get('max')) if args.get('max') else None
        return self.osscl.service.simpleSearch(q, start, size)

    def service__delete(self, **args):
        self.osscl.service.delete(int(args.get('id')))
        return 'Service was deleted successfully'

    def service__comment(self, **args):
        if args.get('id'):
            if not self.osscl.service.exists(int(args.get('id'))):
                return 'Service with ID %s was not found.' % args.get('id')
            service = self.osscl.service.get(int(args.get('id')))
        elif args.get('name'):
            service = self.osscl.service.simpleSearch({'name': args.get('name')})
            if service:
                service = self.osscl.service.get(service[0]['id'])
            else:
                return 'Service with name %s can not be found' % args.get('name')
        else:
            return 'Service ID or name must be passed'
        comment = service.new_comment()
        comment.comment = args.get('comment')
        comment.time = args.get('created')
        comment.author = args.get('author')
        self.osscl.service.set(service)
        return 'Service comment was added successfully'

    def document__create(self, **args):
        if args.get('id'):
            if not self.osscl.document.exists(int(args.get('id'))):
                return 'Document with ID %s was not found.' % args.get('id')
            document = self.osscl.document.get(int(args.get('id')))
        else:
            document = self.osscl.document.new()
        documentdata = document.dump()
        for arg in args:
            if arg in documentdata:
                if arg == 'acl':
                    tags = j.core.tags.getObject(args.get('acl'))
                    documentdata['acl'] = tags.getDict() if tags.getDict() else documentdata['acl']
                elif arg == 'parent':
                    parent = args.get('parent')
                    nativequery={'$or':[{'id':parent}, {'name':parent}]}
                    parent = self.osscl.document.simpleSearch({}, nativequery=nativequery)
                    document.parent = parent[0]['id'] if parent else document.parent
                else:
                    documentdata[arg] = args.get(arg)
        document.dict2obj(documentdata)
        self.osscl.document.set(document)
        return 'Document was created/updated successfully'

    def document__list(self, **args):
        q = dict()
        if args.get('filter'):
            q = json.loads(args.get('filter'))
        start = int(args.get('start')) if args.get('start') else 0
        size = int(args.get('max')) if args.get('max') else None
        return self.osscl.document.simpleSearch(q, start, size)

    def document__delete(self, **args):
        self.osscl.document.delete(int(args.get('id')))
        return 'Document was deleted successfully'

    def document__comment(self, **args):
        if args.get('id'):
            if not self.osscl.document.exists(int(args.get('id'))):
                return 'Document with ID %s was not found.' % args.get('id')
            document = self.osscl.document.get(int(args.get('id')))
        elif args.get('name'):
            document = self.osscl.document.simpleSearch({'name': args.get('name')})
            if document:
                document = self.osscl.document.get(document[0]['id'])
            else:
                return 'Document with name %s can not be found' % args.get('name')
        else:
            return 'Document ID or name must be passed'
        comment = document.new_comment()
        comment.comment = args.get('comment')
        comment.time = args.get('created')
        comment.author = args.get('author')
        self.osscl.document.set(document)
        return 'Document comment was added successfully'

    def workflow__create(self, **args):
        if args.get('id'):
            if not self.osscl.workflow.exists(int(args.get('id'))):
                return 'Workflow with ID %s was not found.' % args.get('id')
            workflow = self.osscl.workflow.get(int(args.get('id')))
        else:
            workflow = self.osscl.workflow.new()
        workflowdata = workflow.dump()
        for arg in args:
            if arg in workflowdata:
                if arg == 'acl':
                    tags = j.core.tags.getObject(args.get('acl'))
                    workflowdata['acl'] = tags.getDict() if tags.getDict() else workflowdata['acl']
                elif arg == 'firststep':
                    firststep = args.get('firststep')
                    nativequery={'$or':[{'id':firststep}, {'name':firststep}]}
                    firststep = self.osscl.workflowstep.simpleSearch({}, nativequery=nativequery)
                    workflow.firststep = firststep[0]['id'] if firststep else workflow.firststep
                else:
                    workflowdata[arg] = args.get(arg)
        workflow.dict2obj(workflowdata)
        self.osscl.workflow.set(workflow)
        return 'Workflow was created/updated successfully'

    def workflow__list(self, **args):
        q = dict()
        if args.get('filter'):
            q = json.loads(args.get('filter'))
        start = int(args.get('start')) if args.get('start') else 0
        size = int(args.get('max')) if args.get('max') else None
        return self.osscl.workflow.simpleSearch(q, start, size)

    def workflow__delete(self, **args):
        self.osscl.workflow.delete(int(args.get('id')))
        return 'Workflow was deleted successfully'

    def workflow__comment(self, **args):
        if args.get('id'):
            if not self.osscl.workflow.exists(int(args.get('id'))):
                return 'Workflow with ID %s was not found.' % args.get('id')
            workflow = self.osscl.workflow.get(int(args.get('id')))
        elif args.get('name'):
            workflow = self.osscl.workflow.simpleSearch({'name': args.get('name')})
            if workflow:
                workflow = self.osscl.workflow.get(workflow[0]['id'])
            else:
                return 'Workflow with name %s can not be found' % args.get('name')
        else:
            return 'Workflow ID or name must be passed'
        comment = workflow.new_comment()
        comment.comment = args.get('comment')
        comment.time = args.get('created')
        comment.author = args.get('author')
        self.osscl.workflow.set(workflow)
        return 'Workflow comment was added successfully'

    def workflowstep__create(self, **args):
        if args.get('id'):
            if not self.osscl.workflowstep.exists(int(args.get('id'))):
                return 'Workflow with ID %s was not found.' % args.get('id')
            workflowstep = self.osscl.workflowstep.get(int(args.get('id')))
        else:
            workflowstep = self.osscl.workflowstep.new()
        workflowstepdata = workflowstep.dump()
        for arg in args:
            if arg in workflowstepdata:
                if arg == 'acl':
                    tags = j.core.tags.getObject(args.get('acl'))
                    workflowstepdata['acl'] = tags.getDict() if tags.getDict() else workflowstepdata['acl']
                else:
                    workflowstepdata[arg] = args.get(arg)
        workflowstep.dict2obj(workflowstepdata)
        self.osscl.workflowstep.set(workflowstep)
        return 'Workflow was created/updated successfully'

    def workflowstep__list(self, **args):
        q = dict()
        if args.get('filter'):
            q = json.loads(args.get('filter'))
        start = int(args.get('start')) if args.get('start') else 0
        size = int(args.get('max')) if args.get('max') else None
        return self.osscl.workflowstep.simpleSearch(q, start, size)

    def workflowstep__delete(self, **args):
        self.osscl.workflowstep.delete(int(args.get('id')))
        return 'Workflow was deleted successfully'

    def workflowstep__comment(self, **args):
        if args.get('id'):
            if not self.osscl.workflowstep.exists(int(args.get('id'))):
                return 'Workflow with ID %s was not found.' % args.get('id')
            workflowstep = self.osscl.workflowstep.get(int(args.get('id')))
        elif args.get('name'):
            workflowstep = self.osscl.workflowstep.simpleSearch({'name': args.get('name')})
            if workflowstep:
                workflowstep = self.osscl.workflowstep.get(workflowstep[0]['id'])
            else:
                return 'Workflow with name %s can not be found' % args.get('name')
        else:
            return 'Workflow ID or name must be passed'
        comment = workflowstep.new_comment()
        comment.comment = args.get('comment')
        comment.time = args.get('created')
        comment.author = args.get('author')
        self.osscl.workflowstep.set(workflowstep)
        return 'Workflow comment was added successfully'

    def job__create(self, **args):
        if args.get('id'):
            if not self.osscl.job.exists(int(args.get('id'))):
                return 'Job with ID %s was not found.' % args.get('id')
            job = self.osscl.job.get(int(args.get('id')))
        else:
            job = self.osscl.job.new()
        jobdata = job.dump()
        for arg in args:
            if arg in jobdata:
                if arg == 'workflow':
                    workflow = args.get('workflow')
                    nativequery={'$or':[{'id':workflow}, {'name':workflow}]}
                    workflow = self.osscl.jobstep.simpleSearch({}, nativequery=nativequery)
                    job.workflow = workflow[0]['id'] if workflow else job.workflow
                else:
                    jobdata[arg] = args.get(arg)
        job.dict2obj(jobdata)
        self.osscl.job.set(job)
        return 'Job was created/updated successfully'

    def job__list(self, **args):
        q = dict()
        if args.get('filter'):
            q = json.loads(args.get('filter'))
        start = int(args.get('start')) if args.get('start') else 0
        size = int(args.get('max')) if args.get('max') else None
        return self.osscl.job.simpleSearch(q, start, size)

    def job__delete(self, **args):
        self.osscl.job.delete(int(args.get('id')))
        return 'Job was deleted successfully'

    def jobstep__create(self, **args):
        if args.get('id'):
            if not self.osscl.jobstep.exists(int(args.get('id'))):
                return 'Jobstep with ID %s was not found.' % args.get('id')
            jobstep = self.osscl.jobstep.get(int(args.get('id')))
        else:
            jobstep = self.osscl.jobstep.new()
        jobstepdata = jobstep.dump()
        for arg in args:
            if arg in jobstepdata:
                if arg == 'workflowstep':
                    workflowstep = args.get('workflowstep')
                    nativequery={'$or':[{'id':workflowstep}, {'name':workflowstep}]}
                    workflowstep = self.osscl.workflowstep.simpleSearch({}, nativequery=nativequery)
                    jobstep.workflowstep_id = workflowstep[0]['id'] if workflowstep else jobstep.workflowstep
                else:
                    jobstepdata[arg] = args.get(arg)
        jobstep.dict2obj(jobstepdata)
        self.osscl.jobstep.set(jobstep)
        return 'Jobstep was created/updated successfully'

    def jobstep__list(self, **args):
        q = dict()
        if args.get('filter'):
            q = json.loads(args.get('filter'))
        start = int(args.get('start')) if args.get('start') else 0
        size = int(args.get('max')) if args.get('max') else None
        return self.osscl.jobstep.simpleSearch(q, start, size)

    def jobstep__delete(self, **args):
        self.osscl.jobstep.delete(int(args.get('id')))
        return 'Jobstep was deleted successfully'

    def jobstep__comment(self, **args):
        if args.get('id'):
            if not self.osscl.jobstep.exists(int(args.get('id'))):
                return 'Jobstep with ID %s was not found.' % args.get('id')
            jobstep = self.osscl.jobstep.get(int(args.get('id')))
        elif args.get('name'):
            jobstep = self.osscl.jobstep.simpleSearch({'name': args.get('name')})
            if jobstep:
                jobstep = self.osscl.jobstep.get(jobstep[0]['id'])
            else:
                return 'Jobstep with name %s can not be found' % args.get('name')
        else:
            return 'Jobstep ID or name must be passed'
        comment = jobstep.new_comment()
        comment.comment = args.get('comment')
        comment.time = args.get('created')
        comment.author = args.get('author')
        self.osscl.jobstep.set(jobstep)
        return 'Jobstep comment was added successfully'