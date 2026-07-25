import streamlit as st
from datetime import date, datetime
from zoneinfo import ZoneInfo

from core.settings import settings
from core.state import initialize
from ui.theme import inject_theme_css
from ui.theme import select_theme
from core.market import MarketClock

from dashboard.home import render as render_header
from dashboard.sidebar import controls
from dashboard.integration import load

from charts.candlestick import build as candlestick
from charts.ohlc import build as ohlc
from charts.line import build as line
from charts.area import build as area
from charts.volume import build as volume
from charts.panels import rsi_chart, macd_chart

from news.renderer import render as news_render
from financials.dashboard import build as financial_dashboard
from portfolio.dashboard import build as portfolio_dashboard
from ai.dashboard import build as ai_dashboard
from ai.rating import stars
from ai.risk import label as risk_label

from ui.metric_cards import render as render_metrics
from ui.status_bar import render as render_status

initialize()
st.set_page_config(
    page_title=settings.APP_NAME,
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_theme_css()
render_header()

with st.sidebar:
    st.markdown("## Navigation")
    page = st.radio(
        "View",
        ["Dashboard", "Technical Analysis", "Financials", "News", "Portfolio", "AI Insights"],
        label_visibility="collapsed",
    )
    st.divider()
    select_theme()

market = MarketClock()
status = market.status()
clock_indicator = "🟢" if status["open"] else "🔴"
st.sidebar.success(f"{clock_indicator} Market {status['reason']}")
st.sidebar.caption(status["time"].strftime("%Y-%m-%d %H:%M %Z"))

ui = controls()

if page == "Dashboard":
    st.subheader("Market Overview")
    df, info = load(ui["ticker"], date(2023, 1, 1), date.today())

    if df is None or df.empty:
        st.error(f"No data available for {ui['ticker']}")
        st.stop()

    latest = df.iloc[-1]
    prev = df.iloc[-2] if len(df) > 1 else latest
    change = ((latest.Close - prev.Close) / prev.Close) * 100

    render_metrics(
        {
            "Price": f"${latest.Close:.2f}",
            "Change": f"{change:+.2f}%",
            "Volume": f"{latest.Volume:,.0f}",
            "High": f"${latest.High:.2f}",
            "Low": f"${latest.Low:.2f}",
            "Open": f"${latest.Open:.2f}",
            "RSI (14)": f"{latest.get('RSI', 0):.1f}",
            "ATR": f"{latest.get('ATR', 0):.2f}",
        },
        cols=4,
    )

    chart_map = {
        "Candlestick": candlestick,
        "OHLC": ohlc,
        "Line": line,
        "Area": area,
    }
    fig = chart_map.get(ui["chart"], candlestick)(df, ui["ticker"])
    st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(volume(df), use_container_width=True)
    with col2:
        st.plotly_chart(rsi_chart(df), use_container_width=True)

elif page == "Technical Analysis":
    st.subheader("Technical Analysis")
    df, info = load(ui["ticker"], date(2023, 1, 1), date.today())
    if df is None or df.empty:
        st.error(f"No data available for {ui['ticker']}")
        st.stop()

    chart_map = {
        "Candlestick": candlestick,
        "OHLC": ohlc,
        "Line": line,
        "Area": area,
    }
    fig = chart_map.get(ui["chart"], candlestick)(df, ui["ticker"])
    st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(rsi_chart(df), use_container_width=True)
    with col2:
        st.plotly_chart(macd_chart(df), use_container_width=True)

    with st.expander("Indicator Values", expanded=False):
        latest = df.iloc[-1]
        ind_data = {
            "RSI (14)": f"{latest.get('RSI', 0):.2f}",
            "MACD": f"{latest.get('MACD', 0):.4f}",
            "Signal": f"{latest.get('Signal', 0):.4f}",
            "ADX (14)": f"{latest.get('ADX', 0):.2f}",
            "ATR (14)": f"{latest.get('ATR', 0):.2f}",
            "SMA (20)": f"${latest.get('SMA20', 0):.2f}",
            "SMA (50)": f"${latest.get('SMA50', 0):.2f}",
            "EMA (20)": f"${latest.get('EMA20', 0):.2f}",
        }
        render_metrics(ind_data, cols=4)

elif page == "Financials":
    st.subheader("Company Intelligence")
    df, info = load(ui["ticker"], date(2023, 1, 1), date.today())
    if not info:
        st.warning("No financial data available")
        st.stop()

    fin = financial_dashboard(info)
    if isinstance(fin, dict):
        for key, value in fin.items():
            m = st.metric if isinstance(value, (int, float)) else st.write
            if isinstance(value, (int, float)):
                st.metric(key.replace("_", " ").title(), f"{value:,.2f}" if isinstance(value, float) else str(value))
            else:
                st.write(f"**{key.replace('_', ' ').title()}**: {value}")

elif page == "News":
    st.subheader("News Intelligence")
    news_render(ui["ticker"])

elif page == "Portfolio":
    st.subheader("Portfolio Overview")
    df, _ = load(ui["ticker"], date(2023, 1, 1), date.today())
    if df is not None and not df.empty:
        price = float(df.Close.iloc[-1])
        result = portfolio_dashboard({ui["ticker"]: price})
        if isinstance(result, dict):
            for key, value in result.items():
                st.metric(key.replace("_", " ").title(), value)
    else:
        st.info("Add positions to your portfolio to see analytics")

elif page == "AI Insights":
    st.subheader("AI-Powered Analysis")
    df, info = load(ui["ticker"], date(2023, 1, 1), date.today())
    if df is None or df.empty:
        st.error(f"No data available for {ui['ticker']}")
        st.stop()

    latest = df.iloc[-1]
    indicators = {
        "RSI": float(latest["RSI"]) if "RSI" in latest else 50,
        "MACD": float(latest["MACD"]) if "MACD" in latest else 0,
        "Signal": float(latest["Signal"]) if "Signal" in latest else 0,
        "ADX": float(latest["ADX"]) if "ADX" in latest else 20,
        "ATR": float(latest["ATR"]) if "ATR" in latest else 0,
        "SMA20": float(latest["SMA20"]) if "SMA20" in latest else 0,
        "SMA50": float(latest["SMA50"]) if "SMA50" in latest else 0,
        "Close": float(latest.Close),
        "BB_Position": float(latest["BB_Position"]) if "BB_Position" in latest else 0,
        "OBV": float(latest["OBV"]) if "OBV" in latest else 0,
    }

    analysis = ai_dashboard(ui["ticker"], indicators, float(latest.Close))

    col1, col2, col3 = st.columns(3)
    rec = analysis.get("recommendation", {})
    col1.metric("Recommendation", rec.get("action", "HOLD"))
    col2.metric("Confidence", f"{rec.get('confidence', 0)}%")
    col3.metric("Risk Level", risk_label(analysis.get("risk", "Medium")))

    st.markdown(f"### Rating {analysis.get('rating', '☆☆☆☆☆')}")

    targets = analysis.get("targets", {})
    if targets:
        st.subheader("Price Targets")
        tcol1, tcol2, tcol3, tcol4 = st.columns(4)
        tcol1.metric("Entry", f"${targets.get('entry', 0):.2f}")
        tcol2.metric("Stop Loss", f"${targets.get('stop_loss', 0):.2f}")
        tcol3.metric("Target 1", f"${targets.get('target_1', 0):.2f}")
        tcol4.metric("Target 2", f"${targets.get('target_2', 0):.2f}")

    reasons = rec.get("reasons", [])
    if reasons:
        st.subheader("Signal Details")
        for r in reasons:
            st.markdown(f"- {r}")

render_status(f"{clock_indicator} {status['reason']}", ui["ticker"])
