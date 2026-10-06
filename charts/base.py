from __future__ import annotations

import plotly.graph_objects as go

from ui.theme import get_chart_theme


def apply_layout(fig: go.Figure, title: str, height: int = 650) -> go.Figure:
    tokens = get_chart_theme()
    fig.update_layout(
        title=dict(
            text=title,
            font=dict(size=14, color=tokens["font_color"]),
        ),
        height=height,
        margin=dict(l=20, r=20, t=50, b=20),
        paper_bgcolor=tokens["paper_bgcolor"],
        plot_bgcolor=tokens["plot_bgcolor"],
        font=dict(color=tokens["font_color"], size=12),
        legend=dict(
            orientation="h",
            bgcolor=tokens["legend_bg"],
            bordercolor=tokens["legend_border"],
            borderwidth=1,
            font=dict(color=tokens["font_color"], size=11),
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
        ),
        hoverlabel=dict(
            bgcolor=tokens["hover_bg"],
            font=dict(color=tokens["hover_font"], size=12),
            bordercolor=tokens["axis_color"],
        ),
        hovermode="closest",
        xaxis=dict(
            gridcolor=tokens["grid_color"],
            gridwidth=1,
            linecolor=tokens["axis_color"],
            linewidth=1,
            zerolinecolor=tokens["zeroline_color"],
            zerolinewidth=1,
            tickfont=dict(color=tokens["font_color"], size=11),
            title_font=dict(color=tokens["font_color"], size=12),
            showgrid=True,
        ),
        yaxis=dict(
            gridcolor=tokens["grid_color"],
            gridwidth=1,
            linecolor=tokens["axis_color"],
            linewidth=1,
            zerolinecolor=tokens["zeroline_color"],
            zerolinewidth=1,
            tickfont=dict(color=tokens["font_color"], size=11),
            title_font=dict(color=tokens["font_color"], size=12),
            showgrid=True,
        ),
        dragmode="pan",
        newshape=dict(line_color=tokens["line_color"]),
    )
    fig.update_xaxes(showspikes=True, spikethickness=1, spikecolor=tokens["grid_color"])
    fig.update_yaxes(showspikes=True, spikethickness=1, spikecolor=tokens["grid_color"])
    return fig
