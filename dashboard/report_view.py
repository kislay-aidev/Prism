import streamlit as st
def render(report:dict):
    st.subheader("Report Preview")
    st.json(report)
