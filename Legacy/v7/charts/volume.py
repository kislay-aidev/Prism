import plotly.graph_objects as go

def build(df):
    fig=go.Figure()
    fig.add_bar(x=df.index,y=df.Volume,name="Volume")
    fig.update_layout(title="Volume",template="plotly_dark")
    return fig
