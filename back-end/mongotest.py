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

# Takes in api data and finds top genre
def parseInfo():
    pass

def insert_user(user):
    info.insert_one(user.__dict__)

#f = open('Names.json')
#data = json.load(f)
#info.insert_many(data)




