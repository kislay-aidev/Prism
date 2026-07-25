def exposure(rows):
    total=sum(max(r["Current"]*r["Qty"],0) for r in rows) or 1
    return [{"Ticker":r["Ticker"],"Exposure %":round((r["Current"]*r["Qty"])/total*100,2)} for r in rows]
