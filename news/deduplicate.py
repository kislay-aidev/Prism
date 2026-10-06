def unique(news):
    seen=set(); out=[]
    for n in news:
        key=n.get("title","").strip().lower()
        if key and key not in seen:
            seen.add(key); out.append(n)
    return out
