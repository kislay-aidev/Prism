from .engine import StockDataEngine

def download_many(symbols, start=None, end=None):
    engine = StockDataEngine()
    result = {}
    for symbol in symbols:
        try:
            result[symbol] = engine.download(symbol, start, end)
        except Exception:
            result[symbol] = None
    return result
