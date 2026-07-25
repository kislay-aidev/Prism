def build(indicators: dict) -> dict:
    if not indicators:
        return {"status": "No data", "indicators": {}}
    report = {"status": "success", "indicators": {}}
    for name, value in indicators.items():
        report["indicators"][name] = {
            "value": round(float(value), 2) if value else None,
            "signal": _signal(name, value),
        }
    return report


def _signal(name: str, value) -> str:
    if value is None:
        return "neutral"
    name = name.upper()
    if name == "RSI":
        if value < 30:
            return "oversold"
        if value > 70:
            return "overbought"
        return "neutral"
    if name == "MACD":
        return "bullish" if value > 0 else "bearish"
    if name == "ADX":
        return "trending" if value > 25 else "ranging"
    return "neutral"
