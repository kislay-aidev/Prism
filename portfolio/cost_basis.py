def average_cost(transactions,symbol):
    qty=0;cost=0
    for t in transactions:
        if t["symbol"]!=symbol: continue
        if t["side"]=="BUY":
            qty+=t["qty"]; cost+=t["qty"]*t["price"]
        elif qty:
            avg=cost/qty
            qty-=t["qty"]; cost-=avg*t["qty"]
    return 0 if qty==0 else round(cost/qty,2)
