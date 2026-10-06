import json
from pathlib import Path
from typing import Any

_TICKER_DIR = Path(__file__).parent / "tickers"
_TICKER_FILE = _TICKER_DIR / "dataset.json"

_EXCHANGES: dict[str, str] = {
    "NASDAQ": "NASDAQ",
    "NYSE": "NYSE",
    "NYSE ARCA": "NYSE",
}

TickerRecord = dict[str, Any]


def _build_dataset() -> list[TickerRecord]:
    seen: set[str] = set()
    records: list[TickerRecord] = []

    def add(symbol: str, name: str, exchange: str) -> None:
        s = symbol.strip().upper()
        if s and s not in seen:
            seen.add(s)
            records.append({
                "symbol": s,
                "name": name.strip(),
                "exchange": _EXCHANGES.get(exchange.strip(), exchange.strip()),
            })

    add("AAPL", "Apple Inc.", "NASDAQ")
    add("MSFT", "Microsoft Corporation", "NASDAQ")
    add("GOOGL", "Alphabet Inc.", "NASDAQ")
    add("GOOG", "Alphabet Inc.", "NASDAQ")
    add("AMZN", "Amazon.com Inc.", "NASDAQ")
    add("NVDA", "NVIDIA Corporation", "NASDAQ")
    add("META", "Meta Platforms Inc.", "NASDAQ")
    add("BRK-B", "Berkshire Hathaway Inc.", "NYSE")
    add("BRK-A", "Berkshire Hathaway Inc.", "NYSE")
    add("TSLA", "Tesla Inc.", "NASDAQ")
    add("UNH", "UnitedHealth Group Inc.", "NYSE")
    add("JPM", "JPMorgan Chase & Co.", "NYSE")
    add("V", "Visa Inc.", "NYSE")
    add("XOM", "Exxon Mobil Corporation", "NYSE")
    add("JNJ", "Johnson & Johnson", "NYSE")
    add("WMT", "Walmart Inc.", "NYSE")
    add("MA", "Mastercard Inc.", "NYSE")
    add("PG", "Procter & Gamble Company", "NYSE")
    add("HD", "The Home Depot Inc.", "NYSE")
    add("CVX", "Chevron Corporation", "NYSE")
    add("LLY", "Eli Lilly and Company", "NYSE")
    add("MRK", "Merck & Co. Inc.", "NYSE")
    add("ABBV", "AbbVie Inc.", "NYSE")
    add("KO", "The Coca-Cola Company", "NYSE")
    add("PEP", "PepsiCo Inc.", "NASDAQ")
    add("ADBE", "Adobe Inc.", "NASDAQ")
    add("CRM", "Salesforce Inc.", "NYSE")
    add("TMO", "Thermo Fisher Scientific Inc.", "NYSE")
    add("ACN", "Accenture plc", "NYSE")
    add("NFLX", "Netflix Inc.", "NASDAQ")
    add("AVGO", "Broadcom Inc.", "NASDAQ")
    add("CMCSA", "Comcast Corporation", "NASDAQ")
    add("PFE", "Pfizer Inc.", "NYSE")
    add("TXN", "Texas Instruments Inc.", "NASDAQ")
    add("QCOM", "QUALCOMM Incorporated", "NASDAQ")
    add("COST", "Costco Wholesale Corporation", "NASDAQ")
    add("NEE", "NextEra Energy Inc.", "NYSE")
    add("AMGN", "Amgen Inc.", "NASDAQ")
    add("NKE", "NIKE Inc.", "NYSE")
    add("DIS", "The Walt Disney Company", "NYSE")
    add("DHR", "Danaher Corporation", "NYSE")
    add("GS", "The Goldman Sachs Group Inc.", "NYSE")
    add("HON", "Honeywell International Inc.", "NASDAQ")
    add("SBUX", "Starbucks Corporation", "NASDAQ")
    add("MS", "Morgan Stanley", "NYSE")
    add("CAT", "Caterpillar Inc.", "NYSE")
    add("IBM", "International Business Machines", "NYSE")
    add("SPY", "SPDR S&P 500 ETF Trust", "NYSE ARCA")
    add("QQQ", "Invesco QQQ Trust", "NASDAQ")
    add("VTI", "Vanguard Total Stock Market ETF", "NYSE ARCA")
    add("AMD", "Advanced Micro Devices Inc.", "NASDAQ")
    add("INTC", "Intel Corporation", "NASDAQ")
    add("PYPL", "PayPal Holdings Inc.", "NASDAQ")
    add("BA", "The Boeing Company", "NYSE")
    add("GE", "General Electric Company", "NYSE")
    add("AMAT", "Applied Materials Inc.", "NASDAQ")
    add("MU", "Micron Technology Inc.", "NASDAQ")
    add("LRCX", "Lam Research Corporation", "NASDAQ")
    add("KLAC", "KLA Corporation", "NASDAQ")
    add("ADI", "Analog Devices Inc.", "NASDAQ")
    add("MCHP", "Microchip Technology Inc.", "NASDAQ")
    add("APP", "AppLovin Corporation", "NASDAQ")
    add("MDB", "MongoDB Inc.", "NASDAQ")
    add("SNOW", "Snowflake Inc.", "NYSE")
    add("DDOG", "Datadog Inc.", "NASDAQ")
    add("PLTR", "Palantir Technologies Inc.", "NYSE")
    add("UBER", "Uber Technologies Inc.", "NYSE")
    add("LYFT", "Lyft Inc.", "NASDAQ")
    add("SNAP", "Snap Inc.", "NYSE")
    add("PINS", "Pinterest Inc.", "NYSE")
    add("SQ", "Block Inc.", "NYSE")
    add("HOOD", "Robinhood Markets Inc.", "NASDAQ")
    add("COIN", "Coinbase Global Inc.", "NASDAQ")
    add("RIVN", "Rivian Automotive Inc.", "NASDAQ")
    add("LCID", "Lucid Group Inc.", "NASDAQ")
    add("F", "Ford Motor Company", "NYSE")
    add("GM", "General Motors Company", "NYSE")
    add("MRNA", "Moderna Inc.", "NASDAQ")
    add("BNTX", "BioNTech SE", "NASDAQ")
    add("MSTR", "MicroStrategy Incorporated", "NASDAQ")
    add("PANW", "Palo Alto Networks Inc.", "NASDAQ")
    add("CRWD", "CrowdStrike Holdings Inc.", "NASDAQ")
    add("ZS", "Zscaler Inc.", "NASDAQ")
    add("NET", "Cloudflare Inc.", "NYSE")
    add("OKTA", "Okta Inc.", "NASDAQ")
    add("WDAY", "Workday Inc.", "NASDAQ")
    add("NOW", "ServiceNow Inc.", "NYSE")
    add("TEAM", "Atlassian Corporation", "NASDAQ")
    add("SHOP", "Shopify Inc.", "NYSE")
    add("TTD", "The Trade Desk Inc.", "NASDAQ")
    add("ROKU", "Roku Inc.", "NASDAQ")
    add("ZM", "Zoom Video Communications Inc.", "NASDAQ")
    add("DOCU", "DocuSign Inc.", "NASDAQ")
    add("ORCL", "Oracle Corporation", "NYSE")
    add("SAP", "SAP SE", "NYSE")
    add("ADSK", "Autodesk Inc.", "NASDAQ")
    add("ANET", "Arista Networks Inc.", "NYSE")
    add("CSCO", "Cisco Systems Inc.", "NASDAQ")
    add("HPQ", "HP Inc.", "NYSE")
    add("DELL", "Dell Technologies Inc.", "NYSE")
    add("WFC", "Wells Fargo & Company", "NYSE")
    add("BAC", "Bank of America Corporation", "NYSE")
    add("C", "Citigroup Inc.", "NYSE")
    add("SCHW", "Charles Schwab Corporation", "NYSE")
    add("BLK", "BlackRock Inc.", "NYSE")
    add("VZ", "Verizon Communications Inc.", "NYSE")
    add("T", "AT&T Inc.", "NYSE")
    add("TMUS", "T-Mobile US Inc.", "NASDAQ")
    add("CHTR", "Charter Communications Inc.", "NASDAQ")
    add("AMT", "American Tower Corporation", "NYSE")
    add("EQIX", "Equinix Inc.", "NYSE")
    add("PLD", "Prologis Inc.", "NYSE")
    add("CCI", "Crown Castle Inc.", "NYSE")
    add("DG", "Dollar General Corporation", "NYSE")
    add("DLTR", "Dollar Tree Inc.", "NASDAQ")
    add("TGT", "Target Corporation", "NYSE")
    add("LOW", "Lowe's Companies Inc.", "NYSE")
    add("TJX", "TJX Companies Inc.", "NYSE")
    add("ROST", "Ross Stores Inc.", "NASDAQ")
    add("MCD", "McDonald's Corporation", "NYSE")
    add("YUM", "Yum! Brands Inc.", "NYSE")
    add("DRI", "Darden Restaurants Inc.", "NYSE")
    add("CMG", "Chipotle Mexican Grill Inc.", "NYSE")
    add("DPZ", "Domino's Pizza Inc.", "NYSE")
    add("MDLZ", "Mondelez International Inc.", "NASDAQ")
    add("KHC", "The Kraft Heinz Company", "NASDAQ")
    add("CAG", "Conagra Brands Inc.", "NYSE")
    add("GIS", "General Mills Inc.", "NYSE")
    add("K", "Kellanova", "NYSE")
    add("CPB", "Campbell's Company", "NYSE")
    add("HSY", "The Hershey Company", "NYSE")
    add("CL", "Colgate-Palmolive Company", "NYSE")
    add("KMB", "Kimberly-Clark Corporation", "NYSE")
    add("EL", "The Estée Lauder Companies Inc.", "NYSE")
    add("AAP", "Advance Auto Parts Inc.", "NYSE")
    add("AZO", "AutoZone Inc.", "NYSE")
    add("ORLY", "O'Reilly Automotive Inc.", "NASDAQ")
    add("TSCO", "Tractor Supply Company", "NASDAQ")
    add("BBY", "Best Buy Co. Inc.", "NYSE")
    add("EBAY", "eBay Inc.", "NASDAQ")
    add("ETSY", "Etsy Inc.", "NASDAQ")
    add("MELI", "MercadoLibre Inc.", "NASDAQ")
    add("PDD", "PDD Holdings Inc.", "NASDAQ")
    add("BABA", "Alibaba Group Holding Ltd.", "NYSE")
    add("JD", "JD.com Inc.", "NASDAQ")
    add("NTES", "NetEase Inc.", "NASDAQ")
    add("TCEHY", "Tencent Holdings Ltd.", "OTC")
    add("TSM", "Taiwan Semiconductor Manufacturing", "NYSE")

    records.sort(key=lambda r: (r["symbol"], r["name"]))
    return records


def get_dataset() -> list[TickerRecord]:
    if _TICKER_FILE.exists():
        with open(_TICKER_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    records = _build_dataset()
    _TICKER_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(_TICKER_FILE, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2)
    return records


def _is_subsequence(query: str, target: str) -> bool:
    it = iter(target)
    for c in query:
        if c not in it:
            return False
    return True


def search(query: str, limit: int = 10) -> list[TickerRecord]:
    """
    Fuzzy search tickers by symbol or company name.
    Returns results ranked by relevance.
    """
    if not query or not query.strip():
        return []
    q = query.strip().upper()
    dataset = get_dataset()
    scored: list[tuple[int, int, TickerRecord]] = []

    for rec in dataset:
        sym = rec["symbol"]
        name = rec["name"].upper()

        if sym == q:
            scored.append((0, 0, rec))
        elif sym.startswith(q):
            scored.append((1, len(sym), rec))
        elif q in sym:
            scored.append((2, len(sym), rec))
        elif _is_subsequence(q, sym):
            scored.append((3, len(sym), rec))
        elif name == q:
            scored.append((4, 0, rec))
        elif name.startswith(q):
            scored.append((5, 0, rec))
        elif q in name:
            scored.append((6, 0, rec))
        elif any(w.startswith(q) for w in name.split()):
            scored.append((7, 0, rec))

    scored.sort(key=lambda x: (x[0], len(x[2]["symbol"]), x[2]["symbol"]))
    return [r[2] for r in scored[:limit]]


def lookup(symbol: str) -> TickerRecord | None:
    s = symbol.strip().upper()
    dataset = get_dataset()
    for rec in dataset:
        if rec["symbol"] == s:
            return rec
    return None
