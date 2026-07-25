def score(indicators: dict):
    score_val = 0
    reasons = []

    rsi = indicators.get("RSI")
    if rsi is not None:
        if rsi < 30:
            score_val += 3
            reasons.append("RSI deeply oversold — strong bullish signal")
        elif rsi < 40:
            score_val += 2
            reasons.append("RSI approaching oversold — bullish bias")
        elif rsi > 70:
            score_val -= 3
            reasons.append("RSI deeply overbought — strong bearish signal")
        elif rsi > 60:
            score_val -= 2
            reasons.append("RSI approaching overbought — bearish bias")
        else:
            reasons.append("RSI neutral zone")

    macd = indicators.get("MACD")
    signal = indicators.get("Signal")
    if macd is not None and signal is not None:
        if abs(macd - signal) > 0.001:
            if macd > signal:
                score_val += 2
                reasons.append("MACD above signal line — bullish momentum")
            else:
                score_val -= 2
                reasons.append("MACD below signal line — bearish momentum")
        if abs(macd) > 0.001:
            if macd > 0:
                score_val += 1
                reasons.append("MACD positive — bullish trend confirmation")
            else:
                score_val -= 1
                reasons.append("MACD negative — bearish trend confirmation")

    adx = indicators.get("ADX")
    if adx is not None:
        if adx > 25:
            score_val += 1 if score_val >= 0 else -1
            if adx > 50:
                reasons.append(f"Very strong trend (ADX: {adx:.0f})")
            else:
                reasons.append(f"Strong trending market (ADX: {adx:.0f})")
        else:
            reasons.append(f"Weak/choppy market (ADX: {adx:.0f})")

    sma20 = indicators.get("SMA20")
    sma50 = indicators.get("SMA50")
    close = indicators.get("Close")
    if close is not None and sma20 is not None:
        if close > sma20:
            score_val += 1
            reasons.append("Price above 20-day SMA — short-term bullish")
        else:
            score_val -= 1
            reasons.append("Price below 20-day SMA — short-term bearish")
    if sma20 is not None and sma50 is not None:
        if sma20 > sma50:
            score_val += 2
            reasons.append("Golden cross (20 > 50 SMA) — bullish trend")
        else:
            score_val -= 2
            reasons.append("Death cross (20 < 50 SMA) — bearish trend")

    bb_position = indicators.get("BB_Position")
    if bb_position is not None:
        if bb_position > 1:
            score_val -= 1
            reasons.append("Price above upper Bollinger Band — overextended")
        elif bb_position < -1:
            score_val += 1
            reasons.append("Price below lower Bollinger Band — oversold bounce potential")

    obv = indicators.get("OBV")
    if obv is not None and close is not None:
        obv_value = obv
        if obv_value > 0:
            score_val += 1
            reasons.append("OBV rising — volume confirms uptrend")

    return score_val, reasons
