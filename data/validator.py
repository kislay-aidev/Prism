from core.exceptions import InvalidTickerError

def validate_ticker(symbol: str) -> str:
    symbol = symbol.strip().upper()
    if not symbol:
        raise InvalidTickerError("Ticker cannot be empty.")
    if not symbol.replace(".","").replace("-","").isalnum():
        raise InvalidTickerError(f"Invalid ticker: {symbol}")
    return symbol
