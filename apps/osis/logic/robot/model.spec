[rootmodel:rscript] @index
    """
    """
    prop:name str,,
    prop:content str,,
    prop:channel str,,
    prop:descr str,,
    prop:secrets list(str),,

[rootmodel:rscript_history] @index
    """    
    """
    prop:name str,,
    prop:content str,,
    prop:channel str,,
    prop:descr str,,
    prop:modtime str,,
    prop:user str,,

[rootmodel:template] @index
    """
    info going back to customer
    """
    prop:name str,,
    prop:content str,,
    prop:channel str,,
    prop:secrets list(str),,

[rootmodel:job] @index
    prop:guid str,,
    prop:rscript_channel str,,
    prop:rscript_name str,,
    prop:rscript_content str,,
    prop:vars str,,
    prop:sessionid str,,
    prop:onetime bool,,if just an adhoc script executed once
    prop:userid str,,
    prop:state str,, (ERROR,OK,RUNNING,PENDING)
    prop:start int,,epoch of start
    prop:end int,,epoch when end of job
    prop:actions list(str),,actionguids
    prop:error str,,
    prop:out str,,

[rootmodel:action] @index
    prop:guid str,,
    prop:jobguid str,,
    prop:rscript_channel str,,
    prop:rscript_name str,,    
    prop:userid str,,
    prop:name str,,
    prop:code str,,
    prop:vars str,,
    prop:result str,,
    prop:out str,,
    prop:log str,,
    prop:state str,, (ERROR,OK,RUNNING,PENDING)
    prop:start int,,epoch of start
    prop:end int,,epoch when end of job
    prop:error str,,

[rootmodel:secrets] @index
    prop:user str,,
    prop:secrets str,,

[rootmodel:secrets] @index
    prop:user str,,
    prop:secrets str,,

[rootmodel:ace] @index
    prop:group str,,
    prop:right str,, today only A for access.

[rootmodel:provider] @index
    prop:name str,,
    prop:type str,,amazon;digitalocean;google;dedicated;ms1
    prop:location str,,free text to describe location
    prop:acl list(ace),,
    prop:descr str,,
    prop:acl list(ace),,
    prop:login str,,
    prop:secret str,,
    prop:params str,,json encode other set of parameters relevant to this provider

[rootmodel:resourcemachine] @index
    """
    can be virtual or physical
    """
    prop:name str,,
    prop:descr str,,
    prop:provider str,,
    prop:location str,,free text to describe location
    prop:acl list(ace),,
    prop:ipv4 str,,
    prop:ipv6 str,,
    prop:rootpasswd str,,
    prop:cpucores int,, is logical cores
    prop:cpumhz int,,e.g. 3400
    prop:ssd_size int,, in MB
    prop:disk_size int,, in MB
    prop:mem_size int,, in MB
    prop:cost int,,recalculated cost in eur per month
    prop:ssd_used int,,in MB
    prop:disk_used int,,in MB
    prop:mem_used int,,in MB
    prop:cpu_used list(int),,mhz used per core; core 0 is first in list
    prop:cost_distr_ssd int,,0-100 expresses percentage that ssd is of cost of node per month
    prop:cost_distr_disk int,,0-100 expresses percentage that disk is of cost of node per month
    prop:cost_distr_compute int,,0-100 expresses percentage that compute is of cost of node per month (is compbo of mem & cpu)


