from .signal_engine import evaluate

def generate_summary(ticker, indicators):
    result=evaluate(
        rsi=indicators.get("RSI"),
        macd=indicators.get("MACD"),
        price=indicators.get("PRICE"),
        sma=indicators.get("SMA")
    )
    lines=[
        f"Ticker: {ticker}",
        f"Signal: {result['action']}",
        f"Confidence: {result['confidence']}%",
        "Reasons:"
    ]
    lines.extend(f"- {r}" for r in result["reasons"])
    return "\n".join(lines), result
