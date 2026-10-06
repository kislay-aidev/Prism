import yfinance as yf

def recommendations(ticker):
    try:
        return yf.Ticker(ticker).recommendations
    except Exception:
        return None
