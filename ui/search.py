import streamlit as st

def ticker():
    return st.sidebar.text_input("Search Ticker","AAPL").upper()
