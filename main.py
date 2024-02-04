# Author: Jas Khetani
# Integretion of Frontend (~Vivian & Suman) and Backend (~Jas & David)

import requests
import urllib.parse
import spotipy
import time

from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, redirect, request, jsonify, session, render_template, url_for

app = Flask(__name__)
app.config['SESSION_COOKIE_NAME'] = 'Mix&Match Cookie'
app.secret_key = '7CkWZTLgAkq5sMKTwAIAhXfo6nVleb7C'

TOKEN_INFO = 'token_info'
SCOPES = 'user-read-email user-top-read'

CLIENT_ID = '2dc2786c2ea544fb9e4121acbb602238' #David's ID: 'f7e239bd09864f0e80778a36626ed251'
CLIENT_SECRET = '2dc2786c2ea544fb9e4121acbb602238' #David's Secret: '51de16b26ecc48deb53cea24443a89c6'
REDIRECT_URI = 'http://localhost:5000/callback'

AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
API_BASE_URL = 'https://api.spotify.com/v1/'

def create_spotify_oauth():
    return SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=url_for('callback'), _external = True,
        scope=SCOPES
    )

def get_token():
    token_info = session.get(TOKEN_INFO, None)
    if not token_info:
        redirect(url_for('login'), external=False)
    
    now = int(time.time())

    is_expired = token_info['expires_at'] - now < 60
    if is_expired:
        spotify_oauth = create_spotify_oauth()
        token_info = spotify_oauth.refresh_access_token(token_info['refresh_token'])
    
    return token_info

def get_data():
    headers = {
    'Authorization': f"Bearer {session['access_token']}"
    }
    try:
        name = requests.get(API_BASE_URL + 'me', headers=headers).json()["display_name"]
    except:
        name = ''
    try:
        image = requests.get(API_BASE_URL + 'me', headers=headers).json()["images"]
    except:
        image = None
    #gender = False #Needs to be taken from webpage
    #age = requests.get(API_BASE_URL + 'me/', headers=headers).json() #Needs to be taken from the webpage
    #country = requests.get(API_BASE_URL + 'me', headers=headers).json()["country"]
    try:
        email = requests.get(API_BASE_URL + 'me', headers=headers).json()["email"]
    except:
        email = None
    try:
        artistsRaw = requests.get(API_BASE_URL + 'me/top/artists', headers=headers).json()["items"]
    except:
        artistsRaw = None
    try:
        tracksRaw = requests.get(API_BASE_URL + 'me/top/tracks', headers=headers).json()["items"]
    except:
        tracksRaw = None
    
    artists = []
    genres = []
    for artist in artistsRaw:
        artists.append(artist['name'])
        genres += artist['genres']
    tracks = []
    for track in tracksRaw:
        tracks.append(track['name'])

    print(f"\n\nName: {name}")
    print(f"Image: {image}")
    #print(f"Country: {country}")
    print(f"Email: {email}")
    print(f"Genres: {genres}")
    print(f"Artists: {artists}")
    print(f"Tracks: {tracks}\n\n")

    return jsonify([name, image, email, genres, artists, tracks])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/authenticate')
def login():
    auth_url = create_spotify_oauth().get_authorize_url()
    return redirect(auth_url) #OAuthentication URL for logging into spotify

@app.route('/callback')
def callback():
    session.clear()
    code = request.args.get('code')
    token_info = create_spotify_oauth().get_access_token(code)
    session[TOKEN_INFO] = token_info
    return redirect(url_for('mainweb', external=True))

@app.route('/spoaut')
def spoaut():
    return render_template('spoaut.html')

@app.route('/mainweb')
def mainweb():
    try:
        token_info = get_token()
    except:
        print("User not logged in!")
        return redirect('/authenticate')
    
    return render_template('/mainweb.html')

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)
