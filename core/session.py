import streamlit as st

def init():
    st.session_state.setdefault('theme','dark')
    st.session_state.setdefault('watchlist',[])
