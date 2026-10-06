from .categorizer import categorize
from .impact import score
def build(news):
    rows=[]
    for n in news:
        rows.append({
            "time":n.get("published"),
            "category":categorize(n.get("title","")),
            "impact":score(n.get("title",""))["impact"],
            "title":n.get("title","")
        })
    return sorted(rows,key=lambda x:x["time"],reverse=True)
