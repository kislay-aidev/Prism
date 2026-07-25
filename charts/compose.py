from .candlestick import build as candlestick
from .indicators_overlay import add_sma,add_ema,add_bollinger
from .signals import add_trade_markers

def build_complete(df):
    fig=candlestick(df,"Technical View")
    fig=add_sma(fig,df,"SMA20","SMA20")
    fig=add_ema(fig,df,"EMA20","EMA20")
    fig=add_bollinger(fig,df)
    buys=df[df.get("Crossover_Event")=="BUY"] if "Crossover_Event" in df else None
    sells=df[df.get("Crossover_Event")=="SELL"] if "Crossover_Event" in df else None
    return add_trade_markers(fig,buys,sells)
