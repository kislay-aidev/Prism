import pandas as pd
def sma(close,period=20): return close.rolling(period).mean()
def ema(close,period=20): return close.ewm(span=period,adjust=False).mean()
