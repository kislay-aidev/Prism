import yfinance as yf

def fetch(ticker):
    try:
        return yf.Ticker(ticker).financials
    except Exception:
        return None
