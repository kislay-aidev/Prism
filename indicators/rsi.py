def calculate(close,period=14):
    d=close.diff()
    g=d.clip(lower=0).rolling(period).mean()
    l=(-d.clip(upper=0)).rolling(period).mean()
    rs=g/l
    return 100-(100/(1+rs))
