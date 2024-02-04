# Author: Jas Khetani
# Integretion of Frontend (~Vivian & Suman) and Backend (~Jas & David)

import requests
import urllib.parse

from datetime import datetime, timedelta
from flask import Flask, redirect, request, jsonify, session, render_template

app = Flask(__name__)
app.secret_key = '7CkWZTLgAkq5sMKTwAIAhXfo6nVleb7C'

CLIENT_ID = '2dc2786c2ea544fb9e4121acbb602238'
CLIENT_SECRET = 'cc31bdeb6fc147109b55b5e7f58080ab'
REDIRECT_URI = 'https://noice-coder.github.io/HopperHacks24/callback'

AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
API_BASE_URL = 'https://api.spotify.com/v1/'

@app.route('/')
def index():
    return  render_template('index.html')

@app.route('/authenticate')
def login():
    scopes = 'user-read-email user-read-private playlist-read-private playlist-read-collaborative ugc-image-upload user-follow-read user-top-read user-read-recently-played user-library-read'
    
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

        session['access_token'] = token_info['access_token']
        session['refresh_token'] = token_info['refresh_token']
        session['expires_at'] = datetime.now().timestamp() + token_info['expires_in']

        return redirect('/object') #After login page, for scroll

@app.route('/refresh-token')
def refresh_token():
    if 'refresh_token' not in session:
        return redirect('/login')
    
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

        return redirect('/discover') #After login page, for scroll
    
if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)