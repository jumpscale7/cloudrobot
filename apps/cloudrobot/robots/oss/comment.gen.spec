
- create (c,n,new)
-- comment
-- time        #epoch
-- author      # who created comment
-- author_name # who created comment
-- id          #Auto generated id @optional

- update (u)
-- guid
-- comment
-- time        #epoch
-- author      # who created comment
-- author_name # who created comment
-- id          #Auto generated id @optional

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
-- guid        #optional,guid gets priority if specified
-- id          #optional
-- format                 #default robot format (other supported formats are json & yaml)

- delete (d,del)
-- guid        #optional,guid gets priority if specified
-- id          #optional

- comment
-- guid        #optional,guid gets priority if specified
-- id          #optional
-- comment
-- created
-- author

- acl
-- guid        #optional,guid gets priority if specified
-- id          #optional
-- acl                   #as tags 'admin:RW guest:R'

        