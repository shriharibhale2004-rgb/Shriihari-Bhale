# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 17:02:03 2026

@author: shrih
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
from sklearn.metrics import mean_squared_error
import warnings
warnings.filterwarnings('ignore')

#1 load dataset and preprocess
df=pd.read_csv("C:/Time Series/uspopulation.csv",index_col='DATE',parse_dates=True)
df.index.freq = "MS" #monthly start frequency


#plot the data

df['PopEst'].plot(figsize=(12,5),title='U.S Monthly Population Estimates')
plt.ylabel("population estimate")
plt.show()

#2 train test split
train=df.iloc[:84]
test=df.iloc[84:]
print(len(train),len(test))

#3 Acf (for ma order selection)

plt.figure(figsize=(8,4))
plot_acf(train["PopEst"],lags=20)
plt.title("ACF plot gor MA order selection")
plt.show()

#4 fit MA models using ARIMA(0,q,0)

ma1=ARIMA(train['PopEst'],order=(0,1,0)).fit()
pred_ma1=ma1.predict(start=len(train),end=len(train)+len(test)-1,dynamic=False)

ma2=ARIMA(train['PopEst'],order=(0,2,0)).fit()
pred_ma2=ma2.predict(start=len(train),end=len(train)+len(test)-1,dynamic=False)

ma6=ARIMA(train['PopEst'],order=(0,6,0)).fit()
pred_ma6=ma6.predict(start=len(train),end=len(train)+len(test)-1,dynamic=False)


#5 compare MA prediction

plt.figure(figsize=(12,6))
plt.plot(train.index,train['PopEst'],labels='Train')
plt.plot(test.index,test['PopEst'],labels='Test',color='black')
plt.plot(test.index,pred_ma1,label="AR(1) prediction")
plt.plot(test.index,pred_ma2,label="AR(2) prediction")
plt.plot(test.index,pred_ma6,label="AR(6) prediction")
plt.legend()
plt.title("AR Model Forecasts")
plt.show()

#6 Evaluation

for label,pred in zip(["MA(1)","MA(2)","MA(6)"],[pred_ma1,pred_ma2,pred_ma6]):
    error =mean_squared_error(test["PopEst"],pred)
    print(f"{label} MSE:{error}:.2f")

#7 final forecast using best MA model

final_ma= ARIMA(df['PopEst'],lags=(0,2,0)).fit()
forecast= final_ma.predict(start=len(df),end=len(df)+12,dynamic=False)

plt.figure(figsize=(12,6))
plt.plot(df.index,df['PopEst'],label="historical data")
plt.plot(forecast.index,forecast,label="12-month forecast (MA(2))",color='red')
plt.legend()
plt.title("US Population Forecast using MA Model")
plt.show()
