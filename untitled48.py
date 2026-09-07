# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 16:19:04 2026

@author: shrih
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.graphics.tsaplots import plot_pacf
from sklearn.metrics import mean_squared_error
import warnings
warnings.filterwarnings('ignore')

#1 load dataset and preprocess
df=pd.read_csv("C:/Time Series/uspopulation.csv",index_col='DATE',parse_dates=True)
df.index.freq = "MS" #monthly start frequency

print(df.head())

#plot the data
df['PopEst'].plot(figsize=(12,5),title='U.S Monthly Population Estimates')
plt.ylabel("population estimate")
plt.show()

#2 train test split

train=df.iloc[:84]
test=df.iloc[84:]
print(len(train),len(test))

#3 use pact to decide Ar order

plt.figure(figsize=(8,4))
plot_pacf(train['PopEst'],lags=20,method='ywm')


'''
ld (levinson-durbin),but 'ywm' is actually preferred for AR model
order selection
'''
plt.title("PACF plot for AR order selection")
plt.show()

'''

Decision Rule
-if only lag 1 is significant (outside shaked area)- choose AR(1)
-if lags 1 and 2 are significant - choose AR2
-if lags keep being significant up to lag k then cut off
-choose AR k
- 

'''

#3 fit AR model with different lags

model=AutoReg(train['PopEst'],lags=1).fit()
pred1=model.predict(start=len(train),end=len(train)+len(test)-1,dynamic=False)

model2=AutoReg(train['PopEst'],lags=1).fit()
pred2=model2.predict(start=len(train),end=len(train)+len(test)-1,dynamic=False)

#4 compare with actual values

plt.figure(figsize=(12,6))
plt.plot(train.index,train['PopEst'],labels='Train')
plt.plot(test.index,test['PopEst'],labels='Test',color='black')
plt.plot(test.index,pred1,label="AR(1) prediction")
plt.plot(test.index,pred2,label="AR(2) prediction")
plt.legend()
plt.title("AR Model Forecasts")
plt.show()

#5 Evaluation (MSE)
for label,pred in zip(["AR(1)","AR(2)"],[pred1,pred2]):
    error =mean_squared_error(test["PopEst"],pred)
    print(f"{label} MSE:{error}:.2f")


#6 forecast future population 

final_model= AutoReg(df['PopEst'],lags=2).fit()
forecast= final_model.predict(start=len(df),end=len(df)+12,dynamic=False)

print(forecast.head())

plt.figure(figsize=(12,6))
plt.plot(df.index,df['PopEst'],label="historical data")
plt.plot(forecast.index,forecast,label="12-month forecast",color='red')
plt.legend()
plt.title("US Population Forecast using AR(2)")
plt.show()
