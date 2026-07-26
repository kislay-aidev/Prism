import plotly.graph_objects as go
from .base import apply_layout
from ui.theme import get_chart_theme

def build(df,title="Price"):
    tokens = get_chart_theme()
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=df.index,y=df.Close,
                             mode="lines",name="Close",
                             line=dict(color=tokens["line_color"])))
    return apply_layout(fig,title)
