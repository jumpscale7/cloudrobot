
- create (c,n,new)
-- name           #domain
-- id
-- description
-- companyname    #optional name
-- parent         #organization can belong to other organization
-- parent_name
-- addresses      #reference to addresses (guid)
-- contactmethods #reference to contactmethod (guid)
-- vatnr
-- datasources    #source(s) where data comes from (reference)
-- acl            #dict where key is name of group; value is R/W/E (E=Execute)
-- comments       #reference to comments

- update (u)
-- guid
-- name           #domain
-- id
-- description
-- companyname    #optional name
-- parent         #organization can belong to other organization
-- parent_name
-- addresses      #reference to addresses (guid)
-- contactmethods #reference to contactmethod (guid)
-- vatnr
-- datasources    #source(s) where data comes from (reference)
-- acl            #dict where key is name of group; value is R/W/E (E=Execute)
-- comments       #reference to comments

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
-- guid           #optional,guid gets priority if specified
-- name           #optional, last priority if specified (id & guid before)
-- id             #optional
-- format                 #default robot format (other supported formats are json & yaml)

- delete (d,del)
-- guid           #optional,guid gets priority if specified
-- name           #optional, last priority if specified (id & guid before)
-- id             #optional

- comment
-- guid           #optional,guid gets priority if specified
-- name           #optional, last priority if specified (id & guid before)
-- id             #optional
-- comment
-- created
-- author

- acl
-- guid           #optional,guid gets priority if specified
-- name           #optional, last priority if specified (id & guid before)
-- id             #optional
-- acl                   #as tags 'admin:RW guest:R'

        