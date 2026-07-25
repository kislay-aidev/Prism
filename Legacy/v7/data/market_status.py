from datetime import datetime
from zoneinfo import ZoneInfo

US_TZ=ZoneInfo("America/New_York")

def market_status():
    now=datetime.now(US_TZ)
    if now.weekday()>=5:
        return False,"Weekend"
    open_time=now.replace(hour=9,minute=30,second=0,microsecond=0)
    close_time=now.replace(hour=16,minute=0,second=0,microsecond=0)
    return open_time<=now<=close_time, now.strftime("%Y-%m-%d %H:%M %Z")
