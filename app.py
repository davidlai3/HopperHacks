# Integretion for frontend (~Vivian & Suman) and backend (~Jas & David)


import requests
import spotipy

from spotipy.oauth2 import SpotifyOAuth
from flask import *

app = Flask(__name__)
app.secret_key = 'Uy6Hv36SH5taBmsHUNhHaG99RVUp2BKC'
app.config['SESSION_COOKIE_NAME'] = 'User Cookie'

@app.route('/')
def index():
    return render_template('index.html')
if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)