import streamlit as st
from .fetcher import fetch
from .summarizer import summarize

def render(symbol):
    data = fetch(symbol)
    if not data:
        st.subheader("News Intelligence")
        st.info("No recent news is available for this symbol right now.")
        return

    info = summarize(data)
    st.subheader("News Intelligence")
    st.metric("Sentiment", info["sentiment"])
    st.caption(f"{info['headline_count']} headlines analyzed")
    for item in data[:5]:
        st.markdown(f"**{item['title']}**")
        st.caption(f"{item['publisher']} • {item['published']}")
        if item["link"]:
            st.markdown(f"[Read more]({item['link']})")
        st.divider()
