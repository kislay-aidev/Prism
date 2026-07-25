import streamlit as st

THEME_KEY = "theme"

def get_theme():
    return st.session_state.get(THEME_KEY, "dark")

def set_theme(name: str):
    st.session_state[THEME_KEY] = name

def available_themes():
    return ["dark", "light", "amoled"]

def inject_theme_css():
    theme = get_theme()
    if theme == "light":
        bg = "#FFFFFF"
        bg2 = "#F4F4F5"
        text = "#18181B"
        border = "#E4E4E7"
        card_bg = "#FAFAFA"
    elif theme == "amoled":
        bg = "#000000"
        bg2 = "#0A0A0B"
        text = "#FFFFFF"
        border = "#1A1A1E"
        card_bg = "#050505"
    else:
        bg = "#0F0F11"
        bg2 = "#1A1B1E"
        text = "#E4E4E7"
        border = "#27272A"
        card_bg = "#18181B"

    st.markdown(f"""
    <style>
        .stApp, .stApp > header {{ background-color: {bg}; color: {text}; }}
        .stSidebar {{ background-color: {bg2}; }}
        .stTabs [data-baseweb="tab-list"] {{ gap: 0; background-color: {bg2}; }}
        .stTabs [data-baseweb="tab"] {{ color: {text}; }}
        .stTabs [aria-selected="true"] {{ background-color: {bg}; }}
        div[data-testid="stMetric"] {{ background-color: {card_bg}; border: 1px solid {border}; border-radius: 8px; padding: 12px; }}
        div[data-testid="metric-container"] {{ background-color: transparent; }}
        .element-container {{ margin-bottom: 0.5rem; }}
        .stButton > button {{ border-radius: 6px; border: 1px solid {border}; background: {card_bg}; color: {text}; }}
        .stButton > button:hover {{ border-color: #6366F1; }}
        h1, h2, h3, h4, h5, h6 {{ color: {text}; }}
        p, li, .stMarkdown {{ color: {text}; }}
        .stDataFrame {{ background-color: {card_bg}; }}
        .stSidebar .sidebar-content {{ background-color: {bg2}; }}
        section[data-testid="stSidebar"] {{ background-color: {bg2}; border-right: 1px solid {border}; }}
        .stSelectbox [data-baseweb="select"] {{ background-color: {card_bg}; }}
        .stTextInput input {{ background-color: {card_bg}; color: {text}; border-color: {border}; }}
    </style>
    """, unsafe_allow_html=True)

def select_theme():
    choice = st.sidebar.selectbox(
        "Theme",
        available_themes(),
        index=available_themes().index(get_theme())
    )
    set_theme(choice)
    return choice
