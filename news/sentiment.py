POS={"beat","growth","upgrade","profit","record","bullish"}
NEG={"miss","loss","downgrade","lawsuit","bearish","decline"}

def analyze(headlines):
    score=0
    for h in headlines:
        t=h.lower()
        score+=sum(w in t for w in POS)
        score-=sum(w in t for w in NEG)
    label="Neutral"
    if score>0: label="Positive"
    elif score<0: label="Negative"
    return {"score":score,"label":label}
