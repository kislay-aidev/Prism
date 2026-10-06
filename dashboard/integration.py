import streamlit as st
import yfinance as yf
from data.engine import download as raw_download
from data.engine import company_info as raw_info
from indicators.pipeline import apply
from core.exceptions import DataFetchError


@st.cache_data(ttl=300, show_spinner=False)
def download(ticker: str, start=None, end=None):
    return raw_download(ticker, start, end)


@st.cache_data(ttl=3600, show_spinner=False)
def company_info(ticker: str):
    return raw_info(ticker)


def load(symbol, start=None, end=None):
    df = download(symbol, start, end)
    enriched = apply(df)
    info = company_info(symbol)
    return enriched, info


def safe_load(symbol: str, start=None, end=None):
    try:
        df, info = load(symbol, start, end)
        if df is None or df.empty:
            return None, {}, f"No market data is available for {symbol}."
        return df, info or {}, None
    except DataFetchError:
        return None, {}, f"Unable to fetch market data for {symbol} right now."
    except Exception:
        return None, {}, f"Something went wrong while loading data for {symbol}."


@st.cache_data(ttl=60, show_spinner=False)
def current_price(symbol: str) -> float:
    try:
        p = yf.Ticker(symbol).history(period="1d")
        if not p.empty:
            return float(p.Close.iloc[-1])
    except Exception:
        pass
    return 0.0
