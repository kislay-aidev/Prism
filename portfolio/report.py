from .transactions import load
from .pnl import unrealized
from .risk import exposure
def generate(price_map):
    tx=load()
    pnl=unrealized(tx,price_map)
    return {"positions":pnl,"risk":exposure(pnl)}
