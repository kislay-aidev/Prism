import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from ai.scoring import score


def test_score_rsi_oversold():
    ind = {"RSI": 25, "MACD": 0, "Signal": 0}
    s, reasons = score(ind)
    assert s > 0, "Oversold RSI should produce positive score"
    assert any("oversold" in r.lower() for r in reasons)


def test_score_rsi_overbought():
    ind = {"RSI": 75, "MACD": 0, "Signal": 0}
    s, reasons = score(ind)
    assert s < 0, "Overbought RSI should produce negative score"
    assert any("overbought" in r.lower() for r in reasons)


def test_score_macd_bullish():
    ind = {"RSI": 50, "MACD": 1, "Signal": 0}
    s, reasons = score(ind)
    assert any("bullish" in r.lower() for r in reasons)


def test_score_adx_trending():
    ind = {"RSI": 50, "MACD": 0, "Signal": 0, "ADX": 35}
    s, _ = score(ind)
    assert s != 0, "Strong ADX should impact score"


def test_empty_indicators():
    s, reasons = score({})
    assert s == 0, "Empty indicators should yield zero score"
    assert len(reasons) == 0


def test_none_indicators():
    s, reasons = score({"RSI": None, "MACD": None})
    assert s == 0, "None values should be handled gracefully"


if __name__ == "__main__":
    test_score_rsi_oversold()
    test_score_rsi_overbought()
    test_score_macd_bullish()
    test_score_adx_trending()
    test_empty_indicators()
    test_none_indicators()
    print("All AI tests passed")
