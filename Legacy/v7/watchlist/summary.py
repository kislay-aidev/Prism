import pandas as pd
from data.data_fetcher import fetch_price_data

def build_summary(symbols, start, end):
    rows=[]
    for s in symbols:
        df=fetch_price_data(s,start,end)
        if df.empty:
            continue
        last=df.Close.iloc[-1]
        prev=df.Close.iloc[-2] if len(df)>1 else last
        chg=((last-prev)/prev)*100
        rows.append({
            "Ticker":s,
            "Price":round(last,2),
            "Change%":round(chg,2),
            "Volume":int(df.Volume.iloc[-1]),
            "52W High":round(df.Close.max(),2),
            "52W Low":round(df.Close.min(),2)
        })
    return pd.DataFrame(rows)
