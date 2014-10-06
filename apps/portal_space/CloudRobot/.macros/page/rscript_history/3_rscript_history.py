
def main(j, args, params, tags, tasklet):

    page = args.page
    modifier = j.html.getPageModifierGridDataTables(page)

    filters = dict()
    for tag, val in args.tags.tags.iteritems():
        val = args.getTag(tag)
        if j.basetype.integer.checkString(val):
            val = int(val)
        filters[tag] = val

    fieldnames = ['ID', 'Name', 'Content', 'Type', 'Description', 'Modification Time', 'User']
    fieldvalues = ['id', 'name', 'content', 'channel', 'descr', 'modtime', 'user']
    fieldids = ['id',  'name', 'content', 'channel', 'descr', 'modtime', 'user']
    tableid = modifier.addTableForModel('robot', 'rscript_history', fieldids, fieldnames, fieldvalues, filters=filters)
    modifier.addSearchOptions('#%s' % tableid)

    params.result = page
    return params


def match(j, args, params, tags, tasklet):
    return True
