import yfinance as yf

def fetch(ticker):
    try:
        t=yf.Ticker(ticker)
        return {
            "annual":t.earnings,
            "quarterly":t.quarterly_earnings
        }
    except Exception:
        return {}
