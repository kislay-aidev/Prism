from .manager import load
from .analytics import summary
from .allocation import weights
from .performance import portfolio_return

def build(price_map):
    holdings=load()
    df,total=summary(holdings,price_map)
    df=weights(df)
    return {"table":df,"value":total,"return_pct":portfolio_return(df)}
