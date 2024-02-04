# Author: David Lai

# Song Match

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
    return 0.7*genre + 0.2*artist + 0.1*song, resString

def findCommonElement(l1, l2):
    for i in l1:
        if i in l2:
            return str(i)
    return ""

def match(user1, user2):
    compatibility = calculateCompat(user1, user2)
    percentage = round(compatibility[0] * 100, 2)
    text = compatibility[1]
    return (percentage, text)




