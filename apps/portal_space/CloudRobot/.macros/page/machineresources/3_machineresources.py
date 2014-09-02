
def main(j, args, params, tags, tasklet):

    page = args.page
    modifier = j.html.getPageModifierGridDataTables(page)

    filters = dict()
    for tag, val in args.tags.tags.iteritems():
        val = args.getTag(tag)
        if j.basetype.integer.checkString(val):
            val = int(val)
        filters[tag] = val

    fieldnames = ['ID', 'Name', 'Provider', 'Location', 'IPv4', 'IPv6']
    fieldvalues = ['[%(id)s|/cloudrobot/machineresource?id=%(id)s]', 'name', 'provider', 'location', 'ipv4', 'ipv6']
    fieldids = ['id',  'name', 'provider', 'location', 'ipv4', 'ipv6']
    tableid = modifier.addTableForModel('robot', 'resourcemachine', fieldids, fieldnames, fieldvalues, filters=filters)
    modifier.addSearchOptions('#%s' % tableid)

    params.result = page
    return params


def match(j, args, params, tags, tasklet):
    return True
