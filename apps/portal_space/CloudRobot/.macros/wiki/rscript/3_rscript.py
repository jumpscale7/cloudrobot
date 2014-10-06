def main(j, args, params, tags, tasklet):

    doc = args.doc

    rscriptid = int(args.getTag('id'))

    if rscriptid == None:
        out = 'Missing parameter'
        params.result = (out, doc)
        return params

    rcl = j.core.osis.getClientForNamespace('robot')
    rscript = rcl.rscript.get(rscriptid)
    rscript = rscript.dump()

    args.doc.applyTemplate(rscript)
    params.result = (args.doc, args.doc)
    return params


def match(j, args, params, tags, tasklet):
    return True
