from JumpScale import j

from eve_mongoengine import EveMongoengine

import mongoengine

def Cmds():
    
    def __init__(self):        
        self.mongo=mongoengine.connect("osis")

    def create(self, **args):
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

    def list(self, **args):
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

    def delete(self, **args):
        self.osscl.ticketid.delete(int(args.get('id')))
        return 'Ticket was deleted successfully'

    def assign(self, **args):
        assignee = args.get('taskowner')
        ticket = self.osscl.ticket.get(int(args.get('id')))
        if not ticket:
            return 'No ticket with id "%s" was found' % args.get('id')
        ticket.taskowner = assignee
        self.osscl.ticket.set(ticket)
        return 'Ticket was updated successfully'

    def duplicate(self, **args):
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

    def depend(self, **args):
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

    def subtask(self,**args):
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

    def get(self,**args):
        id = args.get('id')
        ticket = self.osscl.ticket.get(id)
        if not ticket:
            return 'Ticket not found'
        ticket = ticket.dump()
        out = 'Ticket:\n'
        for k, v in ticket.iteritems():
            out += '%s: %s\n' % (k, v)
        return out

    def comment(self, **args):
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

    def message(self, **args):
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