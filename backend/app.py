from flask import Flask, redirect, request, session, url_for, jsonify
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
import os
import time


app = Flask(__name__)
app.secret_key = 'your_random_secret_key'  # for session encryption
app.config['SESSION_COOKIE_NAME'] = 'Spotify-Login-Session'

# Confi
# 69gure Spotify OAuth
sp_oauth = SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri="http://127.0.0.1:5000/callback",  # updated for Spotify local dev policy
    scope="user-read-private user-read-email"
)

@app.route('/')
def index():
    return jsonify({
        "message": "Spotify backend is running",
        "login_url": "/login"
    })

@app.route('/login')
def login():
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    if code:
        token_info = sp_oauth.get_access_token(code)
        session['token_info'] = token_info
        return redirect(url_for('profile'))
    else:
        return "Authorization failed. No code returned from Spotify.", 400

@app.route('/profile')
def profile():
    token_info = get_valid_token()
    if not token_info:
        return jsonify({"error": "Not authenticated"}), 401

    sp = Spotify(auth=token_info['access_token'])
    user_info = sp.current_user()

    return jsonify({
        "display_name": user_info["display_name"],
        "email": user_info["email"],
        "spotify_id": user_info["id"]
    })

def get_valid_token():
    token_info = session.get('token_info')

    if not token_info:
        return None

    # Check if token expired
    now = int(time.time())
    is_expired = token_info['expires_at'] - now < 60

    if is_expired:
        token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
        session['token_info'] = token_info

    return token_info

if __name__ == '__main__':
    app.run(debug=True)
