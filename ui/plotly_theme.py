def build_chart_tokens(t) -> dict:
    return {
        "paper_bgcolor": t.chart_bg,
        "plot_bgcolor": t.chart_bg,
        "font_color": t.text,
        "grid_color": t.chart_grid,
        "axis_color": t.chart_axis,
        "zeroline_color": t.chart_zeroline,
        "line_color": t.chart_line,
        "volume_color": t.chart_volume,
        "legend_bg": t.chart_legend_bg,
        "legend_border": t.chart_legend_border,
        "hover_bg": t.chart_hover_bg,
        "hover_font": t.chart_hover_font,
    }
