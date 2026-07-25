from .recommendation import recommend
from .portfolio_score import calculate as calculate_score
from .targets import suggest
from .risk import classify
from .rating import stars
from .summary import build as build_summary


def build(symbol: str, indicators: dict, price: float) -> dict:
    rec = recommend(indicators)
    score = calculate_score(indicators)
    tgt = suggest(price, indicators.get("ATR"))
    risk_level = classify(
        beta=indicators.get("Beta"),
        atr=indicators.get("ATR"),
    )
    return {
        "symbol": symbol,
        "price": price,
        "recommendation": rec,
        "score": score,
        "targets": tgt,
        "risk": risk_level,
        "rating": stars(rec["confidence"]),
        "summary": build_summary(symbol, indicators),
    }
