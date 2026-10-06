from datetime import datetime

def timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def pct_change(current, previous):
    if previous==0:
        return 0
    return ((current-previous)/previous)*100
