def weights(df):
    if df.empty:return df
    total=df["Value"].sum()
    df=df.copy()
    df["Allocation %"]=df["Value"]/total*100
    return df
