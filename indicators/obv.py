def calculate(df):
    obv=[0]
    for i in range(1,len(df)):
        c=df.Close.iloc[i]-df.Close.iloc[i-1]
        obv.append(obv[-1]+(df.Volume.iloc[i] if c>0 else -df.Volume.iloc[i] if c<0 else 0))
    return obv
