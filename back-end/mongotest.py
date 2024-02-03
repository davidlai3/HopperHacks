from pymongo import MongoClient

class User:
    def __init__(self, name, gender, age, email, password):
        self.name = name
        self.gender = gender
        self.age = age
        self.email = email
        self.password = password
    def __str__(self):
        return f"{self.name}, {self.gender}, {self.age}, {self.email}"

client = MongoClient("mongodb+srv://davidlai3:sdfghj45@cluster0.3eutqra.mongodb.net/?retryWrites=true&w=majority")
db = client.Users
info = db.UserInfo

u1 = User("Jane", "F", 25, "janedoe@yahoo.com", "123456")

def insert_user(user):
    info.insert_one(user.__dict__)

insert_user(u1)



