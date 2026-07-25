def build(positions: list) -> dict:
    if not positions:
        return {"status": "empty", "positions": [], "summary": {}}
    total_value = sum(p.get("value", 0) for p in positions)
    total_pnl = sum(p.get("pnl", 0) for p in positions)
    return {
        "status": "active",
        "positions": positions,
        "summary": {
            "total_value": round(total_value, 2),
            "total_pnl": round(total_pnl, 2),
            "position_count": len(positions),
        },
    }
