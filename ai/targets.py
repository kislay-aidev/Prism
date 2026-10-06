def suggest(price: float, atr: float = None) -> dict:
    atr = atr or price * 0.02
    return {
        "entry": round(price, 2),
        "stop_loss": round(price - 1.5 * atr, 2),
        "target_1": round(price + 2 * atr, 2),
        "target_2": round(price + 3 * atr, 2),
        "target_3": round(price + 5 * atr, 2),
        "risk_reward_1": round((2 * atr) / (1.5 * atr), 2),
        "risk_reward_2": round((3 * atr) / (1.5 * atr), 2),
    }
