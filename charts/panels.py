import plotly.graph_objects as go

from dashboard.integration import load
from .base import apply_layout
from ui.theme import get_theme


def rsi_chart(df):
    t = get_theme()
    fig = go.Figure()
    if "RSI" in df:
        fig.add_trace(go.Scatter(x=df.index, y=df["RSI"], name="RSI", line=dict(color=t.chart_line)))
        fig.add_hline(y=70, line_color=t.chart_grid, line_dash="dash")
        fig.add_hline(y=30, line_color=t.chart_grid, line_dash="dash")
    return apply_layout(fig, "RSI", height=300)


def macd_chart(df):
    t = get_theme()
    fig = go.Figure()
    if "MACD" in df:
        fig.add_trace(go.Scatter(x=df.index, y=df["MACD"], name="MACD", line=dict(color=t.chart_line)))
    if "Signal" in df:
        fig.add_trace(go.Scatter(x=df.index, y=df["Signal"], name="Signal", line=dict(color=t.chart_colorway[1])))
    if "Histogram" in df:
        fig.add_bar(x=df.index, y=df["Histogram"], name="Histogram", marker_color=t.chart_volume)
    return apply_layout(fig, "MACD", height=300)


def normalized_comparison_chart(symbols: list) -> go.Figure:
    t = get_theme()
    fig = go.Figure()
    colors = list(t.chart_colorway)
    for idx, sym in enumerate(symbols):
        df, _ = load(sym)
        if df is not None and not df.empty and "Close" in df:
            normalized = df["Close"] / df["Close"].iloc[0] * 100
            fig.add_trace(go.Scatter(
                x=df.index, y=normalized, name=sym, mode="lines",
                line=dict(color=colors[idx % len(colors)]),
            ))
    return apply_layout(fig, "Normalized Price Comparison (Base 100)", height=400)
