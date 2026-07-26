import streamlit as st
from dataclasses import dataclass, field
from typing import Any, List, Optional


PREFIX = "app_"

DEFAULT_INDICATORS = ["RSI", "MACD", "Volume"]
AVAILABLE_INDICATORS = ["RSI", "MACD", "Volume", "Bollinger Bands", "ATR", "ADX", "OBV"]
AVAILABLE_THEMES = ["dark", "light", "amoled"]
# Must match charts.CHART_NAMES - the single source of truth for chart types
AVAILABLE_CHART_TYPES = ["Candlestick", "OHLC", "Line", "Area"]
AVAILABLE_TABS = [
    "Dashboard",
    "Financials",
    "News",
    "AI Signals",
    "Portfolio",
    "Compare",
    "Settings",
]

DEFAULTS = {
    "theme": "light",
    "ticker": "AAPL",
    "chart_type": "Candlestick",
    "tab": "Dashboard",
    "enabled_indicators": DEFAULT_INDICATORS,
    "watchlist": [],
    "recent_tickers": [],
    "favorites": [],
    "comparison_symbols": [],
    "ai_settings": {
        "model": "default",
        "confidence_threshold": 60,
        "risk_tolerance": "medium",
        "include_news_sentiment": True,
    },
    "selected_watchlist_symbol": None,
    "selected_favorite_symbol": None,
    "interval": "1d",
    "date_range": "1y",
    "search_query": "",
    "search_display": "",
}


def _key(name: str) -> str:
    return f"{PREFIX}{name}"


def init() -> None:
    for name, default in DEFAULTS.items():
        st.session_state.setdefault(_key(name), default)


def get(name: str, default: Any = None) -> Any:
    return st.session_state.get(_key(name), DEFAULTS.get(name, default))


def set(name: str, value: Any) -> None:
    st.session_state[_key(name)] = value


def widget_key(name: str) -> str:
    return _key(name)


def reset(*names: str) -> None:
    if not names:
        names = list(DEFAULTS.keys())
    for name in names:
        if name in DEFAULTS:
            st.session_state[_key(name)] = DEFAULTS[name]


@dataclass
class AIState:
    model: str = "default"
    confidence_threshold: int = 60
    risk_tolerance: str = "medium"
    include_news_sentiment: bool = True

    @classmethod
    def from_dict(cls, data: dict) -> "AIState":
        return cls(
            model=data.get("model", "default"),
            confidence_threshold=data.get("confidence_threshold", 60),
            risk_tolerance=data.get("risk_tolerance", "medium"),
            include_news_sentiment=data.get("include_news_sentiment", True),
        )

    def to_dict(self) -> dict:
        return {
            "model": self.model,
            "confidence_threshold": self.confidence_threshold,
            "risk_tolerance": self.risk_tolerance,
            "include_news_sentiment": self.include_news_sentiment,
        }


class AppState:
    _instance: Optional["AppState"] = None

    def __new__(cls) -> "AppState":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self) -> None:
        if self._initialized:
            return
        init()
        self._initialized = True

    @property
    def theme(self) -> str:
        return get("theme")

    @theme.setter
    def theme(self, value: str) -> None:
        if value in AVAILABLE_THEMES:
            set("theme", value)

    @property
    def ticker(self) -> str:
        return get("ticker").strip().upper() or "AAPL"

    @ticker.setter
    def ticker(self, value: str) -> None:
        set("ticker", value.strip().upper() or "AAPL")

    @property
    def chart_type(self) -> str:
        ct = get("chart_type")
        return ct if ct in AVAILABLE_CHART_TYPES else "Candlestick"

    @chart_type.setter
    def chart_type(self, value: str) -> None:
        if value in AVAILABLE_CHART_TYPES:
            set("chart_type", value)

    @property
    def tab(self) -> str:
        t = get("tab")
        return t if t in AVAILABLE_TABS else "Dashboard"

    @tab.setter
    def tab(self, value: str) -> None:
        if value in AVAILABLE_TABS:
            set("tab", value)

    @property
    def enabled_indicators(self) -> List[str]:
        indicators = get("enabled_indicators", DEFAULT_INDICATORS)
        return [i for i in indicators if i in AVAILABLE_INDICATORS]

    @enabled_indicators.setter
    def enabled_indicators(self, value: List[str]) -> None:
        valid = [i for i in value if i in AVAILABLE_INDICATORS]
        set("enabled_indicators", valid)

    def is_indicator_enabled(self, indicator: str) -> bool:
        return indicator in self.enabled_indicators

    def toggle_indicator(self, indicator: str) -> None:
        if indicator not in AVAILABLE_INDICATORS:
            return
        current = list(self.enabled_indicators)
        if indicator in current:
            current.remove(indicator)
        else:
            current.append(indicator)
        self.enabled_indicators = current

    @property
    def watchlist(self) -> List[str]:
        return list(get("watchlist", []))

    @watchlist.setter
    def watchlist(self, value: List[str]) -> None:
        set("watchlist", [s.strip().upper() for s in value if s.strip()])

    def add_to_watchlist(self, symbol: str) -> None:
        symbol = symbol.strip().upper()
        if not symbol:
            return
        current = self.watchlist
        if symbol not in current:
            current.append(symbol)
            self.watchlist = current
            if self.selected_watchlist_symbol is None:
                self.selected_watchlist_symbol = symbol

    def remove_from_watchlist(self, symbol: str) -> None:
        symbol = symbol.strip().upper()
        current = self.watchlist
        if symbol in current:
            current.remove(symbol)
            self.watchlist = current
            if self.selected_watchlist_symbol == symbol:
                self.selected_watchlist_symbol = current[0] if current else None

    @property
    def favorites(self) -> List[str]:
        return list(get("favorites", []))

    @favorites.setter
    def favorites(self, value: List[str]) -> None:
        set("favorites", [s.strip().upper() for s in value if s.strip()])

    def add_favorite(self, symbol: str) -> None:
        symbol = symbol.strip().upper()
        if not symbol:
            return
        current = self.favorites
        if symbol not in current:
            current.append(symbol)
            self.favorites = current
            if self.selected_favorite_symbol is None:
                self.selected_favorite_symbol = symbol

    def remove_favorite(self, symbol: str) -> None:
        symbol = symbol.strip().upper()
        current = self.favorites
        if symbol in current:
            current.remove(symbol)
            self.favorites = current
            if self.selected_favorite_symbol == symbol:
                self.selected_favorite_symbol = current[0] if current else None

    def toggle_favorite(self, symbol: str) -> None:
        symbol = symbol.strip().upper()
        if not symbol:
            return
        if symbol in self.favorites:
            self.remove_favorite(symbol)
        else:
            self.add_favorite(symbol)

    @property
    def recent_tickers(self) -> List[str]:
        return list(get("recent_tickers", []))

    def add_recent_ticker(self, symbol: str) -> None:
        symbol = symbol.strip().upper()
        if not symbol:
            return
        current = self.recent_tickers
        if symbol in current:
            current.remove(symbol)
        current.insert(0, symbol)
        set("recent_tickers", current[:10])

    @property
    def comparison_symbols(self) -> List[str]:
        return list(get("comparison_symbols", []))

    @comparison_symbols.setter
    def comparison_symbols(self, value: List[str]) -> None:
        set("comparison_symbols", [s.strip().upper() for s in value if s.strip()])

    def add_comparison_symbol(self, symbol: str) -> None:
        symbol = symbol.strip().upper()
        if not symbol or symbol == self.ticker:
            return
        current = self.comparison_symbols
        if symbol not in current:
            current.append(symbol)
            self.comparison_symbols = current[:5]

    def remove_comparison_symbol(self, symbol: str) -> None:
        symbol = symbol.strip().upper()
        current = self.comparison_symbols
        if symbol in current:
            current.remove(symbol)
            self.comparison_symbols = current

    def clear_comparison(self) -> None:
        set("comparison_symbols", [])

    def add_comparison(self, symbol: str) -> None:
        self.add_comparison_symbol(symbol)

    def remove_comparison(self, symbol: str) -> None:
        self.remove_comparison_symbol(symbol)

    @property
    def ai_settings(self) -> AIState:
        return AIState.from_dict(get("ai_settings", {}))

    @ai_settings.setter
    def ai_settings(self, value: AIState) -> None:
        set("ai_settings", value.to_dict())

    def update_ai_setting(self, key: str, value: Any) -> None:
        settings = self.ai_settings
        if hasattr(settings, key):
            setattr(settings, key, value)
            self.ai_settings = settings

    @property
    def selected_watchlist_symbol(self) -> Optional[str]:
        return get("selected_watchlist_symbol")

    @selected_watchlist_symbol.setter
    def selected_watchlist_symbol(self, value: Optional[str]) -> None:
        set("selected_watchlist_symbol", value.strip().upper() if value else None)

    @property
    def selected_favorite_symbol(self) -> Optional[str]:
        return get("selected_favorite_symbol")

    @selected_favorite_symbol.setter
    def selected_favorite_symbol(self, value: Optional[str]) -> None:
        set("selected_favorite_symbol", value.strip().upper() if value else None)

    @property
    def interval(self) -> str:
        return get("interval", "1d")

    @interval.setter
    def interval(self, value: str) -> None:
        set("interval", value)

    @property
    def date_range(self) -> str:
        return get("date_range", "1y")

    @date_range.setter
    def date_range(self, value: str) -> None:
        set("date_range", value)

    @property
    def search_query(self) -> str:
        return get("search_query", "")

    @search_query.setter
    def search_query(self, value: str) -> None:
        set("search_query", value)

    @property
    def search_display(self) -> str:
        return get("search_display", "")

    @search_display.setter
    def search_display(self, value: str) -> None:
        set("search_display", value)

    def widget_key(self, name: str) -> str:
        return widget_key(name)

    def reset_all(self) -> None:
        reset()

    def reset(self) -> None:
        self.reset_all()

    def select_ticker(self, symbol: str) -> None:
        normalized = symbol.strip().upper()
        if not normalized:
            return
        self.ticker = normalized
        self.add_recent_ticker(normalized)


def get_state() -> AppState:
    return AppState()


def available_themes() -> list:
    return AVAILABLE_THEMES
