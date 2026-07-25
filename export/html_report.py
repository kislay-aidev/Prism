def export(title,body,path):
    html=f'<html><head><title>{title}</title></head><body>{body}</body></html>'
    open(path,'w',encoding='utf-8').write(html)
    return path
