# Prism

**Refracting market data into intelligence.**

Prism is a production-grade financial intelligence platform that transforms raw market data into actionable insights. Built with Streamlit, Plotly, and yFinance, it provides professional-grade technical analysis, AI-powered signal generation, portfolio management, and real-time market intelligence.

---

## Features

- **Professional Charting** — Candlestick, OHLC, Line, Area, Volume charts with dark/light/AMOLED themes
- **Technical Analysis Engine** — RSI, MACD, ADX, ATR, Bollinger Bands, Ichimoku, Stochastic, SuperTrend, VWAP, Williams %R, OBV, Fibonacci, Support/Resistance
- **AI Signal Engine** — Multi-factor scoring with confidence levels, price targets, risk assessment, and recommendation generation
- **Company Intelligence** — Financial ratios, growth metrics, valuation analysis, fundamental scoring, dividend data
- **News Intelligence** — Real-time news aggregation with deduplication, categorization, sentiment analysis, and impact scoring
- **Portfolio Manager** — Position tracking, cost basis, P&L calculation, allocation analytics, risk exposure
- **Export Engine** — CSV, Excel, PDF, HTML report, PNG image exports
- **Multi-Theme Support** — Dark, Light, and AMOLED themes with full CSS customization
- **Market Clock** — Real-time market open/close status with NYSE calendar integration

---

## Architecture

```
prism/
├── app.py                 # Main application entry point
├── core/                  # Foundation layer
│   ├── settings.py        # Application configuration
│   ├── state.py           # Session state management
│   ├── market.py          # Market clock (NYSE calendar)
│   ├── cache.py           # Caching decorator
│   ├── logger.py          # Logging utility
│   ├── performance.py     # Performance timer
│   └── exceptions.py      # Custom exception hierarchy
├── data/                  # Data layer
│   ├── engine.py          # Stock data engine (retry, cache, validation)
│   ├── batch.py           # Batch multi-symbol downloads
│   ├── validator.py       # Input validation
│   └── calendar.py        # Trading calendar
├── indicators/            # Technical indicators
│   ├── pipeline.py        # Indicator computation pipeline
│   ├── rsi.py, macd.py, adx.py, atr.py
│   ├── bollinger.py, moving_averages.py
│   ├── supertrend.py, ichimoku.py
│   ├── stochastic.py, williams_r.py, vwap.py
│   ├── obv.py, fibonacci.py, support_resistance.py
│   └── registry.py        # Indicator registry
├── ai/                    # Signal intelligence
│   ├── scoring.py         # Multi-factor scoring engine
│   ├── recommendation.py  # Buy/sell/hold recommendations
│   ├── risk.py            # Risk classification
│   ├── targets.py         # Price target generation
│   ├── rating.py          # Star rating system
│   └── dashboard.py       # AI insights dashboard
├── charts/                # Charting engine
│   ├── candlestick.py, ohlc.py, line.py, area.py, volume.py
│   ├── comparison.py      # Normalized comparison
│   ├── panels.py          # RSI/MACD panel charts
│   ├── indicators_overlay.py, compose.py, signals.py
│   └── export.py          # Chart export (PNG, HTML)
├── financials/            # Fundamentals
│   ├── ratios.py, growth.py, dividend.py
│   ├── valuation.py, quality.py, health.py
│   ├── fundamental_score.py
│   ├── income_analysis.py, balance_analysis.py, cashflow_analysis.py
│   └── report.py
├── news/                  # News intelligence
│   ├── fetcher.py, sentiment.py, summarizer.py, renderer.py
│   ├── categorizer.py, deduplicate.py, digest.py
│   ├── impact.py, timeline.py
├── portfolio/             # Portfolio management
│   ├── manager.py, allocation.py, analytics.py
│   ├── cost_basis.py, pnl.py, transactions.py, risk.py
│   └── dashboard.py, report.py
├── reports/               # Report generation
│   ├── technical_report.py, financial_report.py, portfolio_report.py
│   ├── executive_summary.py, report_manager.py
│   ├── html_template.py, pdf_template.py
├── export/                # Export engine
│   ├── csv_export.py, excel_export.py, image_export.py
│   ├── pdf_report.py, html_report.py, manager.py
├── ui/                    # UI components
│   ├── theme.py           # Theme engine with CSS injection
│   ├── metric_cards.py, status_bar.py, navigation.py
│   ├── search.py, refresh.py, favorites.py
│   ├── notifications.py, layout_presets.py
├── dashboard/             # Dashboard layout
│   ├── home.py, sidebar.py, tabs.py, layout.py
│   ├── integration.py     # Data & indicator integration
│   └── toolbar.py, workspace.py, actions.py, export_center.py
├── tests/                 # Test suite
│   ├── test_ai.py, test_indicators.py, test_reports.py
├── .streamlit/            # Streamlit configuration
│   └── config.toml        # Theme & server settings
├── Legacy/                # Historical versions (v1–v7)
└── requirements.txt
```

---

## Installation

### Prerequisites

- Python 3.10+
- pip

### Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/prism.git
cd prism

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

### Quick Start

1. Open the application in your browser (default: `http://localhost:8501`)
2. Enter a stock ticker (e.g., `AAPL`, `MSFT`, `TSLA`) in the sidebar
3. Select a chart type (Candlestick, OHLC, Line, Area)
4. Navigate between views using the sidebar navigation
5. Switch between Dark, Light, and AMOLED themes

---

## Screenshots

> Screenshots will be added to `screenshots/` directory.

| View | Description |
|---|---|
| Dashboard | Market overview with price metrics and candlestick chart |
| Technical Analysis | Full technical indicator suite with panel charts |
| Financials | Company fundamentals, ratios, and valuation |
| News | Real-time news with categorization and sentiment |
| Portfolio | Position tracking, P&L, and allocation analytics |
| AI Insights | AI-generated signals, targets, and risk assessment |

---

## Roadmap

- [x] Phase 1: Foundation — Configuration, caching, logging, state management
- [x] Phase 2: Data Engine — Centralized data retrieval with retry and validation
- [x] Phase 3: Chart Engine — Multi-chart types, overlays, trade markers
- [x] Phase 4: Technical Analysis — 17 indicators with pipeline orchestration
- [x] Phase 5: Signal Engine — Multi-factor scoring and recommendation
- [x] Phase 6: Company Intelligence — Fundamentals, ratios, scoring
- [x] Phase 7: Financial Statements — Income, balance sheet, cash flow
- [x] Phase 8: News Intelligence — Categorization, sentiment, impact
- [x] Phase 9: Portfolio Manager — Positions, P&L, risk, allocation
- [x] Phase 10: AI Dashboard — Comprehensive market insights
- [x] Phase 11: Export Engine — CSV, Excel, PDF, HTML, PNG
- [x] Phase 12: UI Polish — Theme engine, responsive layout, animations
- [x] Phase 13: Tests — Unit tests for core modules
- [ ] Phase 14: Integration tests and stress testing
- [ ] Phase 15: CI/CD pipeline and production deployment

---

## Version History

| Version | Description |
|---|---|
| v1 | Base dashboard with single-stock price charts |
| v2 | Multi-stock comparison |
| v3 | Technical indicators (Bollinger, RSI, MACD) |
| v4 | Real-time updates, candlestick charts, signals |
| v5 | UI polish, market status widget |
| v6 | Multi-ticker, SMA/EMA controls, exports |
| v7 | Modular rewrite — foundation build |
| **v8 (Prism 1.0)** | **Production-grade financial intelligence platform** |

Historical versions are preserved in `Legacy/`.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Author

**Author placeholder** — *For attribution*

**GitHub**: [github.com/yourusername](https://github.com/yourusername)

**Intern ID**: `[placeholder]`

---

## Contributing

Contributions are welcome. Please open an issue or pull request for any improvements.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
