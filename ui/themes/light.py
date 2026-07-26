from .tokens import ThemeTokens

LIGHT = ThemeTokens(
    name="light",
    label="Light",

    surface="#FFFFFF",
    surface_secondary="#F6F7F9",
    sidebar="#F6F7F9",
    card="#F6F7F9",
    tooltip="#FFFFFF",
    dropdown="#FFFFFF",

    primary="#6366F1",
    primary_hover="#4F46E5",
    secondary="#A1A1AA",

    text="#1E1E1E",
    text_muted="#6B7280",
    text_inverse="#FFFFFF",

    border="#E3E6EA",
    border_light="#EDF0F3",
    border_focus="#6366F1",

    hover="rgba(99, 102, 241, 0.08)",
    hover_secondary="rgba(0, 0, 0, 0.04)",
    selected="rgba(99, 102, 241, 0.12)",

    success="#16A34A",
    success_bg="#F0FDF4",
    warning="#D97706",
    warning_bg="#FFFBEB",
    danger="#DC2626",
    danger_bg="#FEF2F2",
    info="#2563EB",
    info_bg="#EFF6FF",

    chart_bg="#FFFFFF",
    chart_grid="#D9DCE2",
    chart_axis="#C0C5CC",
    chart_zeroline="#C0C5CC",
    chart_line="#6366F1",
    chart_volume="#6366F1",
    chart_legend_bg="rgba(255, 255, 255, 0.9)",
    chart_legend_border="#E3E6EA",
    chart_hover_bg="#FFFFFF",
    chart_hover_font="#1E1E1E",
    chart_colorway=("#6366F1", "#F59E0B", "#22C55E", "#EF4444", "#A78BFA", "#34D399"),

    candle_up="#22C55E",
    candle_down="#EF4444",
    volume_up="#22C55E",
    volume_down="#EF4444",

    input_bg="#FFFFFF",
    input_border="#E3E6EA",
    input_text="#1E1E1E",
    input_placeholder="#9CA3AF",
    input_focus="#6366F1",

    shadow_sm="0 1px 2px rgba(0,0,0,0.05)",
    shadow_md="0 4px 6px rgba(0,0,0,0.07)",
    shadow_lg="0 10px 15px rgba(0,0,0,0.1)",

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
