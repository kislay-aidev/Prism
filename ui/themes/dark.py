from .tokens import ThemeTokens

DARK = ThemeTokens(
    name="dark",
    label="Dark",

    surface="#111111",
    surface_secondary="#1A1A1A",
    sidebar="#1A1A1A",
    card="#1A1A1A",
    tooltip="#222222",
    dropdown="#1A1A1A",

    primary="#818CF8",
    primary_hover="#6366F1",
    secondary="#A1A1AA",

    text="#F2F2F2",
    text_muted="#888888",
    text_inverse="#111111",

    border="#2A2A2A",
    border_light="#333333",
    border_focus="#818CF8",

    hover="rgba(129, 140, 248, 0.12)",
    hover_secondary="rgba(255, 255, 255, 0.05)",
    selected="rgba(129, 140, 248, 0.2)",

    success="#16A34A",
    success_bg="#052E16",
    warning="#D97706",
    warning_bg="#451A03",
    danger="#DC2626",
    danger_bg="#450A0A",
    info="#2563EB",
    info_bg="#0C1929",

    chart_bg="#111111",
    chart_grid="#2C2C2C",
    chart_axis="#3A3A3A",
    chart_zeroline="#3A3A3A",
    chart_line="#818CF8",
    chart_volume="#818CF8",
    chart_legend_bg="rgba(17, 17, 17, 0.9)",
    chart_legend_border="#2A2A2A",
    chart_hover_bg="#222222",
    chart_hover_font="#F2F2F2",
    chart_colorway=("#818CF8", "#F59E0B", "#22C55E", "#EF4444", "#A78BFA", "#34D399"),

    candle_up="#22C55E",
    candle_down="#EF4444",
    volume_up="#22C55E",
    volume_down="#EF4444",

    input_bg="#111111",
    input_border="#2A2A2A",
    input_text="#F2F2F2",
    input_placeholder="#888888",
    input_focus="#818CF8",

    shadow_sm="0 1px 2px rgba(0,0,0,0.3)",
    shadow_md="0 4px 6px rgba(0,0,0,0.4)",
    shadow_lg="0 10px 15px rgba(0,0,0,0.5)",

    radius_sm="4px",
    radius_md="6px",
    radius_lg="10px",

    font_family="'Inter', -apple-system, BlinkMacSystemFont, sans-serif",
    font_size_xs="11px",
    font_size_sm="12px",
    font_size_md="13px",
    font_size_lg="16px",
    font_size_xl="20px",

    transition_fast="0.12s ease",
    transition_normal="0.2s ease",
)
