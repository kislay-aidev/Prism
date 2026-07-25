import plotly.graph_objects as go
from .base import apply_layout

def build(df):
    fig=go.Figure()
    fig.add_bar(x=df.index,y=df.Volume,name="Volume")
    return apply_layout(fig,"Volume")
