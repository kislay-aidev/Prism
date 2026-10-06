from datetime import datetime
import yfinance as yf
import streamlit as st


@st.cache_data(ttl=1800, show_spinner=False)
def fetch(symbol, limit=15):
    try:
        items = yf.Ticker(symbol).news or []
    except Exception:
        return []
    out = []
    for n in items[:limit]:
        ts = n.get("providerPublishTime")
        try:
            ts = datetime.utcfromtimestamp(ts).strftime("%Y-%m-%d %H:%M UTC")
        except Exception:
            ts = "N/A"
        out.append({
            "title": n.get("title", ""),
            "publisher": n.get("publisher", ""),
            "published": ts,
            "link": n.get("link", ""),
        })
    return out
