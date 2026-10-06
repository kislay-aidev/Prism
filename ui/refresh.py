from streamlit_autorefresh import st_autorefresh

def enable(seconds=60):
    st_autorefresh(interval=seconds*1000,key="refresh")
