import yfinance as yf
import pandas as pd
from datetime import datetime

stocks = ["AXISBANK.NS", "HDFCBANK.NS", "ICICIBANK.NS" ,"INDUSINDBK.NS",
          "KOTAKBANK.NS",
          "SBIN.NS",
          "YESBANK.NS"]
thisdict = {}

start ='2021-03-12'
end = '2021-03-14'
for stock in stocks:
    data = yf.download(tickers=stock , period='1d' , interval='1m')
    df = pd.DataFrame(data)
    thisdict.__setitem__(stock, data['Close'].tail(1).values[0])

for key in thisdict:
    print(key + " "+str(thisdict.get(key)))

