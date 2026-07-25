from .health import balance_health

def score(info):
    h=balance_health(info)
    s=h["health_score"]*30
    if info.get("profitMargins"): s+=20
    if info.get("revenueGrowth"): s+=20
    if info.get("earningsGrowth"): s+=30
    return min(100,s)
