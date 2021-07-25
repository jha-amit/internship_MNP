# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 17:39:39 2021

@author: amit
"""


import yfinance as yf
from yahoofinancials import YahooFinancials
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import csv
import json
from pandas.io.json import json_normalize

import yfinance as yf
from yahoofinancials import YahooFinancials
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import csv
import json
from pandas.io.json import json_normalize

input_data=pd.read_csv('Data_required_filtered.csv')
#input_data=input_data.dropna()
tickers = input_data["ticker"]
tickers=tickers.dropna()
df=pd.DataFrame()

dates=[]
dict_dates={}
for k in range(len(tickers)):
    yahoo_financials = YahooFinancials(tickers[k])
    balance_sheet_data_qt = yahoo_financials.get_financial_stmts('annual', 'balance')
    data=balance_sheet_data_qt['balanceSheetHistory']
    print(data)
    for i in range(0,len(data[tickers[k]])):
        for j in data[tickers[k]][i]: 
            #dates.append(j) 
            #dict_dates['Dates']=j
            value = data[tickers[k]][i][j]
            value['Dates']=j
            value['company']=tickers[k]
            df=df.append(value,ignore_index=True)
            #df=df.append(dict_dates,ignore_index=True)
            
#df=df.set_index(pd.Index(tickers))      
compression_opts = dict(method='zip',
                        archive_name='balanceSheetHistory.csv')  
df.to_csv('test.csv', index=True,
          compression=None) 