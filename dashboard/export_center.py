import streamlit as st
from export.manager import available_exports

def render():
    st.subheader("📤 Export Center")
    for name in available_exports():
        st.button(f"Export {name}", key=name)
