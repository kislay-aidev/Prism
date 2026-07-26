from __future__ import annotations

import time
import pandas as pd
import yfinance as yf
from core.exceptions import DataFetchError


def _download(ticker: str, start=None, end=None) -> pd.DataFrame:
    last_error = None
    for _ in range(3):
        try:
            df = yf.download(
                ticker,
                start=start,
                end=end,
                progress=False,
                auto_adjust=False,
                multi_level_index=False,
            )
            if not df.empty:
                return df
        except Exception as exc:
            last_error = exc
            time.sleep(1)
    raise DataFetchError(f"Failed to fetch '{ticker}'. {last_error}")


def _company_info(ticker: str) -> dict:
    try:
        return yf.Ticker(ticker).info or {}
    except Exception:
        return {}


def download(ticker: str, start=None, end=None) -> pd.DataFrame:
    return _download(ticker, start, end)


def company_info(ticker: str) -> dict:
    return _company_info(ticker)
