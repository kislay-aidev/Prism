from .sentiment import analyze

def summarize(news):
    heads=[n["title"] for n in news]
    s=analyze(heads)
    return {
        "headline_count":len(news),
        "sentiment":s["label"],
        "score":s["score"],
        "top_headlines":heads[:5]
    }
