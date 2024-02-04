from pymongo import MongoClient
import json

# Genres: Length 3
# Artists: Length 10
# Songs: Length 20
class User:
    def __init__(self, name, gender, age, country, email, genres, artists, songs):
        self.name = name
        self.gender = gender
        self.age = age
        self.country = country
        self.email = email
        self.genres = genres
        self.artists = artists
        self.songs = songs
    def __str__(self):
        return f"{self.name}, {self.gender}, {self.age}, {self.email}"

client = MongoClient("mongodb+srv://davidlai3:sdfghj45@cluster0.3eutqra.mongodb.net/?retryWrites=true&w=majority")
db = client.Users
info = db.UserInfo

def create_user(user):
    if info.find_one({"email": user.email}) is None:
        info.insert_one(user.__dict__)

def read_user(_id):
    res = ""
    user = info.find_one({"_id": _id})
    if user is not None:
        res += f"Name: {user['name']}\n"
        res += f"Gender: {user['gender']}\n"
        res += f"Age: {user['age']}\n"
        res += f"Country: {user['country']}\n"
        res += f"Email: {user['email']}\n"
        res += f"Genres: {user['genres']}\n"
        res += f"Artists: {user['artists']}"
    return res

def update_user(_id, field, value):
    user = info.find_one({"_id": _id})
    if user is not None:
        info.update_one({"_id": _id}, {"$set": {field: value}})

def delete_user(_id):
    info.delete_one({"_id": _id})





