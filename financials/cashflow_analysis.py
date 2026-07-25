def analyze(cashflow):
    if cashflow is None or getattr(cashflow,"empty",True):
        return {}
    latest=cashflow.iloc[:,0]
    return {
        "Operating Cash Flow": latest.get("Operating Cash Flow"),
        "Capital Expenditure": latest.get("Capital Expenditures"),
        "Free Cash Flow": latest.get("Free Cash Flow")
    }
