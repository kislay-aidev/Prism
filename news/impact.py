def score(title):
    t=title.lower(); s=0
    for w in ("record","beat","growth","upgrade","profit"): 
        if w in t: s+=2
    for w in ("loss","miss","lawsuit","downgrade","fraud"):
        if w in t: s-=2
    return {"impact":abs(s),"direction":"Positive" if s>0 else "Negative" if s<0 else "Neutral"}
