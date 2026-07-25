def portfolio_return(df):
    if df.empty:return 0
    return round((df["PnL"].sum()/df["Cost"].sum())*100,2)
