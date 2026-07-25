def calculate(df):
    return (df.Close*df.Volume).cumsum()/df.Volume.cumsum()
