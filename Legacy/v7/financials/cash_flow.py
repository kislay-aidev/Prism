import yfinance as yf

def fetch(ticker):
    try:
        return yf.Ticker(ticker).cashflow
    except Exception:
        return None
