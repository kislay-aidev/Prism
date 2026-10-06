import plotly.graph_objects as go

def build(df, title="Candlestick"):
    fig=go.Figure()
    fig.add_trace(go.Candlestick(x=df.index,open=df.Open,high=df.High,low=df.Low,close=df.Close))
    fig.update_layout(title=title,template="plotly_dark")
    return fig
