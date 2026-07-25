from .cost_basis import average_cost
def unrealized(transactions,prices):
    out=[]
    syms={t["symbol"] for t in transactions}
    for s in syms:
        avg=average_cost(transactions,s)
        qty=sum(t["qty"] if t["side"]=="BUY" else -t["qty"] for t in transactions if t["symbol"]==s)
        cur=prices.get(s,avg)
        out.append({"Ticker":s,"Qty":qty,"Avg Cost":avg,"Current":cur,"PnL":round((cur-avg)*qty,2)})
    return out
