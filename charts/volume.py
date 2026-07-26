import plotly.graph_objects as go
from .base import apply_layout
from ui.theme import get_chart_theme

def build(df):
    tokens = get_chart_theme()
    fig=go.Figure()
    fig.add_bar(x=df.index,y=df.Volume,name="Volume", marker_color=tokens["volume_color"])
    return apply_layout(fig,"Volume", height=300)
