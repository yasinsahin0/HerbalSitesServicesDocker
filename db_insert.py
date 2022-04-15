import couchdb


couch = couchdb.Server("http://admin:admin@172.105.73.62:5984/")

database = couch["products"]
doc = {"test": "test"}
database.save(doc)