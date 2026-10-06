from .scoring import score


def recommend(indicators: dict) -> dict:
    score_val, reasons = score(indicators)

    if score_val >= 5:
        action = "STRONG_BUY"
    elif score_val >= 2:
        action = "BUY"
    elif score_val <= -5:
        action = "STRONG_SELL"
    elif score_val <= -2:
        action = "SELL"
    else:
        action = "HOLD"

    confidence = min(95, 50 + abs(score_val) * 8)

    return {
        "action": action,
        "score": score_val,
        "confidence": confidence,
        "reasons": reasons,
    }
