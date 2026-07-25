POS={"beat","growth","upgrade","profit","record","bullish","positive"}
NEG={"miss","loss","downgrade","lawsuit","bearish","decline","negative"}

def simple_sentiment(headlines):
    score=0
    for h in headlines:
        t=h.lower()
        score+=sum(w in t for w in POS)
        score-=sum(w in t for w in NEG)
    if score>0:
        return "Positive",score
    if score<0:
        return "Negative",score
    return "Neutral",score
