import streamlit as st
from core.constants import DEFAULT_TICKERS


def controls():
    st.sidebar.divider()
    st.sidebar.markdown("### Instrument")
    ticker = st.sidebar.text_input(
        "Ticker",
        DEFAULT_TICKERS[0],
        label_visibility="collapsed",
    ).upper()
    chart = st.sidebar.selectbox(
        "Chart Type",
        ["Candlestick", "OHLC", "Line", "Area"],
    )
    interval = st.sidebar.selectbox(
        "Interval",
        ["1d", "1wk", "1mo"],
    )
    return {"ticker": ticker, "chart": chart, "interval": interval}
