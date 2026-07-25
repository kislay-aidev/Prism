import plotly.graph_objects as go
from .base import apply_layout

def build(df,title="Candlestick"):
    fig=go.Figure()
    fig.add_trace(go.Candlestick(
        x=df.index,open=df.Open,high=df.High,
        low=df.Low,close=df.Close,name="OHLC"))
    return apply_layout(fig,title)
