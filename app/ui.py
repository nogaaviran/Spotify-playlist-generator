import streamlit as st

def render_core_controls():
    st.subheader("Core feel")

    c = st.session_state["controls"]

    c["energy"] = st.slider(
        "Energy", 0.0, 1.0, c["energy"], 0.01
    )

    c["valence"] = st.slider(
        "Valence (mood)", 0.0, 1.0, c["valence"], 0.01
    )

    c["danceability"] = st.slider(
        "Danceability", 0.0, 1.0, c["danceability"], 0.01
    )

    c["tempo_min"], c["tempo_max"] = st.slider(
        "Tempo (BPM)",
        60, 200,
        (c["tempo_min"], c["tempo_max"]),
        step=1
    )
