def render(report: dict) -> str:
    parts = ["<html><head><style>",
             "body{font-family:sans-serif;max-width:900px;margin:40px auto;padding:20px;background:#0F0F11;color:#E4E4E7}",
             "h1{color:#6366F1}h2{color:#A1A1AA;border-bottom:1px solid #27272A;padding-bottom:6px}",
             "table{width:100%;border-collapse:collapse;margin:12px 0}",
             "td,th{padding:8px 12px;border:1px solid #27272A;text-align:left}",
             "th{background:#1A1B1E;color:#6366F1}",
             "</style></head><body>",
             "<h1>Executive Report</h1>"]

    for section, data in report.items():
        parts.append(f"<h2>{section.title()}</h2>")
        if isinstance(data, dict):
            parts.append("<table>")
            for k, v in data.items():
                parts.append(f"<tr><td>{k}</td><td>{v}</td></tr>")
            parts.append("</table>")

    parts.append("</body></html>")
    return "\n".join(parts)
