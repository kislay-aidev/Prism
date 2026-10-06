import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from reports.technical_report import build as technical_build
from reports.financial_report import build as financial_build
from reports.portfolio_report import build as portfolio_build
from reports.executive_summary import build as executive_build
from reports.html_template import render as html_render


def test_technical_report():
    result = technical_build({"RSI": 30, "MACD": 1})
    assert result["status"] == "success"
    assert "RSI" in result["indicators"]


def test_technical_report_empty():
    result = technical_build({})
    assert result["status"] == "No data"


def test_financial_report():
    result = financial_build({"marketCap": 1000000000})
    assert result["status"] == "success"
    assert "B" in result["metrics"]["marketCap"]


def test_portfolio_report_empty():
    result = portfolio_build([])
    assert result["status"] == "empty"


def test_portfolio_report_with_positions():
    positions = [{"ticker": "AAPL", "value": 5000, "pnl": 200}]
    result = portfolio_build(positions)
    assert result["status"] == "active"
    assert result["summary"]["position_count"] == 1


def test_executive_summary():
    t = technical_build({"RSI": 50})
    f = financial_build({"marketCap": 1e9})
    p = portfolio_build([])
    result = executive_build(t, f, p)
    assert "technical" in result
    assert "financial" in result
    assert "portfolio" in result
    assert "overall" in result


def test_html_render():
    report = {"technical": {"RSI": "50.00"}}
    html = html_render(report)
    assert "<html>" in html
    assert "RSI" in html


if __name__ == "__main__":
    test_technical_report()
    test_technical_report_empty()
    test_financial_report()
    test_portfolio_report_empty()
    test_portfolio_report_with_positions()
    test_executive_summary()
    test_html_render()
    print("All report tests passed")
