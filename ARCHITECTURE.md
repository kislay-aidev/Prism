# Architecture

## Overview

Prism follows a layered architecture with strict separation of concerns. Each layer has a single responsibility and communicates through well-defined interfaces.

## Layer Diagram

```
┌──────────────────────────────────────────────────────────────┐
│                     Presentation Layer                       │
│  app.py · dashboard/ · ui/                                  │
│  Streamlit pages, sidebar controls, theme CSS injection      │
├──────────────────────────────────────────────────────────────┤
│                     Integration Layer                        │
│  dashboard/integration.py                                    │
│  Wires data → indicators → visualization pipeline            │
├──────────────────────────────────────────────────────────────┤
│                     Domain Layer                             │
│  indicators/ · ai/ · financials/ · news/ · portfolio/        │
│  Business logic: technical analysis, signals, fundamentals   │
├──────────────────────────────────────────────────────────────┤
│                     Data Layer                               │
│  data/engine.py · data/batch.py · data/validator.py          │
│  yfinance abstraction with retry, cache, validation          │
├──────────────────────────────────────────────────────────────┤
│                     Foundation Layer                         │
│  core/settings.py · core/state.py · core/market.py           │
│  Configuration, session state, market clock, logging         │
└──────────────────────────────────────────────────────────────┘
```

## Module Responsibilities

### `core/` — Foundation

| Module | Responsibility |
|---|---|
| `settings.py` | Immutable configuration dataclass (frozen) |
| `state.py` | Session state initialization and defaults |
| `market.py` | NYSE market clock using `pandas_market_calendars` |
| `cache.py` | Streamlit cache decorator wrapper |
| `logger.py` | File-based timestamped logging |
| `performance.py` | Context manager timer for profiling |
| `exceptions.py` | Custom exception hierarchy (`DashboardError` → `DataFetchError`, `InvalidTickerError`) |

### `data/` — Data Layer

| Module | Responsibility |
|---|---|
| `engine.py` | `StockDataEngine` class with retry (3 attempts), TTL caching, yfinance abstraction |
| `batch.py` | Multi-symbol download with per-symbol error isolation |
| `validator.py` | Ticker string validation (alphanumeric, dot, hyphen) |
| `calendar.py` | Trading schedule query via NYSE calendar |

### `indicators/` — Technical Analysis

All indicator modules export a `calculate(df, ...)` function. The `pipeline.py` orchestrates all indicators and enriches a DataFrame with computed columns.

**Supported indicators:** SMA, EMA, RSI, MACD, ADX, ATR, Bollinger Bands, SuperTrend, Ichimoku, Stochastic, Williams %R, VWAP, OBV, Fibonacci, Support/Resistance.

### `ai/` — Signal Intelligence

| Module | Responsibility |
|---|---|
| `scoring.py` | Multi-factor scoring (RSI, MACD, ADX, SMA cross, BB position, OBV) |
| `recommendation.py` | Maps score to STRONG_BUY/BUY/HOLD/SELL/STRONG_SELL with confidence |
| `risk.py` | Risk classification (Low/Medium/High) based on beta and ATR |
| `targets.py` | Price targets (entry, stop loss, targets, risk/reward ratios) |
| `rating.py` | Star rating system (1-5) based on confidence score |
| `dashboard.py` | Aggregates all AI modules into a comprehensive analysis dict |

### `charts/` — Charting Engine

All chart modules export a `build(df, title)` function returning a Plotly figure. `base.py` provides shared layout configuration.

### `financials/` — Fundamentals

Extracts financial metrics from yfinance `info` dict. Covers valuation, growth, quality, dividend, health, and generates fundamental scores.

### `news/` — News Intelligence

Fetches news via yfinance, applies deduplication, categorization, sentiment analysis, impact scoring, and timeline generation.

### `portfolio/` — Portfolio Management

JSON-file-backed portfolio with transaction recording, cost basis (FIFO-like), unrealized P&L, allocation analytics, risk exposure, and reporting.

### `reports/` — Report Generation

Generates structured reports (technical, financial, portfolio) and renders them as HTML or PDF (via reportlab).

### `ui/` — UI Components

Reusable Streamlit components for themes, metric cards, status bar, search, navigation, favorites, notifications, and layout presets.

## Design Decisions

### Why `core/` instead of environment variables?
Settings are configured at the dataclass level for type safety and discoverability. Environment variables can be added via `python-dotenv` if needed.

### Why a single `pipeline.py` for indicators?
Indicators are computed sequentially because many depend on the same base data. A single pipeline avoids redundant computation and ensures consistent data flow.

### Why JSON file storage for portfolios?
Keeps the application self-contained without requiring a database. Suitable for single-user deployments. Replaceable with a database adapter for multi-user scenarios.

### Why rule-based AI instead of ML?
Rule-based signals are transparent, explainable, and require no training data. The scoring engine is designed to be extensible — additional factors can be added without retraining.

## Extensibility

### Adding a new indicator
1. Create `indicators/your_indicator.py` with a `calculate(df, ...)` function
2. Add it to `indicators/pipeline.py` → `apply()`
3. Register in `indicators/registry.py`
4. It will automatically be available in the pipeline

### Adding a new export format
1. Create `export/your_format_export.py`
2. Add it to `export/manager.py` → `available_exports()`

### Adding a new theme
1. Extend `ui/theme.py` → `available_themes()` and `inject_theme_css()`
2. Add theme config to `.streamlit/config.toml`
