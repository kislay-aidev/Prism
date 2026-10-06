import streamlit as st

def render(title,subtitle=''):
    st.title(title)
    if subtitle:
        st.caption(subtitle)
