def main(j, args, params, tags, tasklet):

    doc = args.doc

    jobid = int(args.getTag('id'))

    if jobid == None:
        out = 'Missing parameter'
        params.result = (out, doc)
        return params

    import JumpScale.lib.cloudrobots
    j.servers.cloudrobot.init()

    job = j.servers.cloudrobot.osis_robot_job.get(jobid)
    job = job.dump()
    
    for k in ['start', 'end', 'lastmod']:
        job[k] = j.base.time.epoch2HRDateTime(job[k])

    args.doc.applyTemplate(job)
    params.result = (args.doc, args.doc)
    return params


def match(j, args, params, tags, tasklet):
    return True
