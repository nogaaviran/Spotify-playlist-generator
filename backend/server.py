from flask import Flask, request, jsonify
from flask_cors import CORS

from server.spotify import get_recommendations
from server.state import get_spotify_client

app = Flask(__name__)
CORS(app)  # allow frontend access


@app.route("/", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "message": "Spotify backend is running"
    })


@app.route("/recommend", methods=["POST"])
def recommend():
    """
    Generate track recommendations based on up to 5 words.
    """

    # --- Auth check ---
    sp = get_spotify_client()
    if sp is None:
        return jsonify({"error": "User not authenticated"}), 401

    # --- Input validation ---
    data = request.get_json()
    if not data or "words" not in data:
        return jsonify({
            "error": "Invalid input",
            "details": "Missing 'words' field"
        }), 400

    words = data["words"]

    if not isinstance(words, list) or not (1 <= len(words) <= 5):
        return jsonify({
            "error": "Invalid input",
            "details": "Words must be an array of 1–5 strings"
        }), 400

    # --- Call application logic ---
    try:
        result = get_recommendations(sp, words)
        return jsonify(result), 200

    except Exception as e:
        return jsonify({
            "error": "Spotify API error",
            "details": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
