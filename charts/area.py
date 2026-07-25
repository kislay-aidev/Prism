import plotly.graph_objects as go
from .base import apply_layout

def build(df,title="Area"):
    fig=go.Figure()
    fig.add_trace(go.Scatter(
        x=df.index,y=df.Close,
        fill="tozeroy",
        name="Close"))
    return apply_layout(fig,title)
