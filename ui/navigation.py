import streamlit as st

def tabs():
    return st.sidebar.radio(
        "Navigate",
        ["Overview","Technical","Financials","News","Portfolio","AI","Settings"]
    )
