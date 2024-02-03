def findMatches(person1, person2):
    genreMatches = []
    artistMatches = []
    songMatches = []
    for genre in person1.favoriteGenres:
        if genre in person2.favoriteGenres:
            genreMatches.append(genre)
    for artist in person1.favoriteArtists:
        if artist in person2.favoriteArtists:
            artistMatches.append(artist)
    for song in person1.favoriteSongs:
        if song in person2.favoriteSongs:
            songMatches.append(song)
    return [genreMatches, artistMatches, songMatches]
