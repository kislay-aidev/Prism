import json
from pathlib import Path
DB=Path(__file__).parent/"transactions.json"
def load():
    return json.loads(DB.read_text()) if DB.exists() else []
def add(symbol,side,qty,price,date):
    data=load()
    data.append({"symbol":symbol.upper(),"side":side.upper(),"qty":qty,"price":price,"date":date})
    DB.write_text(json.dumps(data,indent=2))
