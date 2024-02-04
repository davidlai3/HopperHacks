# Author: Jas Khetani
# Integretion of Frontend (~Vivian & Suman) and Backend (~Jas & David)

import requests
import urllib.parse

from datetime import datetime
from flask import Flask, redirect, request, jsonify, session, render_template

app = Flask(__name__)
app.secret_key = '7CkWZTLgAkq5sMKTwAIAhXfo6nVleb7C'

CLIENT_ID = '2dc2786c2ea544fb9e4121acbb602238' #David's ID: 'f7e239bd09864f0e80778a36626ed251'
CLIENT_SECRET = '2dc2786c2ea544fb9e4121acbb602238' #David's Secret: '51de16b26ecc48deb53cea24443a89c6'
REDIRECT_URI = 'http://localhost:5000/callback'

AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
API_BASE_URL = 'https://api.spotify.com/v1/'

def getting_input():
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
    scopes = 'user-read-email user-top-read'
    
    params = {
        'client_id': CLIENT_ID,
        'response_type': 'code',
        'scope': scopes,
        'redirect_uri': REDIRECT_URI,
        'show_dialog': True
    }

    auth_url = f"{AUTH_URL}?{urllib.parse.urlencode(params)}"

    return redirect(auth_url) #OAuthentication URL for logging into spotify

@app.route('/callback')
def callback():
    if 'error' in request.args:
        return jsonify({"error": request.args['error']})
    
    if 'code' in request.args:
        req_body = {
            'code': request.args['code'],
            'grant_type': 'authorization_code',
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }

        response = requests.post(TOKEN_URL, data=req_body)
        token_info = response.json()

        print(token_info)

        session['access_token'] = token_info['access_token']
        session['refresh_token'] = token_info['refresh_token']
        session['expires_at'] = datetime.now().timestamp() + token_info['expires_in']

        temp = getting_input()
        print(temp)

        return redirect('/mainweb') #After login page, for scroll

@app.route('/refresh-token')
def refresh_token():
    if 'refresh_token' not in session:
        return redirect('/authenticate')
    
    if datetime.now().timestamp() > session['expires_at']:
        req_body = {
            'grant_type': 'refresh_token',
            'refresh_token': session['refresh_token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }

        response = requests.post(TOKEN_URL, data=req_body)
        new_token_info = response.json()

        session['access_token'] = new_token_info['access_token']
        session['expires_at'] = datetime.now().timestamp() + new_token_info['expires_in']

        return redirect('/mainweb') #After login page, for scroll

@app.route('/spoaut')
def spoaut():
    return render_template('spoaut.html')

@app.route('/mainweb')
def mainweb():
    if 'refresh_token' not in session:
        return redirect('/authenticate')
    
    if datetime.now().timestamp() > session['expires_at']:
        return redirect('/refresh_token')

    else:
        return render_template('/mainweb.html')
if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)
