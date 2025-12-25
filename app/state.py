import streamlit as st

# Default Values
def init_state():
    if "controls" not in st.session_state:
        st.session_state["controls"] = {
            "energy": 0.5,
            "valence": 0.5,
            "danceability": 0.5,
            "tempo_min": 90,
            "tempo_max": 140,
        }
