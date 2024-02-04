from mongotest import User
from matchmaker import match
import json


f = open('Names.json')

test = {
  "name": "Morgan",
  "gender": "Female",
  "age": 27,
  "email": "morgan@example.com",
  "password": "securePass987",
  "genres": ["Pop", "Rock", "Electronic", "Classical"],
  "artists": ["Lady Gaga", "Coldplay", "Deadmau5", "Ludwig van Beethoven"],
  "songs": ["Bad Romance", "Fix You", "Ghosts 'n' Stuff", "Moonlight Sonata"]
}
test = User(**test)

data = json.load(f)

for item in data:
    user = User(**item)
    print(match(user, test))
