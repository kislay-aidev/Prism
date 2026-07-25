from .atr import calculate as atr
def calculate(df,period=10,multiplier=3):
    a=atr(df,period)
    hl2=(df.High+df.Low)/2
    upper=hl2+multiplier*a
    lower=hl2-multiplier*a
    return {"upper":upper,"lower":lower}
