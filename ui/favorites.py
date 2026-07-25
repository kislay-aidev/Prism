import streamlit as st

def add(symbol):
    fav=st.session_state.setdefault("favorites",[])
    if symbol not in fav:
        fav.append(symbol)
    return fav
