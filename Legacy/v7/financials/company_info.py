import yfinance as yf

def fetch(ticker):
    try:
        info=yf.Ticker(ticker).info
        return {k:info.get(k) for k in [
            "longName","sector","industry","marketCap","enterpriseValue",
            "priceToSalesTrailing12Months","priceToBook","forwardPE",
            "dividendYield","beta","fiftyTwoWeekHigh","fiftyTwoWeekLow"
        ]}
    except Exception:
        return {}
