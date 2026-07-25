from __future__ import annotations
import time
import pandas as pd
import yfinance as yf
from core.cache import cache
from core.exceptions import DataFetchError

class StockDataEngine:
    """Centralized data retrieval engine."""

    @cache(ttl=300)
    def download(self, ticker: str, start=None, end=None) -> pd.DataFrame:
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

    @cache(ttl=3600)
    def company_info(self, ticker: str) -> dict:
        try:
            return yf.Ticker(ticker).info or {}
        except Exception:
            return {}
