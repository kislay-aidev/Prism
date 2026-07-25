from .timeline import build
def generate(news):
    tl=build(news)
    cats={}
    for e in tl:
        cats[e["category"]]=cats.get(e["category"],0)+1
    return {
      "events":len(tl),
      "categories":cats,
      "summary":"; ".join(f"{k}: {v}" for k,v in cats.items()) or "No major events"
    }
