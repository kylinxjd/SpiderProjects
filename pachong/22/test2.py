import pymongo

client = pymongo.MongoClient("127.0.0.1", 27017)
db = client['spider']
coll = db['suning']

coll.insert({'name':'asd'})