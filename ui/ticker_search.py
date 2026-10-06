from __future__ import annotations

import streamlit as st

from core.state import get_state
from data.ticker_repository import get_repository


def render_ticker_search(
    key: str = "ticker_search",
    placeholder: str = "Search companies or tickers",
    max_suggestions: int = 8,
) -> None:
    state = get_state()
    repo = get_repository()
    input_key = f"{key}_input"

    if state.search_display:
        st.session_state[input_key] = state.search_display
        state.search_display = ""

    typed = st.text_input(
        "Search",
        key=input_key,
        placeholder=placeholder,
        label_visibility="collapsed",
    )

    recent = state.recent_tickers[:5]
    if recent:
        st.markdown(f'<div class="search-recent-label">Recent</div>', unsafe_allow_html=True)
        cols = st.columns(len(recent))
        for i, symbol in enumerate(recent):
            if cols[i].button(
                symbol,
                key=f"{key}_recent_{i}_{symbol}",
                use_container_width=True,
            ):
                record = repo.lookup(symbol)
                if record:
                    state.search_display = f"{record['name']} ({symbol})"
                state.select_ticker(symbol)
                st.rerun()

    query = typed.strip()
    if not query:
        return

    suggestions = repo.search(query, limit=max_suggestions)
    if not suggestions:
        st.markdown(
            f'<div class="search-no-matches">No matches for \'{query}\'</div>',
            unsafe_allow_html=True,
        )
        return

    st.markdown('<div class="search-results">', unsafe_allow_html=True)
    for idx, record in enumerate(suggestions):
        symbol = record["symbol"]
        name = record["name"]
        exchange = record["exchange"]
        label = f"**{name}**\n\n{symbol} \u2022 {exchange}"

        if st.button(
            label,
            key=f"{key}_result_{idx}_{symbol}",
            use_container_width=True,
            type="secondary",
        ):
            state.search_display = f"{name} ({symbol})"
            state.select_ticker(symbol)
            st.rerun()

        if idx < len(suggestions) - 1:
            st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


def render_add_symbol_search(
    key: str,
    placeholder: str = "Add symbol...",
    max_suggestions: int = 6,
    exclude: list[str] | None = None,
) -> str | None:
    exclude_set = {s.strip().upper() for s in (exclude or [])}
    repo = get_repository()

    typed = st.text_input(
        "",
        key=f"{key}_query",
        placeholder=placeholder,
        label_visibility="collapsed",
    )
    query = typed.strip().upper()
    if not query:
        return None

    suggestions = repo.search(query, limit=max_suggestions)
    for idx, record in enumerate(suggestions):
        symbol = record["symbol"]
        if symbol in exclude_set:
            continue
        name = record["name"]
        exchange = record["exchange"]

        if st.button(
            f"{name} ({symbol} \u2022 {exchange})",
            key=f"{key}_add_{idx}_{symbol}",
            use_container_width=True,
        ):
            return symbol

    return None
