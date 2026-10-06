def calculate(df):
    tenkan=(df.High.rolling(9).max()+df.Low.rolling(9).min())/2
    kijun=(df.High.rolling(26).max()+df.Low.rolling(26).min())/2
    span_a=((tenkan+kijun)/2).shift(26)
    span_b=((df.High.rolling(52).max()+df.Low.rolling(52).min())/2).shift(26)
    return {"tenkan":tenkan,"kijun":kijun,"span_a":span_a,"span_b":span_b}
