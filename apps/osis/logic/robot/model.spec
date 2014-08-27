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
    prop:uid str,,
    prop:rscript_channel str,,
    prop:rscript_name str,,
    prop:rscript_content str,,
    prop:globals str,,
    prop:session str,,
    prop:onetime bool,,if just an adhoc script executed once
    prop:user str,,
    prop:result str,,
    prop:log str,,
    prop:state str,, (ERROR,OK,RUNNING,PENDING)
    prop:start int,,epoch of start
    prop:end int,,epoch when end of job

[rootmodel:secrets] @index
    prop:user str,,
    prop:secrets str,,

