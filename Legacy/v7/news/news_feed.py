from datetime import datetime
import yfinance as yf
import streamlit as st

@st.cache_data(ttl=1800)
def fetch_news(ticker, limit=10):
    try:
        items=yf.Ticker(ticker).news or []
    except Exception:
        return []
    out=[]
    for n in items[:limit]:
        ts=n.get("providerPublishTime")
        try:
            dt=datetime.utcfromtimestamp(ts).strftime("%Y-%m-%d %H:%M")
        except Exception:
            dt="N/A"
        out.append({"title":n.get("title",""),"publisher":n.get("publisher",""),"time":dt,"link":n.get("link","")})
    return out

def render_news(st_module, ticker, limit=5):
    items=fetch_news(ticker,limit)
    if not items:
        st_module.caption("No recent news.")
        return
    for n in items:
        st_module.markdown(f"**{n['title']}**")
        st_module.caption(f"{n['publisher']} · {n['time']}")
        if n["link"]:
            st_module.markdown(f"[Read more]({n['link']})")
        st_module.divider()
