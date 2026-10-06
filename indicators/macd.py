def calculate(close,fast=12,slow=26,signal=9):
    f=close.ewm(span=fast,adjust=False).mean()
    s=close.ewm(span=slow,adjust=False).mean()
    m=f-s
    sig=m.ewm(span=signal,adjust=False).mean()
    return {"macd":m,"signal":sig,"histogram":m-sig}
