from __future__ import annotations

import streamlit as st

from ai.dashboard import build as ai_dashboard
from ai.risk import label as risk_label
from charts import CHART_NAMES, get_renderer
from charts.panels import normalized_comparison_chart
from core.state import AVAILABLE_INDICATORS, get_state
from dashboard.integration import safe_load
from ui.theme import render_theme_switcher_compact
from ui.ticker_search import render_add_symbol_search


def render_symbol_collection_editor(
    title: str,
    symbols: list[str],
    remove_key_prefix: str,
    search_key: str,
    placeholder: str,
    on_remove,
    on_add,
    empty_message: str,
    exclude: list[str] | None = None,
    clear_action=None,
    clear_label: str = "Clear all",
) -> None:
    with st.expander(title, expanded=False):
        if symbols:
            for symbol in symbols:
                name_col, action_col = st.columns([4, 1])
                name_col.markdown(f"**{symbol}**")
                if action_col.button("Remove", key=f"{remove_key_prefix}_{symbol}", width="stretch"):
                    on_remove(symbol)
                    st.rerun()
        else:
            st.caption(empty_message)

        selected_symbol = render_add_symbol_search(
            search_key,
            placeholder=placeholder,
            exclude=exclude or symbols,
        )
        if selected_symbol:
            on_add(selected_symbol)
            st.rerun()

        if clear_action and symbols and st.button(clear_label, key=f"{search_key}_clear", type="secondary", width="stretch"):
            clear_action()
            st.rerun()


def render_selectable_symbol_panel(
    title: str,
    symbols: list[str],
    selected_symbol: str | None,
    selection_key: str,
    add_search_key: str,
    placeholder: str,
    empty_message: str,
    on_select,
    on_remove,
    on_add,
    exclude: list[str] | None = None,
) -> str | None:
    with st.expander(title, expanded=False):
        current_selection = selected_symbol
        if symbols:
            current_selection = st.radio(
                title,
                symbols,
                index=symbols.index(selected_symbol) if selected_symbol in symbols else 0,
                label_visibility="collapsed",
                key=selection_key,
            )
            load_col, remove_col = st.columns(2)
            if load_col.button("Load", key=f"{selection_key}_load", width="stretch"):
                on_select(current_selection)
                st.rerun()
            if remove_col.button("Remove", key=f"{selection_key}_remove", width="stretch"):
                on_remove(current_selection)
                st.rerun()
        else:
            st.caption(empty_message)

        selected_symbol_to_add = render_add_symbol_search(
            add_search_key,
            placeholder=placeholder,
            exclude=exclude or symbols,
        )
        if selected_symbol_to_add:
            on_add(selected_symbol_to_add)
            st.rerun()

        return current_selection


def render_ai_signals_view(ticker: str, latest, df) -> None:
    st.subheader("Signals", divider=False)

    indicators = {
        "RSI": float(latest.get("RSI", 50) or 50),
        "MACD": float(latest.get("MACD", 0) or 0),
        "Signal": float(latest.get("Signal", 0) or 0),
        "ADX": float(latest.get("ADX", 20) or 20),
        "ATR": float(latest.get("ATR", 0) or 0),
        "SMA20": float(latest.get("SMA20", 0) or 0),
        "SMA50": float(latest.get("SMA50", 0) or 0),
        "Close": float(latest.Close),
        "BB_Position": float(latest.get("BB_Position", 0) or 0),
        "OBV": float(latest.get("OBV", 0) or 0),
        "Beta": float(latest.get("Beta", 1.0) or 1.0),
    }

    analysis = ai_dashboard(ticker, indicators, float(latest.Close))
    rec = analysis.get("recommendation", {})
    targets = analysis.get("targets", {})

    cols = st.columns(5)
    cols[0].metric("Signal", str(rec.get("action", "HOLD")))
    cols[1].metric("Confidence", f"{float(rec.get('confidence', 0) or 0):.0f}%")
    cols[2].metric("Risk", risk_label(analysis.get("risk", "Medium")))
    cols[3].metric("Entry", f"${float(targets.get('entry', 0) or 0):.2f}")
    cols[4].metric("Stop", f"${float(targets.get('stop_loss', 0) or 0):.2f}")

    detail_cols = st.columns(3)
    detail_cols[0].metric("Target 1", f"${float(targets.get('target_1', 0) or 0):.2f}")
    detail_cols[1].metric("Target 2", f"${float(targets.get('target_2', 0) or 0):.2f}")
    detail_cols[2].metric("Risk/Reward", f"1:{float(targets.get('risk_reward_1', 0) or 0):.1f}")

    reasons = rec.get("reasons", [])
    if reasons:
        st.markdown("**Signals**")
        for reason in reasons:
            st.markdown(f"- {reason}")

    score = analysis.get("score", {})
    if score:
        normalized = float(score.get("normalized", 0) or 0)
        details = score.get("details", {})
        st.markdown("**Technical Score**")
        score_cols = st.columns(1 + len(details))
        score_cols[0].metric("Overall", f"{normalized:.0%}")
        for idx, (name, value) in enumerate(details.items(), start=1):
            scalar = value.get("value", 0) if isinstance(value, dict) else value
            score_cols[idx].metric(str(name), f"{float(scalar or 0):.1f}")

    summary = analysis.get("summary", "")
    if summary:
        with st.expander("AI Analysis Summary", expanded=False):
            st.markdown(summary)


def render_compare_view(df, ticker: str) -> None:
    state = get_state()
    st.subheader("Comparison", divider=False)

    comparison_symbols = state.comparison_symbols
    if not comparison_symbols:
        st.info("Add symbols to compare from the sidebar or settings.")
        return

    chart_fn = get_renderer(state.chart_type)
    symbols = [ticker] + comparison_symbols
    cols = st.columns(min(len(symbols), 3))

    for idx, symbol in enumerate(symbols):
        with cols[idx % len(cols)]:
            st.markdown(f"**{symbol}{' (Primary)' if symbol == ticker else ''}**")
            if symbol == ticker:
                current_df = df
                load_error = None
            else:
                current_df, _, load_error = safe_load(symbol)
            if load_error or current_df is None or current_df.empty:
                st.error(load_error or f"No data for {symbol}")
                continue
            st.plotly_chart(chart_fn(current_df, symbol), width="stretch", config={"scrollZoom": True})

    st.divider()
    comparison_chart = normalized_comparison_chart(symbols)
    if comparison_chart and comparison_chart.data:
        st.plotly_chart(comparison_chart, width="stretch")
    else:
        st.info("Unable to generate comparison chart")


def render_settings_view() -> None:
    state = get_state()
    st.subheader("Settings", divider=False)

    with st.expander("Display", expanded=True):
        st.caption("Theme")
        render_theme_switcher_compact()
        chart_type = st.selectbox(
            "Default Chart Type",
            CHART_NAMES,
            index=CHART_NAMES.index(state.chart_type),
            key=state.widget_key("settings_chart_type"),
        )
        state.chart_type = chart_type

        interval_options = ["1d", "1wk", "1mo"]
        interval = st.selectbox(
            "Default Interval",
            interval_options,
            index=interval_options.index(state.interval),
            key=state.widget_key("settings_interval"),
        )
        state.interval = interval

        range_options = ["1mo", "3mo", "6mo", "1y", "2y", "5y", "max"]
        date_range = st.selectbox(
            "Default Date Range",
            range_options,
            index=range_options.index(state.date_range),
            key=state.widget_key("settings_date_range"),
        )
        state.date_range = date_range

    with st.expander("Indicators", expanded=True):
        selected = st.multiselect(
            "Enabled Indicators",
            AVAILABLE_INDICATORS,
            default=state.enabled_indicators,
            key=state.widget_key("settings_indicators"),
        )
        state.enabled_indicators = selected

    render_symbol_collection_editor(
        "Watchlist",
        state.watchlist,
        "settings_watch_remove",
        state.widget_key("settings_watchlist_search"),
        "Add watchlist symbol",
        state.remove_from_watchlist,
        state.add_to_watchlist,
        "No watchlist symbols yet.",
    )

    render_symbol_collection_editor(
        "Favorites",
        state.favorites,
        "settings_favorite_remove",
        state.widget_key("settings_favorites_search"),
        "Add favorite",
        state.remove_favorite,
        state.add_favorite,
        "No favorites yet.",
    )

    render_symbol_collection_editor(
        "Comparison",
        state.comparison_symbols,
        "settings_compare_remove",
        state.widget_key("settings_comparison_search"),
        "Add comparison symbol",
        state.remove_comparison_symbol,
        state.add_comparison_symbol,
        "No comparison symbols.",
        exclude=[state.ticker, *state.comparison_symbols],
        clear_action=state.clear_comparison,
        clear_label="Clear comparison list",
    )

    with st.expander("AI Settings", expanded=False):
        ai = state.ai_settings
        model_options = ["default", "gpt-4", "gpt-3.5-turbo", "claude-3"]
        state.update_ai_setting(
            "model",
            st.selectbox(
                "Model",
                model_options,
                index=model_options.index(ai.model),
                key=state.widget_key("settings_ai_model"),
            ),
        )
        state.update_ai_setting(
            "confidence_threshold",
            st.slider(
                "Confidence Threshold",
                0,
                100,
                ai.confidence_threshold,
                key=state.widget_key("settings_ai_confidence"),
            ),
        )
        risk_options = ["low", "medium", "high"]
        state.update_ai_setting(
            "risk_tolerance",
            st.selectbox(
                "Risk Tolerance",
                risk_options,
                index=risk_options.index(ai.risk_tolerance),
                key=state.widget_key("settings_ai_risk"),
            ),
        )
        state.update_ai_setting(
            "include_news_sentiment",
            st.checkbox(
                "Include News Sentiment",
                value=ai.include_news_sentiment,
                key=state.widget_key("settings_ai_news"),
            ),
        )

    with st.expander("Danger Zone", expanded=False):
        if st.button("Reset all settings", type="secondary", key=state.widget_key("settings_reset"), width="stretch"):
            state.reset_all()
            st.rerun()
