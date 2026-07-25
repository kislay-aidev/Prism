import pandas as pd
def calculate(df,period=14):
    tr=pd.concat([(df.High-df.Low),(df.High-df.Close.shift()).abs(),(df.Low-df.Close.shift()).abs()],axis=1).max(axis=1)
    return tr.rolling(period).mean()
