

import pymongo

myclient = pymongo.MongoClient("mongodb+srv://test:test@cluster0.kw4id.mongodb.net/collection?retryWrites=true&w=majority")
mydb = myclient["mydatabase"]
mycol = mydb["update"]

"""
mydict = { "name": "Tom", "address": "Bhubaneswar" }

x = mycol.insert_one(mydict)
"""


myquery = { "address": "Bhubaneswar" }
newvalues = { "$set": { "address": "Bhadrak" } }

myquery = { "address": { "$regex": "^B" } }
newvalues = { "$set": { "name": "Siddharth" } }

mycol.update_one(myquery, newvalues)

#print "customers" after the update:
for x in mycol.find():
  print(x)



