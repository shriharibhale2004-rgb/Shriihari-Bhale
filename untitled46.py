# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 17:45:15 2026

@author: shrih
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
plt.style.use('dark_background')

#load dataset
df=pd.read_csv("C:/Linear Regression/AirPassengers.csv")
df=df.rename({'#Passengers': 'Passengers'},axis=1)

print(df.dtypes)

#convert month to datetime

df['Month']=pd.to_datetime(df['Month'])

print(df.dtypes)

#set month as index

df.set_index('Month',inplace=True)

#plot time series

plt.plot(df.Passengers)
plt.title('Air passengers over time')
plt.show()

#Diskey Fuller test (Stationarity check)
from statsmodels.tsa.stattools import adfuller

adf ,pvalue,usedlag_,nobs_,critical_values_,ichest_=adfuller(df['Passengers'])
print("pvalue=",pvalue,"(If >0.05 is not stationary)")

'''
p- value = 0.991880
condition          interpretation
**p-value<_0.05     data is stationary
p-value >0.05       data is not stationary

0.9918

therefore
reject stationarity assumption
the time series is non stationarity
what this means practically
the data likely contains:
trend 
seasonality
    
'''
