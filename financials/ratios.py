def calculate(info):
    return {
        "PE":info.get("trailingPE"),
        "Forward PE":info.get("forwardPE"),
        "PEG":info.get("pegRatio"),
        "ROE":info.get("returnOnEquity"),
        "ROA":info.get("returnOnAssets"),
        "Debt/Equity":info.get("debtToEquity"),
        "Current Ratio":info.get("currentRatio"),
        "Quick Ratio":info.get("quickRatio")
    }
