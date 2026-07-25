import pandas as pd
def summary(holdings,prices):
    rows=[]
    total=0
    for h in holdings:
        cur=prices.get(h["symbol"],h["price"])
        val=cur*h["qty"]
        cost=h["price"]*h["qty"]
        pnl=val-cost
        total+=val
        rows.append({"Ticker":h["symbol"],"Qty":h["qty"],"Cost":cost,"Value":val,"PnL":pnl})
    return pd.DataFrame(rows),total
