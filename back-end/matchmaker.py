# Author: David Lai

# Song Match

from mongotest import User
from collections import Counter
import math

# cosine similarity for compatibility
def formatLists(items):
    c1 = Counter(items)
    for i in range(len(items)):
        c1[items[i]] += len(items)-1-i
    return c1


def counter_cosine_similarity(c1, c2):
    terms = set(c1).union(c2)
    dotprod = sum(c1.get(k, 0) * c2.get(k, 0) for k in terms)
    magA = math.sqrt(sum(c1.get(k, 0)**2 for k in terms))
    magB = math.sqrt(sum(c2.get(k, 0)**2 for k in terms))
    return dotprod / (magA * magB)


def calculateCompat(user1, user2):
    genre = counter_cosine_similarity(formatLists(user1.genres), formatLists(user2.genres))
    artist = counter_cosine_similarity(formatLists(user1.artists), formatLists(user2.artists))
    song = counter_cosine_similarity(formatLists(user1.songs), formatLists(user2.songs))

    resString = ""
    text = max(genre, artist, song)
    if text == genre:
        resString = findCommonElement(user1.genres, user2.genres) + " music"
    elif text == artist:
        resString = findCommonElement(user1.artists, user2.artists)
    elif text == song:
        resString = findCommonElement(user1.songs, user2.songs)
    return (genre + artist + song) / 3, resString

def findCommonElement(l1, l2):
    for i in l1:
        if i in l2:
            return str(i)
    return ""

def match(user1, user2):
    res = ""
    compatibility = calculateCompat(user1, user2)
    percentage = round(compatibility[0] * 100, 2)
    text = compatibility[1]
    if percentage != 0:
        res += f"{ user1.name } and { user2.name } are { str(percentage) }% compatible"
        res += f"\nYou both listen to { text }"
    else:
        res = f"{ user1.name } and { user2.name } are not compatible. :("
    return res

user1 = User("David", "M", "18", "david@gmail", "12345", ["Rock", "Rap", "RNB", "Poo"], ["Queen", "Michael Jackson", "Billy Joel", "Kendrick Lamar"], ["Bohemian Rhapsody", "Pride", "Instagram", "War"])

user2 = User("Jas", "M", "18", "david@gmail", "12345", ["Indie", "HyperPop", "Grunge", "Classical"], ["Boy Pablo", "Drake", "Yeat", "Pop Smoke"], ["These Days", "Alright", "Ultimate", "August"])

print(match(user1, user2))


