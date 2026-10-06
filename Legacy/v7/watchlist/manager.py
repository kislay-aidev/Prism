import json
from pathlib import Path

DB=Path(__file__).parent/"watchlist.json"

def load_watchlist():
    if not DB.exists():
        return []
    try:
        return json.loads(DB.read_text())
    except Exception:
        return []

def save_watchlist(symbols):
    symbols=sorted(set(s.upper().strip() for s in symbols if s.strip()))
    DB.write_text(json.dumps(symbols,indent=2))

def add(symbol):
    wl=load_watchlist()
    s=symbol.upper().strip()
    if s and s not in wl:
        wl.append(s)
        save_watchlist(wl)

def remove(symbol):
    wl=load_watchlist()
    s=symbol.upper().strip()
    if s in wl:
        wl.remove(s)
        save_watchlist(wl)
