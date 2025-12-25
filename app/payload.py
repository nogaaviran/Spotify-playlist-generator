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

def build_payload():
    controls = st.session_state["controls"]
    seeds = st.session_state.get("seeds", {})

    return {
        "controls": {
            "energy": controls["energy"],
            "valence": controls["valence"],
            "danceability": controls["danceability"],
            "tempo": {
                "min": controls["tempo_min"],
                "max": controls["tempo_max"]
            }
        },
        "seeds": seeds
    }
