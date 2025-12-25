import streamlit as st
from ui_state import init_state
from ui import render_core_controls, render_presets
from payload import build_payload
from seeds import render_genre_seeds

st.set_page_config(page_title="Playlist by Feel")

st.title("🎛️ Playlist by Feel")
st.write("Tune the knobs to shape your playlist. You can also use the presets if you're SO uninspired...")
st.markdown("---")

init_state()

render_presets()

render_core_controls()
st.markdown("---")

render_genre_seeds()
st.markdown("---")


if st.button("Generate playlist"):
    payload = build_payload()

    st.success("Playlist ready to go!")

    controls = payload["controls"]
    seeds = payload.get("seeds", {})
    tempo = controls["tempo"]
    genres = seeds.get("genres", [])

    st.write(f"🔥 **Energy:** {controls['energy']:.2f}")
    st.write(f"😊 **Mood:** {controls['valence']:.2f}")
    st.write(f"💃 **Danceability:** {controls['danceability']:.2f}")
    st.write(f"⚡ **Tempo:** {tempo['min']}–{tempo['max']} BPM")
    st.write(f"🎵 **Genres:** {', '.join(genres) if genres else 'Surprise me'}")


    # from spotify import recommend
    # result = recommend(payload)
    # st.write(result)

