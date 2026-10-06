import pandas as pd

def sma(s,w):
    return s.rolling(w).mean()

def ema(s,w):
    return s.ewm(span=w).mean()
