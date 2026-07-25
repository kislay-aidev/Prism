def calculate(close, fast=12, slow=26, signal=9):
    e=close.ewm(span=fast).mean()
    m=close.ewm(span=slow).mean()
    macd=e-m
    sig=macd.ewm(span=signal).mean()
    hist=macd-sig
    return macd,sig,hist
