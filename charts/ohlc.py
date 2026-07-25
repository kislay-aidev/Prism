import plotly.graph_objects as go
from .base import apply_layout

def build(df,title="OHLC"):
    fig=go.Figure()
    fig.add_trace(go.Ohlc(
        x=df.index,open=df.Open,high=df.High,
        low=df.Low,close=df.Close))
    return apply_layout(fig,title)
