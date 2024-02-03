from pymongo import MongoClient

class User:
    def __init__(self, name, gender, age, email, password, genres, artists, songs):
        self.name = name
        self.gender = gender
        self.age = age
        self.email = email
        self.password = password
        self.genres = genres
        self.artists = artists
        self.songs = songs
    def __str__(self):
        return f"{self.name}, {self.gender}, {self.age}, {self.email}"

client = MongoClient("mongodb+srv://davidlai3:sdfghj45@cluster0.3eutqra.mongodb.net/?retryWrites=true&w=majority")
db = client.Users
info = db.UserInfo

u1 = User("Jane", "F", 25, "janedoe@yahoo.com", "123456", ["Rock"], ["Queen"], ["Bohemian Rhapsody"])

def insert_user(user):
    info.insert_one(user.__dict__)




