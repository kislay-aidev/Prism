import plotly.graph_objects as go
from .base import apply_layout

def build(df,title="Price"):
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=df.index,y=df.Close,
                             mode="lines",name="Close"))
    return apply_layout(fig,title)
