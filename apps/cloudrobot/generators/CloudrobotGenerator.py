from JumpScale import j
# import ujson as json
import yaml

class CloudrobotGenerator():
    def __init__(self,dest):
        self.dest=dest
        j.system.fs.createDir(j.system.fs.getDirName(self.dest))
        self.longest=0

    def generate(self,spec):

        
        for modelname in spec.keys():
            spec2=spec[modelname]
            out=self.generateSpec(modelname,spec2)
            destpath="%s/%s.gen.spec"%(self.dest,modelname)
            j.system.fs.writeFile(filename=destpath,contents=out)
            destpath="%s/%s.spec"%(self.dest,modelname)
            if not j.system.fs.exists(path=destpath):
                j.system.fs.writeFile(filename=destpath,contents=out)

        for modelname in spec.keys():
            spec2=spec[modelname]
            out=self.generateRobotCode(modelname,spec2)
            destpath="%s/%s.gen.py"%(self.dest,modelname)
            j.system.fs.writeFile(filename=destpath,contents=out)
            destpath="%s/%s.py"%(self.dest,modelname)
            if True or not j.system.fs.exists(path=destpath):
                j.system.fs.writeFile(filename=destpath,contents=out)

    def pad(self,txt,llen):
        while len(txt)<llen:
            txt+=" "
        return txt

    def add(self,previous,name,descr):
        if descr<>"":
            previous+="-- %s #%s\n"%(self.pad(name,self.longest),descr)
        else:
            previous+="-- %s\n"%name
        return previous

    def generateSpec(self,name,modelspec):
        classname="%s_%s"%(modelspec["actorname"],name)
        # out="%s ():\n\n"%classname
        out=""
        
        self.longest=0
        for propspec in modelspec["properties"]:
            name=propspec["name"].lower().strip()
            if len(name)>self.longest:
                self.longest=len(name)

        #generate the list of fields
        fieldlist=""
        idlist=self.add("","guid","optional,guid gets priority if specified")
        for propspec in modelspec["properties"]:
            name=propspec["name"].lower().strip()

            if name=="guid":
                continue

            if name=="id":
                idlist=self.add(idlist,"id","optional")
            elif name=="name":
                idlist=self.add(idlist,"name","optional, last priority if specified (id & guid before)")

            descr=propspec["description"]
            if descr==None:
                descr=""
            if len(descr)>100:
                descr=descr[:100]

            default=propspec["default"]
            if default==None:
                default=""

            if default<>"":
                descr+=" (default:%s)"%default

            fieldlist=self.add(fieldlist,name,descr)
            guid=self.add("","guid","")

        TEMPL="""
- create (c,n,new)
$fieldlist

- update (u)
$guid
$fieldlist

- export                  #produce text which will allow import
-- filter (f)             #is filter which is mongodb querystr
-- format                 #if verbose=3: std json (can also yaml) otherwise this arg is not valid

- list (l)
-- max                    #max amount of items
-- start                  #startpoint e.g. 10 is id
-- filter (f)             #is filter which is mongodb querystr in tag format e.g. org:myorg country:belgium price:<10
-- sort (s)               #comma separated list of sort (optional)
-- fields                 #comma separated list of fields to show (optional)

- get                     #produces txt which can be used by robot to input 
$idlist
-- format                 #default robot format (other supported formats are json & yaml)

- delete (d,del)
$idlist

- comment
$idlist
-- comment
-- created
-- author

- acl
$idlist
-- acl                   #as tags 'admin:RW guest:R'

        """

        TEMPL=TEMPL.replace("$fieldlist",fieldlist.strip())
        TEMPL=TEMPL.replace("$idlist",idlist.strip())
        TEMPL=TEMPL.replace("$guid",guid.strip())

        out+=TEMPL

        return out


    def spec2newformat(self,modelspec):
        newspec={}
        newspec["model"]=[]

        longest=0
        for propspec in modelspec["properties"]:
            name=propspec["name"].lower().strip()
            if len(name)>longest:
                longest=len(name)
        newspec["propname_longest"]=longest

        for propspec in modelspec["properties"]:
            name=propspec["name"].lower().strip()

            if name=="guid":
                continue

            descr=propspec["description"]
            if descr==None:
                descr=""
            # if len(descr)>100:
            #     descr=descr[:100]

            default=propspec["default"]
            if default==None:
                default=""

            item={}
            item["name"]=name
            item["descr"]=descr
            item["default"]=default
            item["tags"]=descr            


            tags=j.core.tags.getObject(item["tags"])

            # if item["tags"]<>None and item["tags"].strip()<>"":

            #     if str(tags).find("ref")<>-1:
            #         from IPython import embed
            #         print "DEBUG NOW id"
            #         embed()                
            

            item["optional"]=tags.labelExists("option") or tags.labelExists("optional")

            item["islist"]=propspec["type"].find("list")==0
            item["isdict"]=propspec["type"].find("dict")==0

            item["type"]=propspec["type"]
            item["type"]=item["type"].replace("list(","")
            item["type"]=item["type"].replace("dict(","")
            item["type"]=item["type"].strip().strip(")").strip()


            newspec["model"].append(item)

        return newspec


    def generateRobotCode(self,name,modelspec):
        # spec=json.dumps(modelspec)

        spec=yaml.dump(self.spec2newformat(modelspec))


        TEMPL="""
from JumpScale import j
import yaml
import JumpScale.grid.osis
import JumpScale.lib.cloudrobots

OSISObjManipulatorClass=j.cloudrobot.getOSISObjManipulatorClass()

def Cmds(OSISObjManipulatorClass):
    
    def __init__(self):    
        self.osisclient = j.core.osis.getClientForNamespace('$actorname')    
        self.model=self.osisclient.$name
        self.spec=\"\"\"
$spec        
\"\"\" 
        self.spec=yaml.load(self.spec)       

    def trigger_set(self,obj,args):        
        \"\"\"
        overrule this method to do some business logic when setting or after setting
        \"\"\"
        self.model.set(obj)

    def trigger_delete(self,obj):
        \"\"\"
        overrule this method to list other properties (this is called per item in the list, when return None then will not be shown)
        return what needs to be returned to user who called robot (per line)
        \"\"\"
        self.model.delete(obj.guid)

    def trigger_list(self,obj):
        \"\"\"
        overrule this method to list other properties (this is called per item in the list, when return None then will not be shown)
        return what needs to be returned to user who called robot (per line)
        \"\"\"
        out="%-7s %-15s %-10s %s"%(obj.id,obj.name,obj.description,obj.type)
        return out
                      

        """

        TEMPL=TEMPL.replace("$name",name)
        TEMPL=TEMPL.replace("$spec",spec)
        TEMPL=TEMPL.replace("$actorname",modelspec["actorname"])
    

        return TEMPL

