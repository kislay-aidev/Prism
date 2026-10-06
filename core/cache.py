import streamlit as st

def cache(ttl=300):
    def deco(f):
        return st.cache_data(ttl=ttl)(f)
    return deco
