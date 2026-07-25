import pandas_market_calendars as mcal

def trading_schedule(start, end):
    nyse = mcal.get_calendar("NYSE")
    return nyse.schedule(start_date=start, end_date=end)
