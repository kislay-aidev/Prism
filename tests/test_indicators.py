import sys
import os
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from indicators.rsi import calculate as rsi
from indicators.macd import calculate as macd
from indicators.bollinger import calculate as bb
from indicators.moving_averages import sma, ema
from indicators.atr import calculate as atr
from indicators.adx import calculate as adx


def _sample_df():
    return pd.DataFrame({
        "Open": [100, 102, 101, 103, 104],
        "High": [105, 104, 103, 106, 107],
        "Low": [98, 99, 100, 101, 102],
        "Close": [102, 101, 103, 104, 105],
        "Volume": [1000, 1200, 1100, 1300, 1400],
    })


def test_rsi_calculation():
    df = _sample_df()
    result = rsi(df.Close)
    assert len(result) == len(df), "RSI should match input length"


def test_macd_calculation():
    df = _sample_df()
    result = macd(df.Close)
    assert "macd" in result
    assert "signal" in result
    assert "histogram" in result


def test_bollinger_calculation():
    df = _sample_df()
    result = bb(df.Close)
    assert "middle" in result
    assert "upper" in result
    assert "lower" in result


def test_sma():
    df = _sample_df()
    result = sma(df.Close, 2)
    assert len(result) == len(df)


def test_ema():
    df = _sample_df()
    result = ema(df.Close, 2)
    assert len(result) == len(df)


def test_atr():
    df = _sample_df()
    result = atr(df)
    assert len(result) == len(df)


def test_adx():
    df = _sample_df()
    result = adx(df)
    assert len(result) == len(df)


if __name__ == "__main__":
    test_rsi_calculation()
    test_macd_calculation()
    test_bollinger_calculation()
    test_sma()
    test_ema()
    test_atr()
    test_adx()
    print("All indicator tests passed")
