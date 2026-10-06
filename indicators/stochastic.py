def calculate(df,period=14):
    low=df.Low.rolling(period).min()
    high=df.High.rolling(period).max()
    k=((df.Close-low)/(high-low))*100
    d=k.rolling(3).mean()
    return {"k":k,"d":d}
