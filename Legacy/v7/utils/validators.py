def validate_ticker(text):
    text=text.strip().upper()
    if not text:
        return False,"Ticker cannot be empty."
    cleaned=text.replace(".","").replace("-","")
    if not cleaned.isalnum():
        return False,"Ticker contains invalid characters."
    return True,text
