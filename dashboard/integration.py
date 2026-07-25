from data.engine import StockDataEngine
from indicators.pipeline import apply

engine=StockDataEngine()

def load(symbol,start=None,end=None):
    df=engine.download(symbol,start,end)
    return apply(df),engine.company_info(symbol)
