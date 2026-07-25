def build(technical: dict, financial: dict, portfolio: dict) -> dict:
    return {
        "technical": technical,
        "financial": financial,
        "portfolio": portfolio,
        "overall": _overall_rating(technical, financial, portfolio),
    }


def _overall_rating(technical: dict, financial: dict, portfolio: dict) -> str:
    score = 50
    if technical.get("status") == "success":
        score += 10
    if financial.get("status") == "success":
        score += 10
    if portfolio.get("status") == "active":
        score += 15
    if score >= 80:
        return "Strong"
    if score >= 60:
        return "Moderate"
    return "Weak"
