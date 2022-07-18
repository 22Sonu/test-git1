import pymongo

client = pymongo.MongoClient("mongodb+srv://ineuron:sonu@cluster0.qhdrec2.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

db1= client['mongotest']
coll= db1['test']
#coll.insert_one(d)

