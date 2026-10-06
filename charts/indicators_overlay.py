import plotly.graph_objects as go

def add_sma(fig, df, column, name="SMA"):
    if column in df:
        fig.add_trace(go.Scatter(x=df.index,y=df[column],mode="lines",name=name))
    return fig

def add_ema(fig, df, column, name="EMA"):
    if column in df:
        fig.add_trace(go.Scatter(x=df.index,y=df[column],mode="lines",name=name))
    return fig

def add_bollinger(fig, df, upper="Upper", lower="Lower"):
    if upper in df:
        fig.add_trace(go.Scatter(x=df.index,y=df[upper],name="Upper Band",line=dict(dash="dot")))
    if lower in df:
        fig.add_trace(go.Scatter(x=df.index,y=df[lower],name="Lower Band",line=dict(dash="dot")))
    return fig
