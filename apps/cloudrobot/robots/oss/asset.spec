
- create (c,n,new)
-- id
-- organization       #id of organization which owns the asset if any
-- organization_names #comma separated list of name
-- label
-- parent
-- parent_name
-- description
-- type
-- brand
-- model
-- interfaces
-- components
-- depends            # link to other assets (what does it need to work)
-- depends_names
-- rack
-- datacenter_name
-- pod_name
-- rack_name
-- datacenter_label
-- pod_label
-- rack_label
-- u                  #how many U taken
-- rackpos            # how many U starting from bottomn
-- acl                #dict where key is name of group; value is R/W/E (E=Execute)
-- comments           #reference to comments

- update (u)
-- guid
-- id
-- organization       #id of organization which owns the asset if any
-- organization_names #comma separated list of name
-- label
-- parent
-- parent_name
-- description
-- type
-- brand
-- model
-- interfaces
-- components
-- depends            # link to other assets (what does it need to work)
-- depends_names
-- rack
-- datacenter_name
-- pod_name
-- rack_name
-- datacenter_label
-- pod_label
-- rack_label
-- u                  #how many U taken
-- rackpos            # how many U starting from bottomn
-- acl                #dict where key is name of group; value is R/W/E (E=Execute)
-- comments           #reference to comments

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
-- guid               #optional,guid gets priority if specified
-- id                 #optional
-- format                 #default robot format (other supported formats are json & yaml)

- delete (d,del)
-- guid               #optional,guid gets priority if specified
-- id                 #optional

- comment
-- guid               #optional,guid gets priority if specified
-- id                 #optional
-- comment
-- created
-- author

- acl
-- guid               #optional,guid gets priority if specified
-- id                 #optional
-- acl                   #as tags 'admin:RW guest:R'

        