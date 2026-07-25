def human_number(value):
    if value is None:
        return "N/A"
    try:
        value=float(value)
    except (ValueError,TypeError):
        return value
    if abs(value)>=1e12:
        return f"{value/1e12:.2f}T"
    if abs(value)>=1e9:
        return f"{value/1e9:.2f}B"
    if abs(value)>=1e6:
        return f"{value/1e6:.2f}M"
    if abs(value)>=1e3:
        return f"{value/1e3:.2f}K"
    return f"{value:.2f}"
