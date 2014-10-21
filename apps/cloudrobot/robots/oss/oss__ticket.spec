ticket (issue,bug,feature,task,event,perfissue,check)

- create (c,n,new,update,u)
-- id
-- name
-- description
-- priority #0-4,4 being highest
-- project #reference to projectid or name
-- type #supported types: story;task;issue;event;bug;feature;ticket;perfissue,check
-- parent #specify part of name or id of task which we are subtask for
-- depends #specify part of name or id of task which we depend on, do comma separated if more than 1
-- duplicate #comma separated list of id's 
-- taskowner #name of person who will do it (email or username)
-- descr (description,d)
-- deadline
-- source #id or name or email of person who created the ticket
-- sprint #id or (part of name) name of sprint
-- organization #id or (part of name) name of organization
-- nextstep #epoch or time from now notation (e.g. +4d, +1m)
-- workflow #current workflow active
-- jobs #list of ids to jobs
-- job_status #values: PENDING,ACTIVE,ERROR,OK,WARNING,CRITICAL
-- time_created         #epoch
-- time_lastmessage     #epoch
-- time_lastresponse    #epoch
-- time_closed          #epoch
-- messages #reference to messages (comma separated)
-- comments #reference to comments (comma separated)
-- datasources #comma separated list of datasources e.g. osticket, ...
-- acl                  #as tags 'admin:RW guest:R'
-- params               #json repr of dict with args or as tags (if possible)

- export #produce list of ticket.create statements defined above
-- filter (f) #is filter which is query str for osis

- list (l)
-- max #max amount of items
-- start #startpoint e.g. 10 is id
-- filter (f) #is filter which is query str for osis
-- verbose (v) #1-3 3 being most verbose

- delete (d,del)
-- id

- comment
-- comment
-- created
-- author

- assign
-- id
-- taskowner

- duplicate
-- id

- get #produces full ticket statement, see above)
-- id

- message
-- id
-- ticketid
-- subject
-- message
-- destination #as comma separated
-- time #epoch
-- type #email;sms;gtalk;tel
-- format #html;confl;md;text default is text

- depend
-- id
-- name (n) #speciy name or part of name
-- on #depend on (speciy name or part of name or id)

- subtask
-- id
-- name (n) #speciy name or part of name (if id not used)
-- parent #parent of this task (speciy name or part of name or id)

- duplicate
-- id
-- name (n) #speciy name or part of name (if id not used) of ticket
-- duplicate #duplicate (speciy name or part of name or id)

