import plotly.graph_objects as go
from .base import apply_layout

def normalized(data):
    fig=go.Figure()
    for ticker,df in data.items():
        if df is None or df.empty:
            continue
        base=df.Close.iloc[0]
        fig.add_trace(go.Scatter(
            x=df.index,
            y=(df.Close/base)*100,
            mode="lines",
            name=ticker))
    return apply_layout(fig,"Normalized Comparison (%)")
