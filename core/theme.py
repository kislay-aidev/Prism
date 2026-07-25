import streamlit as st

THEMES = ("dark", "light", "amoled")


def sidebar_theme():
    current = st.session_state.get("theme", "dark")
    index = THEMES.index(current) if current in THEMES else 0
    choice = st.sidebar.selectbox("Theme", THEMES, index=index)
    st.session_state["theme"] = choice
    return choice
