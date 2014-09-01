
def main(j, args, params, tags, tasklet):

    doc = args.doc

    filters = dict()
    for tag, val in args.tags.tags.iteritems():
        val = args.getTag(tag)
        if j.basetype.integer.checkString(val):
            val = int(val)
        filters[tag] = val

    import JumpScale.lib.cloudrobots
    j.servers.cloudrobot.init()
    out = ['||Name||User ID||Channel||Modification Date||Jobs||']

    users = j.servers.cloudrobot.osis_system_user.list()
    for user in users:
        userid, name = user.split('_')
        session = j.servers.cloudrobot.sessionGet(userid, name)
        out.append('|[%s|/cloudrobot/session?name=%s&userid=%s]|%s|%s|%s|%s|' % (session.name, session.name, session.userid, session.userid, session.channel, session.moddate, session.jobs))

    out = '\n'.join(out)

    params.result = (out, doc)
    return params


def match(j, args, params, tags, tasklet):
    return True
