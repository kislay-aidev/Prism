from __future__ import annotations

from datetime import date, timedelta


def resolve_start_date(date_range: str, today: date | None = None) -> date:
    current_day = today or date.today()
    date_ranges = {
        "1mo": current_day - timedelta(days=30),
        "3mo": current_day - timedelta(days=90),
        "6mo": current_day - timedelta(days=180),
        "1y": current_day - timedelta(days=365),
        "2y": current_day - timedelta(days=730),
        "5y": current_day - timedelta(days=1825),
        "max": date(2000, 1, 1),
    }
    return date_ranges.get(date_range, current_day - timedelta(days=365))


def flatten_financial_metrics(metrics: dict) -> list[tuple[str, object]]:
    flattened: list[tuple[str, object]] = []
    for section, values in metrics.items():
        if isinstance(values, dict):
            for label, value in values.items():
                flattened.append((f"{section} · {label}", value))
        else:
            flattened.append((section, values))
    return flattened


def format_financial_value(label: str, value: object) -> str:
    if value is None or value == "":
        return "N/A"
    if "date" in label.lower() and isinstance(value, (int, float)):
        try:
            return date.fromtimestamp(int(value)).isoformat()
        except Exception:
            return str(value)
    if isinstance(value, float):
        if -1 <= value <= 1 and any(
            token in label.lower()
            for token in ["yield", "growth", "margin", "roe", "roa", "ratio"]
        ):
            return f"{value:.2%}"
        return f"{value:,.2f}"
    if isinstance(value, int):
        return f"{value:,}"
    return str(value)
