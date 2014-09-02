def main(j, args, params, tags, tasklet):

    doc = args.doc

    actionid = int(args.getTag('id'))

    if actionid == None:
        out = 'Missing parameter'
        params.result = (out, doc)
        return params

    import JumpScale.lib.cloudrobots
    j.servers.cloudrobot.init()

    action = j.servers.cloudrobot.osis_robot_action.get(actionid)
    action = action.dump()
    
    for k in ['start', 'end', 'lastmod']:
        action[k] = j.base.time.epoch2HRDateTime(action[k])

    args.doc.applyTemplate(action)
    params.result = (args.doc, args.doc)
    return params


def match(j, args, params, tags, tasklet):
    return True
