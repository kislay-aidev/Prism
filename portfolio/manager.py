import json
from pathlib import Path
DB=Path(__file__).parent/"portfolio.json"
def load():
    if DB.exists():
        return json.loads(DB.read_text())
    return []
def save(data):
    DB.write_text(json.dumps(data,indent=2))
def add(symbol,qty,price):
    p=load()
    p.append({"symbol":symbol.upper(),"qty":qty,"price":price})
    save(p)
