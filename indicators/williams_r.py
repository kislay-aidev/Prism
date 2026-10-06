def calculate(df,period=14):
    hh=df.High.rolling(period).max()
    ll=df.Low.rolling(period).min()
    return -100*((hh-df.Close)/(hh-ll))
