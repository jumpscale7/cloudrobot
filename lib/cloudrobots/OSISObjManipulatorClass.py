from JumpScale import j

def OSISObjManipulatorClass():
    
    def __init__(self):        
        self.model=None
        self.spec=None

    def _objGetFromArgs(self,args={}):
        if args.has_key("guid"):
            obj=self.trigger_get(obj.guid)
        elif args.has_key("id"):
            obj=self.model.get(id="id")
        elif args.has_key("name"):
            res=self.model.simpleSearch({"name":name})
            if len(res)==1:
                guid=res["guid"]
                obj=self.model.get(guid=guid)
            elif len(res)>1:
                self.raiseError(obj,"found more than 1 obj.")
            else:
                self.raiseError(obj,"Did not find obj.")
        return obj

    def _objFromArgs(self,new=True, args={},obj=None):
        if obj==None:
            if new:
                obj = self.model.new()
            else:
                obj=self._objGetFromArgs(args)

        objdata = obj.dump()
        for arg in args:
            if arg in objdata:
                if arg == 'acl':
                    tags = j.core.tags.getObject(args.get('acl'))
                    objdata['acl'] = tags.getDict() if tags.getDict() else objdata['acl']
                else:
                    objdata[arg] = args.get(arg)
        obj.dict2obj(objdata)

    def create(self, **args):
        obj=self._objFromArgs(new=True,args=args)
        self.trigger_set(obj,args)
        return 'obj was added successfully'

    def duplicate(self, **args):
        obj=self._objGetFromArgs(args)
        if obj.__dict__.has_key("id"):
            obj.__dict__.pop("id")
        if obj.__dict__.has_key("guid"):
            obj.__dict__.pop("guid")
        if args.has_key("id"):
            args.pop("id")
        if args.has_key("guid"):
            args.pop("guid")        
        obj=self._objFromArgs(new=False,args=args,obj=obj)
        self.trigger_set(ob,args)
        return 'obj was duplicated successfully'

    def update(self, **args):
        obj=self._objFromArgs(new=False,args=args)
        self.trigger_set(obj,args)
        return 'obj was updated successfully'

    def trigger_set(self,obj,args):        
        """
        overrule this method to do some business logic when setting or after setting
        """
        self.model.set(obj)

    def get(self,**args):
        obj=self._objFromArgs(new=False,args=args)
        obj = obj.dump()
        out = 'obj:\n'
        for k, v in obj.iteritems():
            out += '%s: %s\n' % (k, v)
        return out

    def list(self, **args):
        maximum = args.get('max')
        start = args.get('start', 0)
        query = json.loads(args.get('filter', "{}"))
        objs = self.model.simpleSearch(query, size=maximum, start=start)
        result = list()
        verbose = int(args.get('verbose'), 3)
        out=""
        for obj in objs:
            out+="%s\n"%trigger_list(obj)
        return out

    def trigger_list(self,obj):
        """
        overrule this method to list other properties (this is called per item in the list, when return None then will not be shown)
        return what needs to be returned to user who called robot (per line)
        """
        out="%-7s %-15s %-10s %s"%(obj.id,obj.name,obj.description,obj.type)
        return out

    def delete(self, **args):
        obj=self._objGetFromArgs(args)
        self.trigger_delete(obj)
        return 'obj was deleted successfully'

    def trigger_delete(self,obj):
        """
        overrule this method to list other properties (this is called per item in the list, when return None then will not be shown)
        return what needs to be returned to user who called robot (per line)
        """
        self.model.delete(obj.guid)

    def comment(self, **args):
        obj=self._objGetFromArgs(args)
        #@todo is new code now !!!
        comment = obj.new_comment()
        comment.comment = args.get('comment')
        comment.time = args.get('created')
        comment.author = args.get('author')
        self.model.set(obj)
        return 'obj comment was added successfully'

    def acl_set(self, **args):
        obj=self._objGetFromArgs(args)
        #@todo is new code now !!!
        comment = obj.new_comment()
        comment.comment = args.get('comment')
        comment.time = args.get('created')
        comment.author = args.get('author')
        self.model.set(obj)
        return 'obj acl was set successfully'

    def acl_get(self, **args):
        obj=self._objGetFromArgs(args)
        #@todo is new code now !!!
        comment = obj.new_comment()
        comment.comment = args.get('comment')
        comment.time = args.get('created')
        comment.author = args.get('author')
        self.model.set(obj)
        return 'obj acl was set successfully'
