import streamlit as st
from datetime import date

from config import APP_TITLE, DEFAULT_TICKERS
from data.data_fetcher import fetch_price_data, fetch_company_info
from data.market_status import market_status
from charts.candlestick import build as candle_chart
from charts.line_chart import build as line_chart
from charts.volume import build as volume_chart
from indicators.rsi import calculate as rsi
from indicators.macd import calculate as macd
from indicators.moving_average import sma
from news.news_feed import render_news
from watchlist.manager import load_watchlist
from watchlist.summary import build_summary
from ai.summary import generate_summary
from ai.market_rating import stars
from utils.formatting import human_number

st.set_page_config(page_title=APP_TITLE,layout="wide")
st.title(APP_TITLE)

open_now,msg=market_status()
st.sidebar.success("Market Open" if open_now else "Market Closed")
st.sidebar.caption(msg)

ticker=st.sidebar.text_input("Ticker",DEFAULT_TICKERS[0]).upper()
chart_type=st.sidebar.radio("Chart",["Candlestick","Line"])
start=st.sidebar.date_input("Start",date(2023,1,1))
end=st.sidebar.date_input("End",date.today())

df=fetch_price_data(ticker,start,end)
if df.empty:
    st.error("No data found.")
    st.stop()

df["SMA20"]=sma(df.Close,20)
df["RSI"]=rsi(df.Close)
m,sig,h=macd(df.Close)
df["MACD"]=m

c1,c2=st.columns([3,1])

with c1:
    if chart_type=="Candlestick":
        st.plotly_chart(candle_chart(df,ticker),use_container_width=True)
    else:
        st.plotly_chart(line_chart(df,ticker),use_container_width=True)
    st.plotly_chart(volume_chart(df),use_container_width=True)

with c2:
    info=fetch_company_info(ticker)
    st.subheader("Company")
    st.write(info.get("longName",ticker))
    st.write("Sector:",info.get("sector","N/A"))
    st.write("Market Cap:",human_number(info.get("marketCap","N/A")))
    summary,res=generate_summary(ticker,{
        "RSI":float(df["RSI"].iloc[-1]),
        "MACD":float(df["MACD"].iloc[-1]),
        "PRICE":float(df.Close.iloc[-1]),
        "SMA":float(df.SMA20.iloc[-1])
    })
    st.subheader("AI")
    st.text(summary)
    st.write(stars(res["confidence"]))

st.divider()
render_news(st,ticker)

wl=load_watchlist()
if wl:
    st.subheader("Watchlist")
    st.dataframe(build_summary(wl,start,end),use_container_width=True)
