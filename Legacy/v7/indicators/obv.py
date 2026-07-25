def calculate(df):
    obv=[0]
    for i in range(1,len(df)):
        if df.Close.iloc[i]>df.Close.iloc[i-1]:
            obv.append(obv[-1]+df.Volume.iloc[i])
        elif df.Close.iloc[i]<df.Close.iloc[i-1]:
            obv.append(obv[-1]-df.Volume.iloc[i])
        else:
            obv.append(obv[-1])
    return obv
