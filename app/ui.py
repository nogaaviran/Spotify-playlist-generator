import streamlit as st
from presets import load_presets

st.markdown("""
<style>
div[data-testid="stButton"] button {
    white-space: nowrap;
    height: 56px;
    font-size: 16px;
    margin: 4px;
}
</style>
""", unsafe_allow_html=True)




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
        "🌿⚡ Organic ↔ Electronic",
        0.0, 1.0, c["acousticness"], 0.01
    )

    c["instrumentalness"] = st.slider(
        "🎤🎸 Vocals ↔ Instrumental",
        0.0, 1.0, c["instrumentalness"], 0.01
    )

    c["speechiness"] = st.slider(
        "🗣️ Background ↔ Sing-along",
        0.0, 1.0, c["speechiness"], 0.01
    )

def render_presets():
    st.subheader("🎚️ Presets")
    st.caption("(you can tweak anything after)")

    presets = load_presets()
    cols = st.columns(4)

    for i, (name, values) in enumerate(presets.items()):
        col = cols[i % 4]

        if col.button(name.replace("_", " ").title()):
            # Update controls
            for key, value in values.items():
                if key != "suggested_genres":
                    st.session_state["controls"][key] = value

            # Update genres
            if "suggested_genres" in values:
                st.session_state["seeds"]["genres"] = values["suggested_genres"]


