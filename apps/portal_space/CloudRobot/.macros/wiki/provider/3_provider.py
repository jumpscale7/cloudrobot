def main(j, args, params, tags, tasklet):

    doc = args.doc

    providerid = int(args.getTag('id'))

    if providerid == None:
        out = 'Missing parameter'
        params.result = (out, doc)
        return params

    import JumpScale.lib.cloudrobots
    j.servers.cloudrobot.init()
    
    provider = j.servers.cloudrobot.osis.get('robot', 'provider', providerid)

    args.doc.applyTemplate(provider)
    params.result = (args.doc, args.doc)
    return params


def match(j, args, params, tags, tasklet):
    return True
