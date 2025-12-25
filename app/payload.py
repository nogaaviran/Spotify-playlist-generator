import streamlit as st

# Translates state -> JSON
def build_payload():
    c = st.session_state["controls"]

    return {
        "energy": c["energy"],
        "valence": c["valence"],
        "danceability": c["danceability"],
        "tempo": {
            "min": c["tempo_min"],
            "max": c["tempo_max"]
        }
    }
