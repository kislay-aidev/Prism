from .fundamental_score import score

def company_quality(info):
    s=score(info)
    if s>=80:grade="A"
    elif s>=65:grade="B"
    elif s>=50:grade="C"
    elif s>=35:grade="D"
    else:grade="F"
    return {"score":s,"grade":grade}
