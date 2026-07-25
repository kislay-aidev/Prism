def classify(beta: float = None, atr: float = None) -> str:
    high_risk = False
    low_risk = True

    if beta is not None:
        if beta > 1.5:
            high_risk = True
            low_risk = False
        elif beta < 0.7:
            low_risk = True
            high_risk = False
        else:
            low_risk = False
            high_risk = False

    if atr is not None and atr > 8:
        high_risk = True
        low_risk = False

    if high_risk:
        return "High"
    if low_risk:
        return "Low"
    return "Medium"


def label(level: str) -> str:
    labels = {"Low": "🟢 Low Risk", "Medium": "🟡 Medium Risk", "High": "🔴 High Risk"}
    return labels.get(level, "⚪ Unknown")
