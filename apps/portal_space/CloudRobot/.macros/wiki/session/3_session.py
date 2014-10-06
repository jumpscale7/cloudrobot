
def main(j, args, params, tags, tasklet):

    doc = args.doc

    # filters = dict()
    # for tag, val in args.tags.tags.iteritems():
    #     val = args.getTag(tag)
    #     if j.basetype.integer.checkString(val):
    #         val = int(val)
    #     filters[tag] = val
    userid = args.getTag('userid')
    name = args.getTag('name')

    if userid == None or name == None:
        out = 'Missing parameter'
        params.result = (out, doc)
        return params

    import JumpScale.lib.cloudrobots
    j.servers.cloudrobot.init()

    session = j.servers.cloudrobot.sessionGet(userid, name)
    session = session.__dict__
    session['moddate'] = j.base.time.epoch2HRDateTime(session['moddate'])
    session['retchannels'] = ' ,'.join(session['retchannels'])

    args.doc.applyTemplate(session)
    params.result = (args.doc, args.doc)
    return params


def match(j, args, params, tags, tasklet):
    return True
