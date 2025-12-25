import yaml
from pathlib import Path
import streamlit as st

GENRES_PATH = Path(__file__).parent / "mapping" / "genres.yml"

def load_genres():
    with open(GENRES_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def render_genre_seeds():
    st.subheader("🎵 Musical anchors")
    st.caption("Pick up to 5 genres (or leave empty for a surprise 👀)")



    with open(GENRES_PATH, "r", encoding="utf-8") as f:
        genres = yaml.safe_load(f)

    selected_genres = st.multiselect(
        "Genres",
        options=genres,
        max_selections=5
    )

    st.session_state["seeds"] = {
        "genres": selected_genres
    }
    