def analyze(statement):
    if statement is None or getattr(statement,"empty",True):
        return {}
    latest=statement.iloc[:,0]
    return {
        "Total Revenue": latest.get("Total Revenue"),
        "Gross Profit": latest.get("Gross Profit"),
        "Operating Income": latest.get("Operating Income"),
        "Net Income": latest.get("Net Income")
    }
