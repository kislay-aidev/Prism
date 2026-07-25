CATEGORIES={
"earnings":["earnings","eps","quarter","revenue"],
"merger":["merger","acquisition","acquire"],
"product":["launch","product","device","service"],
"regulation":["sec","regulation","court","fine"],
"analyst":["upgrade","downgrade","target"]
}
def categorize(title:str):
    t=title.lower()
    for cat,keys in CATEGORIES.items():
        if any(k in t for k in keys):
            return cat.title()
    return "General"
