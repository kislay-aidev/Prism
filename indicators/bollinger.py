def calculate(close,period=20,std=2):
    ma=close.rolling(period).mean()
    s=close.rolling(period).std()
    return {"middle":ma,"upper":ma+std*s,"lower":ma-std*s}
