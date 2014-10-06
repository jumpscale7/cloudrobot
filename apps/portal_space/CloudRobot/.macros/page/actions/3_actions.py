
def main(j, args, params, tags, tasklet):

    page = args.page
    modifier = j.html.getPageModifierGridDataTables(page)

    filters = dict()
    for tag, val in args.tags.tags.iteritems():
        val = args.getTag(tag)
        if j.basetype.integer.checkString(val):
            val = int(val)
        filters[tag] = val

    fieldnames = ['ID', 'Name', 'RScript Name', 'RScript Channel', 'State']
    fieldvalues = ['[%(id)s|/cloudrobot/action?id=%(id)s]', 'name', 'rscript_name', 'rscript_channel', 'state']
    fieldids = ['id', 'name', 'rscript_name', 'rscript_channel', 'state']
    tableid = modifier.addTableForModel('robot', 'action', fieldids, fieldnames, fieldvalues, filters=filters)
    modifier.addSearchOptions('#%s' % tableid)

    params.result = page
    return params


def match(j, args, params, tags, tasklet):
    return True
