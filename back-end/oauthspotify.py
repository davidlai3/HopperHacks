import requests
import urllib.parse
from flask import Flask, redirect

app = Flask(__name__)
app.secret_key = '7CkWZTLgAkq5sMKTwAIAhXfo6nVleb7C'

CLIENT_ID = '2dc2786c2ea544fb9e4121acbb602238'
CLIENT_SECRET = 'cc31bdeb6fc147109b55b5e7f58080ab'
REDIRECT_URI = 'https://noice-coder.github.io/HopperHacks24/callback'

AUTH_URL = 'https://accounts.spotify.com/authorize'
TOCKEN_URL = 'https://accounts.spotify.com/api/token'
API_BASE_URL = 'https://api.spotify.com/v1/'

@app.route('/login')
def login():
    pass