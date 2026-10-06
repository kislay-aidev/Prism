from __future__ import annotations

from datetime import date

import streamlit as st

from ai.risk import label as risk_label
from charts import CHART_NAMES, get_renderer
from charts.panels import macd_chart, rsi_chart
from charts.volume import build as volume_chart
from core.market import MarketClock
from core.presentation import (
    flatten_financial_metrics,
    format_financial_value,
    resolve_start_date,
)
from core.settings import settings
from core.state import AVAILABLE_TABS, get_state, init
from dashboard.integration import current_price, safe_load
from financials.dashboard import build as financial_dashboard
from news.renderer import render as render_news
from ui.theme import inject_theme_css, render_theme_switcher_compact
from ui.ticker_search import render_add_symbol_search, render_ticker_search
from ui.views import (
    render_ai_signals_view,
    render_compare_view,
    render_selectable_symbol_panel,
    render_settings_view,
)


init()
state = get_state()
st.set_page_config(
    page_title=settings.APP_NAME,
    layout="wide",
    initial_sidebar_state="expanded",
)
inject_theme_css()


def render_sidebar() -> None:
    market_status = MarketClock().status()

    with st.sidebar:
        st.markdown("#### Prism")
        st.caption("Financial Intelligence Platform")
        st.divider()

        render_ticker_search(key="ticker_search")

        selected_tab = st.radio(
            "View",
            AVAILABLE_TABS,
            index=AVAILABLE_TABS.index(state.tab),
            label_visibility="collapsed",
            key=state.widget_key("sidebar_tab"),
        )
        state.tab = selected_tab

        selected_chart = st.selectbox(
            "Chart",
            CHART_NAMES,
            index=CHART_NAMES.index(state.chart_type),
            label_visibility="collapsed",
            key=state.widget_key("sidebar_chart_type"),
        )
        state.chart_type = selected_chart

        selected_indicators = st.multiselect(
            "Indicators",
            ["RSI", "MACD", "Volume"],
            default=[indicator for indicator in ["RSI", "MACD", "Volume"] if state.is_indicator_enabled(indicator)],
            key=state.widget_key("sidebar_indicators"),
        )
        state.enabled_indicators = [
            indicator
            for indicator in state.enabled_indicators
            if indicator not in {"RSI", "MACD", "Volume"}
        ] + selected_indicators

        st.divider()
        render_theme_switcher_compact()
        market_icon = "🟢" if market_status["open"] else "🔴"
        st.markdown(f"{market_icon} Market **{market_status['reason']}**")
        st.caption(market_status["time"].strftime("%H:%M %Z"))

        render_watchlist_section()
        render_favorites_section()
        render_comparison_section()
        render_ai_settings_section()


def render_watchlist_section() -> None:
    state.selected_watchlist_symbol = render_selectable_symbol_panel(
        "Watchlist",
        state.watchlist,
        state.selected_watchlist_symbol,
        state.widget_key("watchlist_selection"),
        state.widget_key("watchlist_add_search"),
        "Add watchlist symbol",
        "No watchlist symbols yet.",
        state.select_ticker,
        state.remove_from_watchlist,
        state.add_to_watchlist,
    )


def render_favorites_section() -> None:
    state.selected_favorite_symbol = render_selectable_symbol_panel(
        "Favorites",
        state.favorites,
        state.selected_favorite_symbol,
        state.widget_key("favorites_selection"),
        state.widget_key("favorites_add_search"),
        "Add favorite",
        "No favorites yet.",
        state.select_ticker,
        state.remove_favorite,
        state.add_favorite,
    )
    with st.sidebar:
        action_label = "Remove current ticker from favorites" if state.ticker in state.favorites else "Add current ticker to favorites"
        if st.button(action_label, key=state.widget_key("favorite_toggle_current"), width="stretch"):
            state.toggle_favorite(state.ticker)
            st.rerun()


def render_comparison_section() -> None:
    with st.sidebar.expander("Compare", expanded=False):
        if state.comparison_symbols:
            for symbol in state.comparison_symbols:
                label_col, action_col = st.columns([4, 1])
                label_col.markdown(f"**{symbol}**")
                if action_col.button("✕", key=state.widget_key(f"compare_remove_{symbol}"), width="stretch"):
                    state.remove_comparison_symbol(symbol)
                    st.rerun()
        else:
            st.caption("No comparison symbols.")

        added = render_add_symbol_search(
            state.widget_key("compare_add_search"),
            placeholder="Add comparison symbol",
            exclude=[state.ticker, *state.comparison_symbols],
        )
        if added:
            state.add_comparison_symbol(added)
            st.rerun()


def render_ai_settings_section() -> None:
    with st.sidebar.expander("AI Settings", expanded=False):
        ai_settings = state.ai_settings
        models = ["default", "gpt-4", "gpt-3.5-turbo", "claude-3"]
        model = st.selectbox(
            "Model",
            models,
            index=models.index(ai_settings.model),
            key=state.widget_key("sidebar_ai_model"),
        )
        state.update_ai_setting("model", model)

        confidence = st.slider(
            "Confidence Threshold",
            0,
            100,
            value=ai_settings.confidence_threshold,
            key=state.widget_key("sidebar_ai_confidence"),
        )
        state.update_ai_setting("confidence_threshold", confidence)

        risks = ["low", "medium", "high"]
        risk = st.selectbox(
            "Risk Tolerance",
            risks,
            index=risks.index(ai_settings.risk_tolerance),
            key=state.widget_key("sidebar_ai_risk"),
        )
        state.update_ai_setting("risk_tolerance", risk)

        include_news = st.checkbox(
            "Include News Sentiment",
            value=ai_settings.include_news_sentiment,
            key=state.widget_key("sidebar_ai_news"),
        )
        state.update_ai_setting("include_news_sentiment", include_news)


def render_header_metrics(df, ticker: str) -> None:
    latest = df.iloc[-1]
    previous = df.iloc[-2] if len(df) > 1 else latest
    change_pct = ((latest.Close - previous.Close) / previous.Close) * 100 if previous.Close else 0

    col_ticker, col_price, col_change, col_volume, col_high, col_low, col_open, _ = st.columns([1.2, 1, 1, 1.2, 1, 1, 1, 2])
    col_ticker.markdown(f"### {ticker}")
    col_price.metric("Price", f"${latest.Close:.2f}")
    col_change.metric("Change", f"{change_pct:+.2f}%", delta=f"{change_pct:+.2f}%")
    col_volume.metric("Volume", f"{latest.Volume:,.0f}")
    col_high.metric("High", f"${latest.High:.2f}")
    col_low.metric("Low", f"${latest.Low:.2f}")
    col_open.metric("Open", f"${latest.Open:.2f}")


def render_dashboard(df, ticker: str) -> None:
    chart_figure = get_renderer(state.chart_type)(df, ticker)
    st.plotly_chart(chart_figure, width="stretch", config={"scrollZoom": True})

    chart_columns = st.columns(3)
    if state.is_indicator_enabled("Volume"):
        with chart_columns[0]:
            st.plotly_chart(volume_chart(df), width="stretch")
    if state.is_indicator_enabled("RSI"):
        with chart_columns[1]:
            st.plotly_chart(rsi_chart(df), width="stretch")
    if state.is_indicator_enabled("MACD"):
        with chart_columns[2]:
            st.plotly_chart(macd_chart(df), width="stretch")


def render_financials(info: dict, ticker: str) -> None:
    st.subheader("Company", divider=False)
    if info:
        st.caption(f"{info.get('longName', ticker)} · {info.get('sector', 'N/A')} · {info.get('industry', 'N/A')}")
    metrics = financial_dashboard(info) if info else {}
    if not metrics:
        st.info("Financial data is not available for this symbol.")
        return
    flattened_metrics = flatten_financial_metrics(metrics)
    columns = st.columns(4)
    for idx, (label, value) in enumerate(flattened_metrics[:12]):
        columns[idx % 4].metric(label.replace("_", " ").title(), format_financial_value(label, value))


def render_portfolio(latest_close: float, ticker: str) -> None:
    st.subheader("Portfolio", divider=False)
    from portfolio.allocation import weights
    from portfolio.analytics import summary
    from portfolio.manager import load as load_holdings

    holdings = load_holdings()
    if not holdings:
        st.info("No holdings. Add positions via portfolio/portfolio.json")
        return

    prices: dict[str, float] = {}
    for symbol in {holding["symbol"] for holding in holdings}:
        prices[symbol] = float(latest_close) if symbol == ticker else current_price(symbol)

    portfolio_df, total_value = summary(holdings, prices)
    portfolio_df = weights(portfolio_df)
    total_cost = portfolio_df["Cost"].sum() if not portfolio_df.empty else 0
    total_pnl = total_value - total_cost
    return_pct = ((total_value / total_cost) - 1) * 100 if total_cost else 0

    col_value, col_pnl, col_holdings = st.columns(3)
    col_value.metric("Total Value", f"${total_value:,.2f}")
    col_pnl.metric("Total PnL", f"${total_pnl:,.2f}", delta=f"{return_pct:+.2f}%")
    col_holdings.metric("Holdings", str(len(holdings)))
    st.dataframe(portfolio_df, width="stretch")


render_sidebar()

ticker = state.ticker
today = date.today()
start_date = resolve_start_date(state.date_range, today)
df, info, load_error = safe_load(ticker, start_date, today)

if load_error:
    st.error(load_error)
    st.stop()

render_header_metrics(df, ticker)
latest = df.iloc[-1]

if state.tab == "Dashboard":
    render_dashboard(df, ticker)
elif state.tab == "Financials":
    render_financials(info, ticker)
elif state.tab == "News":
    st.subheader("News", divider=False)
    render_news(ticker)
elif state.tab == "AI Signals":
    render_ai_signals_view(ticker, latest, df)
elif state.tab == "Portfolio":
    render_portfolio(float(latest.Close), ticker)
elif state.tab == "Compare":
    render_compare_view(df, ticker)
elif state.tab == "Settings":
    render_settings_view()
