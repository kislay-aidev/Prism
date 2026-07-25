import streamlit as st

def render():
    c1,c2,c3=st.columns(3)
    c1.button('Refresh')
    c2.button('Export')
    c3.button('Reset Layout')
