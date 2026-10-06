from ui.theme import get_theme


def render(report: dict) -> str:
    t = get_theme()
    parts = [
        "<html><head><style>",
        f"body{{font-family:'Inter',sans-serif;max-width:900px;margin:40px auto;padding:20px;background:{t.surface};color:{t.text}}}",
        f"h1{{color:{t.primary}}}h2{{color:{t.secondary};border-bottom:1px solid {t.border};padding-bottom:6px}}",
        "table{width:100%;border-collapse:collapse;margin:12px 0}",
        f"td,th{{padding:8px 12px;border:1px solid {t.border};text-align:left}}",
        f"th{{background:{t.surface_secondary};color:{t.primary}}}",
        "</style></head><body>",
        "<h1>Executive Report</h1>",
    ]

    for section, data in report.items():
        parts.append(f"<h2>{section.title()}</h2>")
        if isinstance(data, dict):
            parts.append("<table>")
            for k, v in data.items():
                parts.append(f"<tr><td>{k}</td><td>{v}</td></tr>")
            parts.append("</table>")

    parts.append("</body></html>")
    return "\n".join(parts)
