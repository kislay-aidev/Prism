import streamlit as st

DEFAULTS = {
    "watchlist": [],
    "recent_tickers": [],
    "theme": "dark",
    "chart_type": "Candlestick",
    "favorites": [],
}


def initialize():
    for key, value in DEFAULTS.items():
        st.session_state.setdefault(key, value)
