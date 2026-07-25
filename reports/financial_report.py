def build(metrics: dict) -> dict:
    if not metrics:
        return {"status": "No data", "metrics": {}}
    return {
        "status": "success",
        "metrics": {k: _format(v) for k, v in metrics.items()},
    }


def _format(value):
    if value is None:
        return "N/A"
    try:
        v = float(value)
        if abs(v) >= 1e12:
            return f"{v/1e12:.2f}T"
        if abs(v) >= 1e9:
            return f"{v/1e9:.2f}B"
        if abs(v) >= 1e6:
            return f"{v/1e6:.2f}M"
        return f"{v:,.2f}"
    except (ValueError, TypeError):
        return str(value)
