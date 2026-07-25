import plotly.graph_objects as go

def build(df, title="Price"):
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=df.index,y=df.Close,mode="lines",name="Close"))
    fig.update_layout(title=title,template="plotly_dark")
    return fig
