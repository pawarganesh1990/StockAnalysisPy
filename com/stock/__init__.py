import yfinance as yf
import pandas as pd
from datetime import datetime

stocks = ["AXISBANK.NS", "HDFCBANK.NS", "ICICIBANK.NS" ,"INDUSINDBK.NS",
          "KOTAKBANK.NS",
          "SBIN.NS",
          "YESBANK.NS"]
start ='2021-03-12'
end = '2021-03-14'
data = yf.download(tickers='UBER', period='1d' , interval='1m')
df = pd.DataFrame(data)
--int()

print(data['Close'].tail(1))
