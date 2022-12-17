import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["CRUD_operations"]
mycol = mydb["CRUD"]


myquery={"city":"Phoenix"}

mydoc=mycol.delete_one(myquery)
for y in mycol.find():
    print(y)