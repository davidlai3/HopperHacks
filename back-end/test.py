from mongotest import User, insert_user, info
from matchmaker import match


def generateMatches(user1):
    matches = []
    insert_user(user1)
    for post in info.find({"gender": "Male"},{"_id":0}):
        if post["email"] != user1.email:
            user2 = User(**post)
            matches.append((user2, match(user1, user2)[0]))
    matches.sort(key=lambda x: x[1], reverse=True)
    return matches

def displayMatches(matches):
    print("The top matches are: ")
    for match in matches:
        print(match[0].name, str(match[1]) + "%")

user = {
  "name": "Noah",
  "gender": "Male",
  "age": 28,
  "email": "noah@example.com",
  "country": "Canada",
  "genres": ["Rock", "Hip Hop", "Alternative", "EDM"],
  "artists": ["Foo Fighters", "Drake", "Twenty One Pilots", "Calvin Harris"],
  "songs": ["Everlong", "Hotline Bling", "Stressed Out", "Feel So Close"]
}

user = User(**user)
displayMatches(generateMatches(user))

 




