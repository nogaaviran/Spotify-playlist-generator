# Functions to call Spotify APIs (recommendations, create playlist)
# Client of the Backend

import os
import requests

API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")

# Sends playlist generation request to backend, Returns parsed JSON response.
def recommend(payload: dict) -> dict:
    
    response = requests.post(
        f"{API_BASE_URL}/api/recommend",
        json=payload,
        timeout=10
    )

    response.raise_for_status()
    return response.json()
