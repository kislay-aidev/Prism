def evaluate(rsi=None, macd=None, price=None, sma=None):
    score=0
    reasons=[]
    if rsi is not None:
        if rsi<30:
            score+=2; reasons.append("RSI oversold — bullish")
        elif rsi>70:
            score-=2; reasons.append("RSI overbought — bearish")
    if macd is not None:
        if macd>0:
            score+=2; reasons.append("MACD positive — bullish")
        else:
            score-=2; reasons.append("MACD negative — bearish")
    if price is not None and sma is not None:
        if price>sma:
            score+=1; reasons.append("Price above SMA — bullish")
        else:
            score-=1; reasons.append("Price below SMA — bearish")
    if score>=3:
        action="BUY"
    elif score<=-3:
        action="SELL"
    else:
        action="HOLD"
    confidence=min(100,50+abs(score)*10)
    return {"action":action,"score":score,"confidence":confidence,"reasons":reasons}
