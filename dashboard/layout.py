import streamlit as st

def header(title,subtitle=""):
    st.title(title)
    if subtitle:
        st.caption(subtitle)

def metrics(cols,data):
    containers=st.columns(cols)
    for c,(k,v) in zip(containers,data.items()):
        c.metric(k,v)
