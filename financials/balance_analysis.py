def analyze(balance):
    if balance is None or getattr(balance,"empty",True):
        return {}
    latest=balance.iloc[:,0]
    return {
        "Cash": latest.get("Cash And Cash Equivalents"),
        "Total Assets": latest.get("Total Assets"),
        "Total Liabilities": latest.get("Total Liabilities"),
        "Shareholder Equity": latest.get("Stockholders Equity")
    }
