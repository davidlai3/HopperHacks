from pymongo import MongoClient


client = MongoClient("mongodb+srv://davidlai3:sdfghj45@cluster0.3eutqra.mongodb.net/?retryWrites=true&w=majority")
db = client.Users

post = {
    "author": "David",
    "text": "Testing testing 123"
}

info = db.UserInfo
info_id = info.insert_one(post).inserted_id
print(info_id)

