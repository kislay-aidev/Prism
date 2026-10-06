from dataclasses import dataclass


@dataclass(frozen=True)
class ThemeTokens:
    name: str
    label: str

    surface: str
    surface_secondary: str
    sidebar: str
    card: str
    tooltip: str
    dropdown: str

    primary: str
    primary_hover: str
    secondary: str

    text: str
    text_muted: str
    text_inverse: str

    border: str
    border_light: str
    border_focus: str

    hover: str
    hover_secondary: str
    selected: str

    success: str
    success_bg: str
    warning: str
    warning_bg: str
    danger: str
    danger_bg: str
    info: str
    info_bg: str

    chart_bg: str
    chart_grid: str
    chart_axis: str
    chart_zeroline: str
    chart_line: str
    chart_volume: str
    chart_legend_bg: str
    chart_legend_border: str
    chart_hover_bg: str
    chart_hover_font: str
    chart_colorway: tuple

    candle_up: str
    candle_down: str
    volume_up: str
    volume_down: str

    input_bg: str
    input_border: str
    input_text: str
    input_placeholder: str
    input_focus: str

    shadow_sm: str
    shadow_md: str
    shadow_lg: str

    radius_sm: str
    radius_md: str
    radius_lg: str

    font_family: str
    font_size_xs: str
    font_size_sm: str
    font_size_md: str
    font_size_lg: str
    font_size_xl: str

    transition_fast: str
    transition_normal: str
