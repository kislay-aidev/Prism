import pandas as pd

def calculate(df, period=14):
    up=df.High.diff()
    down=-df.Low.diff()
    plus=up.where((up>down)&(up>0),0.0)
    minus=down.where((down>up)&(down>0),0.0)
    tr=pd.concat([(df.High-df.Low),(df.High-df.Close.shift()).abs(),(df.Low-df.Close.shift()).abs()],axis=1).max(axis=1)
    atr=tr.rolling(period).mean()
    pdi=100*(plus.rolling(period).mean()/atr)
    mdi=100*(minus.rolling(period).mean()/atr)
    dx=((pdi-mdi).abs()/(pdi+mdi))*100
    return dx.rolling(period).mean()
