from functools import wraps
import streamlit as st

def cache(ttl=300):
    def deco(func):
        return st.cache_data(ttl=ttl)(func)
    return deco
