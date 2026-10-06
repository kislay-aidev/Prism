import streamlit as st
from datetime import datetime


def render(status: str, ticker: str = ""):
    col1, col2, col3 = st.columns([4, 2, 2])
    col1.caption(f"System Status: {status}")
    if ticker:
        col2.caption(f"Active: {ticker}")
    col3.caption(datetime.now().strftime("%Y-%m-%d %H:%M UTC"))
