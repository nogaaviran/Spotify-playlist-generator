import streamlit as st
from presets import load_presets

def render_core_controls():
    st.subheader("🎛️ Core feel")
    st.caption("How should this playlist ✨*feel*?✨")

    c = st.session_state["controls"]

    c["energy"] = st.slider(
        "🔥 Energy", 0.0, 1.0, c["energy"], 0.01
    )

    c["valence"] = st.slider(
        "🎭 Mood (valence)", 0.0, 1.0, c["valence"], 0.01
    )

    c["danceability"] = st.slider(
        "💃 Danceability", 0.0, 1.0, c["danceability"], 0.01
    )

    c["tempo_min"], c["tempo_max"] = st.slider(
        "🕰️ Tempo range (BPM)",
        60, 200,
        (c["tempo_min"], c["tempo_max"]),
        step=1
    )

    c["acousticness"] = st.slider(
        "🎸 Acoustic",
        0.0, 1.0, c["acousticness"], 0.01
    )

    c["instrumentalness"] = st.slider(
        "🎻 Instrumental",
        0.0, 1.0, c["instrumentalness"], 0.01
    )

    c["speechiness"] = st.slider(
        "🗣️ Vocal presence",
        0.0, 1.0, c["speechiness"], 0.01
    )


def render_presets():
    st.subheader("🎚️ Presets")
    st.caption("Quick moods to get you started - tweak anything after")


    presets = load_presets()
    cols = st.columns(len(presets))

    for col, (name, values) in zip(cols, presets.items()):
        if col.button(name.capitalize()):
            st.session_state["controls"].update(values)

