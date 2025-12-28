import streamlit as st

# Default Values
def init_state():
    if "controls" not in st.session_state:
        st.session_state["controls"] = {
            "energy": 0.5,
            "valence": 0.5,
            "danceability": 0.5,
            "tempo_min": 50,
            "tempo_max": 100,
            "acousticness": 0.5,
            "instrumentalness": 0.3,
            "speechiness": 0.3,
        }

    if "active_preset" not in st.session_state:
        st.session_state["active_preset"] = None

