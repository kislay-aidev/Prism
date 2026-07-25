import streamlit as st
from .fetcher import fetch
from .summarizer import summarize

def render(symbol):
    data=fetch(symbol)
    info=summarize(data)
    st.subheader("News Intelligence")
    st.metric("Sentiment",info["sentiment"])
    for item in data[:5]:
        st.markdown(f"**{item['title']}**")
        st.caption(f"{item['publisher']} • {item['published']}")
        if item["link"]:
            st.markdown(f"[Read more]({item['link']})")
        st.divider()
