"""
backend/server.py

Flask backend for Spotify Playlist Generator.
Exposes JSON endpoints:
- /login
- /callback
- /profile
- /recommend

All frontend payloads from app/ will call /recommend.
"""

from flask import Flask, request, jsonify, redirect, session
from flask_cors import CORS
from app.state import get_spotify_client
from app.spotify import get_recommendations
from app.oauth import sp_oauth  # your OAuth object

app = Flask(__name__)
app.secret_key = "replace-with-a-secure-random-key"  # required for session
CORS(app)  # allow frontend to call from Streamlit

# -----------------------
# Health check
# -----------------------
@app.route("/", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "message": "Spotify backend is running"
    })


# -----------------------
# Login / OAuth
# -----------------------
@app.route("/login", methods=["GET"])
def login():
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)


@app.route("/callback", methods=["GET"])
def callback():
    code = request.args.get("code")
    if not code:
        return jsonify({"error": "No code in callback"}), 400

    try:
        token_info = sp_oauth.get_access_token(code)
        session["token_info"] = token_info
        return redirect("/profile")
    except Exception as e:
        return jsonify({"error": "OAuth failed", "details": str(e)}), 500


# -----------------------
# Profile endpoint (test)
# -----------------------
@app.route("/profile", methods=["GET"])
def profile():
    sp = get_spotify_client()
    if sp is None:
        return jsonify({"error": "User not authenticated"}), 401

    try:
        user_info = sp.current_user()
        return jsonify({
            "display_name": user_info.get("display_name"),
            "email": user_info.get("email"),
            "spotify_id": user_info.get("id")
        })
    except Exception as e:
        return jsonify({"error": "Spotify API error", "details": str(e)}), 500


# -----------------------
# Recommend endpoint (CORE)
# -----------------------
@app.route("/recommend", methods=["POST"])
def recommend():
    sp = get_spotify_client()
    if sp is None:
        return jsonify({"error": "User not authenticated"}), 401

    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input", "details": "No JSON body"}), 400

    try:
        result = get_recommendations(sp, data)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": "Spotify API error", "details": str(e)}), 500


# -----------------------
# Run server
# -----------------------
if __name__ == "__main__":
    app.run(debug=True)
