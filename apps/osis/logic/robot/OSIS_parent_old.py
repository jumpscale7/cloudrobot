from JumpScale import j
from JumpScale.grid.osis.OSISStore import OSISStore
ujson = j.db.serializers.getSerializerType('j')
import imp
import pymongo
from pymongo import MongoClient
import JumpScale.baselib.redisworker

class mainclass(OSISStore):

    """
    Default object implementation
    """

    def _getDB(self):
        raise RuntimeError("Not Implemented")

    def init(self, path, namespace,categoryname):
        """
        gets executed when catgory in osis gets loaded by osiscmds.py (.init method)
        """
        self.initall( path, namespace,categoryname,db=False)

        client = MongoClient()
        self.db=client[namespace]
        self.client=self.db[categoryname]
        self.counter=self.db["counter"]

        seq= {"_id": categoryname,"seq": 0}
        if self.counter.find_one({'_id': categoryname})==None:
            self.counter.save(seq)
        
    def _getObjectId(self,id):
        return pymongo.mongo_client.helpers.bson.objectid.ObjectId(id)

    def incrId(self):
        self.counter.update({'_id': self.categoryname},{"$inc": { "seq": 1 }})
        seq=self.counter.find_one({'_id': self.categoryname})
        return seq["seq"]

    def set(self, key, value,**args):
        """
        value can be a dict or a raw value (seen as string)
        """

        if j.basetype.dictionary.check(value):
            obj=None

            objInDB=None

            if value.has_key("id") and int(value["id"])<>0:                
                objInDB=self.client.find_one({"id":value["id"]}) 

            elif value.has_key("guid") and value["guid"]<>"":                
                value["guid"]=value["guid"].replace("-","")
                objInDB=self.client.find_one({"guid":value["guid"]}) 

            if objInDB<>None:
                # value["_id"]=
                # value.pop("guid")

                objInDB.update(value)
                # objInDB.pop("guid")
                objInDB["guid"]=objInDB["guid"].replace("-","")
                res=self.client.save(objInDB)
                new=False
                return (new,True,objInDB["guid"])
            
            new=True
            value["guid"]=value["guid"].replace("-","")
            if value.has_key("id") and int(value["id"])==0:
                value["id"]=self.incrId()


            res=self.client.save(value)
            
            return (new,True,value["guid"])
        else:
            raise RuntimeError("value can only be dict")

    def get(self, key):
        if j.basetype.string.check(key):
            key=key.replace("-","")
            res=self.client.find_one({"guid":key})
        else:
            res=self.client.find_one({"id":key})

        # res["guid"]=str(res["_id"])
        if res<>None:
            res.pop("_id")
        return res
        
    def exists(self, key):
        """
        get dict value
        """
        # oid=pymongo.mongo_client.helpers.bson.objectid.ObjectId(key)
        if j.basetype.string.check(key):
            return not self.client.find_one({"guid":key})==None
        else:
            return not self.client.find_one({"id":key})==None

    def index(self, obj,ttl=0,replication="sync",consistency="all",refresh=True):
        return

    def delete(self, key):
        if j.basetype.string.check(key):
            key=key.replace("-","")
            res=self.client.find_one({"guid":key})
        else:
            res=self.client.find_one({"id":key})
        if res<>None:
            self.client.remove(res["_id"])
        
    def deleteIndex(self, key,waitIndex=False,timeout=1):           
        pass

    def removeFromIndex(self, key,replication="sync",consistency="all",refresh=True):
        pass

    def find(self, query, start=0, size=200):        
        if size==None:
            size=200
        sortlist=[]
        if j.basetype.string.check(query):
            tags=j.core.tags.getObject(query)
            sort=None
            if tags.tagExists("@sort"):
                sort=tags.tagGet("@sort")
                tags.tagDelete("@sort")
                for item in sort.split(","):
                    item=item.strip()
                    if item=="":
                        continue
                    if item[0]=="-":
                        item=item.strip("-")
                        sortlist.append((item,-1))
                    else:
                        sortlist.append((item,1))


            if tags.tagExists("@size"):
                size=int(tags.tagGet("@size"))
                tags.tagDelete("@size")

            if tags.tagExists("@start"):
                start=int(tags.tagGet("@start"))
                tags.tagDelete("@start")            

            fields=None
            if tags.tagExists("@fields"):
                fields=tags.tagGet("@fields")
                tags.tagDelete("@fields")
                fields=[item.strip() for item in fields.split(",") if item.strip()<>""]

            params=tags.getDict()
            
            result=[]
            for item in self.client.find(params,limit=size,skip=start,fields=fields,sort=sortlist):
                item.pop("_id")
                result.append(item)
            return result
        else:
            mongoquery = dict()
            query.setdefault('query', {'bool':{'must':{}}})
            query['query']['bool'].setdefault('should', {})
            query['query']['bool'].setdefault('must', {})
            for queryitem in query['query']['bool']['must']:
                if 'term' in queryitem:
                    for k, v in queryitem['term'].iteritems():
                        mongoquery[k] = v
                if 'range' in queryitem:
                    for k, v in queryitem['range'].iteritems():
                        operatormap = {'from':'$gte', 'to':'$lte'}
                        for operator, val in v.iteritems():
                            mongoquery[k] = {operatormap[operator]: val}
                if 'wildcard' in queryitem:
                    for k, v in queryitem['wildcard'].iteritems():
                        mongoquery[k] = {'$regex': '.*%s.*' % str(v).replace('*', '')}


            wilds = dict()
            mongoquery['$or'] = list()
            for queryitem in query['query']['bool']['should']:
                if 'wildcard' in queryitem:
                    for k, v in queryitem['wildcard'].iteritems():
                        wilds[k] = {'$regex': '.*%s.*' % str(v).replace('*', '')}
                        mongoquery['$or'].append(wilds)

            if not mongoquery['$or']:
                mongoquery.pop('$or')

            start = int(start)
            size = int(size)
            if 'sort' in query:
                sorting = list()
                for field in query['sort']:
                    sorting.append((field.keys()[0], 1 if field.values()[0] == 'asc' else -1))
                resultdata = self.client.find(mongoquery).sort(sorting).skip(start).limit(size)
            else:
                resultdata = self.client.find(mongoquery).skip(start).limit(size)

            count = self.client.find(mongoquery).count()
            result = [count, ]
            for item in resultdata:
                item.pop("_id")
                result.append(item)
            return result

    def destroyindex(self):
        pass

    def deleteSearch(self,query):
        if not j.basetype.string.check(update):
            raise RuntimeError("not implemented")
        query+=' @fields:guid'
        counter=0
        for item in self.find(query=query):
            self.delete(item["guid"])
            counter+=1
        return counter
        
    def updateSearch(self,query,update):
        """
        update is dict or text
        dict e.g. {"name":aname,nr:1}  these fields will be updated then
        text e.g. name:aname nr:1
        """
        if not j.basetype.string.check(query):
            raise RuntimeError("not implemented")
        if j.basetype.string.check(update):
            tags=j.core.tags.getObject(update)
            update=tags.getDict()            
        # self.client.find_and_modify(query,update=update)
        query+=' @fields:guid'
        counter=0
        for item in self.find(query=query):
            update["guid"]=item["guid"]
            self.set(value=update)
            counter+=1
            
        return counter

    def destroy(self):
        """
        delete objects as well as index (all)
        """
        self.client.drop()
        self.rebuildindex()

    def demodata(self):
        path=j.system.fs.joinPaths(self.path,"demodata.py")
        if j.system.fs.exists(path):
            module = imp.load_source("%s_%s_demodata"%(self.namespace,self.categoryname), path)    
            job=j.clients.redisworker.execFunction(module.populate,_organization=self.namespace,_category=self.categoryname,_timeout=60,_queue="io",_log=True,_sync=False)

    def list(self, prefix="", withcontent=False):
        """
        return all object id's stored in DB
        """
        from IPython import embed
        print "DEBUG NOW list"
        embed()
        

    def rebuildindex(self):
        path=j.system.fs.joinPaths(self.path,"index.py")
        if j.system.fs.exists(path):
            module = imp.load_source("%s_%sindex"%(self.namespace,self.categoryname), path)
            module.index(self.client)

    def export(self, outputpath):
        """
        export all objects of a category to json format.
        Placed in outputpath
        """
        from IPython import embed
        print "DEBUG NOW export"
        embed()
        
        if not j.system.fs.isDir(outputpath):
            j.system.fs.createDir(outputpath)
        ids = self.list()
        for id in ids:
            obj = self.get(id)
            filename = j.system.fs.joinPaths(outputpath, id)
            if isinstance(obj, dict):
                obj = json.dumps(obj)
            j.system.fs.writeFile(filename, obj)

    def importFromPath(self, path):
        from IPython import embed
        print "DEBUG NOW import"
        embed()
        
        '''Imports OSIS category from file system'''
        if not j.system.fs.exists(path):
            raise RuntimeError("Can't find the specified path: %s" % path)

        data_files = j.system.fs.listFilesInDir(path)
        for data_file in data_files:
            with open(data_file) as f:
                obj = json.load(f)
            self.set(obj['guid'], obj)
