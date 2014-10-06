
def main(j, args, params, tags, tasklet):

    page = args.page
    modifier = j.html.getPageModifierGridDataTables(page)

    filters = dict()
    for tag, val in args.tags.tags.iteritems():
        val = args.getTag(tag)
        if j.basetype.integer.checkString(val):
            val = int(val)
        filters[tag] = val

    fieldnames = ['ID', 'Name', 'Type', 'Location']
    fieldvalues = ['[%(id)s|/cloudrobot/provider?id=%(id)s]', 'name', 'type', 'location']
    fieldids = ['id', 'name', 'type', 'location']
    tableid = modifier.addTableForModel('robot', 'provider', fieldids, fieldnames, fieldvalues, filters=filters)
    modifier.addSearchOptions('#%s' % tableid)

    params.result = page
    return params


def match(j, args, params, tags, tasklet):
    return True
