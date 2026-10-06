from datetime import datetime
from zoneinfo import ZoneInfo
import pandas_market_calendars as mcal

class MarketClock:
    def __init__(self):
        self.calendar=mcal.get_calendar("NYSE")
        self.tz=ZoneInfo("America/New_York")

    def status(self):
        now=datetime.now(self.tz)
        if now.weekday()>=5:
            return {"open":False,"reason":"Weekend","time":now}
        sched=self.calendar.schedule(start_date=now.date(),end_date=now.date())
        if sched.empty:
            return {"open":False,"reason":"Holiday","time":now}
        o=sched.iloc[0]["market_open"].tz_convert(self.tz)
        c=sched.iloc[0]["market_close"].tz_convert(self.tz)
        return {"open":o<=now<=c,"reason":"Open" if o<=now<=c else "Closed","time":now}
