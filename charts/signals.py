import plotly.graph_objects as go

def add_trade_markers(fig, buys, sells):
    if buys is not None and not buys.empty:
        fig.add_trace(go.Scatter(x=buys.index,y=buys.Close,mode="markers",
                                 marker_symbol="triangle-up",marker_size=11,
                                 name="BUY"))
    if sells is not None and not sells.empty:
        fig.add_trace(go.Scatter(x=sells.index,y=sells.Close,mode="markers",
                                 marker_symbol="triangle-down",marker_size=11,
                                 name="SELL"))
    return fig
