def balance_health(info):
    score=0
    if (info.get("currentRatio") or 0)>=1.5: score+=1
    if (info.get("debtToEquity") or 999)<100: score+=1
    if (info.get("returnOnEquity") or 0)>0.15: score+=1
    return {"health_score":score,"max_score":3}
