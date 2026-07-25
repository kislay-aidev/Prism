import plotly.graph_objects as go

def normalized(data_dict):
    fig=go.Figure()
    for ticker,df in data_dict.items():
        if df is None or df.empty:
            continue
        base=df.Close.iloc[0]
        fig.add_trace(go.Scatter(x=df.index,y=(df.Close/base)*100,mode="lines",name=ticker))
    fig.update_layout(title="Normalized Comparison (%)",template="plotly_dark")
    return fig
