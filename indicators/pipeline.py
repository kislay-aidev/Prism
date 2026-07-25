from .moving_averages import sma, ema
from .rsi import calculate as rsi
from .macd import calculate as macd
from .bollinger import calculate as bb
from .atr import calculate as atr
from .obv import calculate as obv
from .adx import calculate as adx


def apply(df):
    df = df.copy()
    close = df.Close
    df["SMA20"] = sma(close, 20)
    df["SMA50"] = sma(close, 50)
    df["EMA20"] = ema(close, 20)
    df["RSI"] = rsi(close)

    m = macd(close)
    df["MACD"] = m["macd"]
    df["Signal"] = m["signal"]
    df["Histogram"] = m["histogram"]

    b = bb(close)
    df["BB_Middle"] = b["middle"]
    df["BB_Upper"] = b["upper"]
    df["BB_Lower"] = b["lower"]

    latest = close.iloc[-1]
    upper = df["BB_Upper"].iloc[-1]
    lower = df["BB_Lower"].iloc[-1]
    middle = df["BB_Middle"].iloc[-1]
    if middle and middle != 0:
        df["BB_Position"] = (latest - middle) / (upper - lower) * 2
    else:
        df["BB_Position"] = 0.0

    df["ATR"] = atr(df)
    df["OBV"] = obv(df)
    df["ADX"] = adx(df)

    return df
