from .weights import WEIGHTS

def calculate(metrics:dict):
    score=0
    details={}
    for k,w in WEIGHTS.items():
        val=float(metrics.get(k,0))
        contrib=val*w
        details[k]=contrib
        score+=contrib
    return {"normalized":round(score/sum(WEIGHTS.values()),2),
            "details":details}
