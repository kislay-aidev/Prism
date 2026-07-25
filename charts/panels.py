import plotly.graph_objects as go

def rsi_chart(df):
    fig=go.Figure()
    if "RSI" in df:
        fig.add_trace(go.Scatter(x=df.index,y=df["RSI"],name="RSI"))
        fig.add_hline(y=70)
        fig.add_hline(y=30)
    fig.update_layout(title="RSI",template="plotly_dark")
    return fig

def macd_chart(df):
    fig=go.Figure()
    if "MACD" in df:
        fig.add_trace(go.Scatter(x=df.index,y=df["MACD"],name="MACD"))
    if "Signal" in df:
        fig.add_trace(go.Scatter(x=df.index,y=df["Signal"],name="Signal"))
    if "Histogram" in df:
        fig.add_bar(x=df.index,y=df["Histogram"],name="Histogram")
    fig.update_layout(title="MACD",template="plotly_dark")
    return fig
