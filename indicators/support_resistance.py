def calculate(df,window=20):
    return {"support":df.Low.rolling(window).min(),"resistance":df.High.rolling(window).max()}
