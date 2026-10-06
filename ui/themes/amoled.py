from .tokens import ThemeTokens

AMOLED = ThemeTokens(
    name="amoled",
    label="AMOLED",

    surface="#000000",
    surface_secondary="#090909",
    sidebar="#090909",
    card="#090909",
    tooltip="#141414",
    dropdown="#090909",

    primary="#A78BFA",
    primary_hover="#8B5CF6",
    secondary="#71717A",

    text="#FFFFFF",
    text_muted="#555555",
    text_inverse="#000000",

    border="#141414",
    border_light="#1A1A1A",
    border_focus="#A78BFA",

    hover="rgba(167, 139, 250, 0.15)",
    hover_secondary="rgba(255, 255, 255, 0.04)",
    selected="rgba(167, 139, 250, 0.25)",

    success="#16A34A",
    success_bg="#052E16",
    warning="#D97706",
    warning_bg="#451A03",
    danger="#DC2626",
    danger_bg="#450A0A",
    info="#2563EB",
    info_bg="#0C1929",

    chart_bg="#000000",
    chart_grid="#1A1A1A",
    chart_axis="#222222",
    chart_zeroline="#222222",
    chart_line="#A78BFA",
    chart_volume="#A78BFA",
    chart_legend_bg="rgba(0, 0, 0, 0.9)",
    chart_legend_border="#141414",
    chart_hover_bg="#141414",
    chart_hover_font="#FFFFFF",
    chart_colorway=("#A78BFA", "#F59E0B", "#22C55E", "#EF4444", "#818CF8", "#34D399"),

    candle_up="#22C55E",
    candle_down="#EF4444",
    volume_up="#22C55E",
    volume_down="#EF4444",

    input_bg="#000000",
    input_border="#141414",
    input_text="#FFFFFF",
    input_placeholder="#555555",
    input_focus="#A78BFA",

    shadow_sm="0 1px 2px rgba(0,0,0,0.5)",
    shadow_md="0 4px 6px rgba(0,0,0,0.6)",
    shadow_lg="0 10px 15px rgba(0,0,0,0.7)",

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
