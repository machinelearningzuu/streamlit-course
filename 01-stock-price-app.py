import time
import yfinance 
import pandas as pd
import streamlit as st
from datetime import date, timedelta

st.write("""
# Simple Stock Price App
         
Shown are the stock closing price and volume of Google!

""")

tickerSymbol = 'GOOGL' #define the ticker symbol
tickerData = yfinance.Ticker(tickerSymbol) #get data on this ticker

start_date = '2021-01-01'
end_date = '2022-01-01'

counter = 0
ph_close = st.empty()
ph_volume = st.empty()
time_initial = time.time()

while counter <= 365:
    if time.time() >= time_initial + 0.1:
        tickerDf = tickerData.history(
                                    period='1d', 
                                    start=start_date, 
                                    end=end_date
                                    ) #get the historical prices for this ticker

        ph_close.line_chart(tickerDf.Close)
        ph_volume.line_chart(tickerDf.Volume)

        time_initial = time.time()

        start_date = date.fromisoformat(start_date) + timedelta(days=1)
        start_date = start_date.isoformat()

        end_date = date.fromisoformat(end_date) + timedelta(days=1)
        end_date = end_date.isoformat()
        counter += 1