import yfinance as yf

def fetch(ticker):
    try:
        return yf.Ticker(ticker).balance_sheet
    except Exception:
        return None
