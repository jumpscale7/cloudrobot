def main(j, args, params, tags, tasklet):

    doc = args.doc

    machineresourceid = int(args.getTag('id'))

    if machineresourceid == None:
        out = 'Missing parameter'
        params.result = (out, doc)
        return params

    rcl = j.core.osis.getClientForNamespace('robot')
    machineresource = rcl.resourcemachine.get(machineresourceid)
    machineresource = machineresource.dump()
    
    args.doc.applyTemplate(machineresource)
    params.result = (args.doc, args.doc)
    return params


def match(j, args, params, tags, tasklet):
    return True
