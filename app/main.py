import streamlit as st
from state import init_state
from ui import render_core_controls
from payload import build_payload

st.set_page_config(page_title="Playlist by Feel")

st.title("🎛️ Playlist by Feel")
st.write("Tune the knobs to shape your playlist.")
st.markdown("---")

init_state()
render_core_controls()

st.markdown("---")

if st.button("Generate playlist"):
    payload = build_payload()
    st.json(payload)

