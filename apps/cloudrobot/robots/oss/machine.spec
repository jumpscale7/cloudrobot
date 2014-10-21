
- create (c,n,new)
-- id
-- name
-- organization      #id of organization which owns the machine if any
-- organization_name
-- label
-- parent
-- parent_name
-- description
-- type
-- interfaces
-- depends           # link to other machines (what does it need to work)
-- depends_names
-- assethost         #who is asset hosting this machinehost
-- memory            #in GB
-- ssdcapacity       #in GB
-- hdcapacity        #in GB
-- cpumhz            #in mhz
-- nrcores
-- nrcpu
-- rootpasswd        #encrypted root passwd
-- acl               #dict where key is name of group; value is R/W/E (E=Execute)
-- comments          #reference to comments

- update (u)
-- guid
-- id
-- name
-- organization      #id of organization which owns the machine if any
-- organization_name
-- label
-- parent
-- parent_name
-- description
-- type
-- interfaces
-- depends           # link to other machines (what does it need to work)
-- depends_names
-- assethost         #who is asset hosting this machinehost
-- memory            #in GB
-- ssdcapacity       #in GB
-- hdcapacity        #in GB
-- cpumhz            #in mhz
-- nrcores
-- nrcpu
-- rootpasswd        #encrypted root passwd
-- acl               #dict where key is name of group; value is R/W/E (E=Execute)
-- comments          #reference to comments

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
-- guid              #optional,guid gets priority if specified
-- id                #optional
-- name              #optional, last priority if specified (id & guid before)
-- format                 #default robot format (other supported formats are json & yaml)

- delete (d,del)
-- guid              #optional,guid gets priority if specified
-- id                #optional
-- name              #optional, last priority if specified (id & guid before)

- comment
-- guid              #optional,guid gets priority if specified
-- id                #optional
-- name              #optional, last priority if specified (id & guid before)
-- comment
-- created
-- author

- acl
-- guid              #optional,guid gets priority if specified
-- id                #optional
-- name              #optional, last priority if specified (id & guid before)
-- acl                   #as tags 'admin:RW guest:R'

        