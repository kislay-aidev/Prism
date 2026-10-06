import streamlit as st

def render_sections(sections):
    for section in sections:
        st.subheader(section)
        st.empty()
