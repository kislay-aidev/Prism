import yfinance as yf
import pandas as pd
from .cache import cache

@cache(ttl=300)
def fetch_price_data(ticker,start,end):
    data=yf.download(ticker,start=start,end=end,multi_level_index=False,progress=False)
    if isinstance(data,pd.DataFrame):
        return data
    return pd.DataFrame()

@cache(ttl=3600)
def fetch_company_info(ticker):
    try:
        return yf.Ticker(ticker).info or {}
    except Exception:
        return {}
