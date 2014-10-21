from JumpScale import j

import mongoengine
from eve import Eve
from eve_mongoengine import EveMongoengine

from flask.ext.bootstrap import Bootstrap
from eve_docs import eve_docs

import JumpScale.grid.osis

client = j.core.osis.getClient(user='root')
spec=client.getOsisSpecModel("oss")

from generators.CloudrobotGenerator import *

# gen=MongoEngineGenerator("generated/oss.py")
# gen.generate(json)

gen=CloudrobotGenerator("robots/oss")
gen.generate(spec)

