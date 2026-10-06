from .recommendation import recommend


def build(symbol: str, indicators: dict) -> str:
    rec = recommend(indicators)
    lines = [
        f"# {symbol} Analysis",
        f"**Recommendation**: {rec['action']} (Confidence: {rec['confidence']}%)",
        f"**Score**: {rec['score']}",
        "",
        "## Key Signals",
    ]
    for r in rec["reasons"]:
        lines.append(f"- {r}")
    return "\n".join(lines)
