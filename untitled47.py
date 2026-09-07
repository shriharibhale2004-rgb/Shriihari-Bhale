# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 17:10:29 2026

@author: shrih
"""

#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AutoReg
from sklearn.metrics import mean_squared_error
import warnings
warnings.filterwarnings('ignore')

#1 load dataset and preprocess
df=pd.read_csv("C:/Time Series/uspopulation.csv",index_col='DATE',parse_dates=True)
'''
index_col='DATE'
this tells pandas:
"use the column named date as the raw index of the Dataframe"
normally,pandas gives rows numeric indexes (0,1,2,..)
But here we want time series indexing- rows indexed by dates
instead of numbers
parse_dates=True
by default pandas reads dates as plain strings("2011-01-01")
with parse_dates=True pandas converts them into datetime object(timestamp) 
this allows us to do time series operation like:
    resamplingby montg/year
    extracting . month ,year
'''

#tell pandas that data is monthly (MS =month start)
df.index.freq="MS"

print(df.head())
#output (first few rows should look like this):

#pop est
#date 
#2011-01-01  311037
#2011-02-01  311189
#2011-03-01  311351

#plot the data
df['PopEst'].plot(figure=(12.5),title='U.S.Monthly Population Estimate')
plt.ylabel("Population Estimate")
plt.show()

#EXPECTED plot : Upward trend in population over time

#2 train test split

#first 84 months - training last 12 months - testing
len(df)
train=df.iloc[:84]
test=df.iloc[84:]

print(len(train), len(test))

#Expected 84 training samples 12 test samples

#3 Fit AR models with different lags


#AR(1) model - uses 1 previous observation to predict the next
model=AutoReg(train['PopEst'],lags=1).fit()
pred1=model.pred1.predict(start=len(train),end=len(train)+len(test)-1,dynamic=False)

'''
len(df)=96
|<-------Train (84 months)-------->|<------ Test (12 months)---->|
2011----------------2017   2018
index: 0----------------------------83|84--------------95

Dynamic Parameter Intuition
dynamic=false:
At each test step it uses the ewal observed value from the past
more accurate (good for evaluation)
dynamic=true:
At each step it uses its own previous prediction (not real past)
mimics "real forecasting" (when actuals are unknown) 
Errors any accumalate   
'''

#AR(2) model uses 2 previous observation
model2=AutoReg(train['PopEst'],lags=2).fit()
pred2=model2.pred1.predict(start=len(train),end=len(train)+len(test)-1,dynamic=False)

#AR(11)model- uese 11 previous observation (chosen based on AIC in original cos)
model_auto=AutoReg(train['PopEst'],lags=11).fit()
pred_auto=model_auto.pred_auto.predict(start=len(train),end=len(train)+len(test)-1,dynamic=False)

#4 cpmpare prediction with actual values

plt.figure(figsize=(12,6))

#plot training data 
plt.plot(train.index,train['PopEst'],labels='Train')

#plot actual test value
plt.plot(test.index,test['PopEst'],labels='Test',color='black')

#plot prediction from different Ar models

plt.plot(test.index,pred1,label="AR(1) prediction")
plt.plot(test.index,pred2,label="AR(2) prediction")
plt.plot(test.index,pred_auto,label="AR(11) prediction")

plt.legend()
plt.title("AR Model Forecasts")
plt.show()

#Expected plot: AR(1) line should closely follow test values
#AR (2) AR(11) might lag slightly behind


#5 Evaluation (MSE)
#calculate mean squared error (lower is better)
for label,pred in zip(["AR(1)","AR(2)","AR(11)"],[pred1,pred2,pred_auto]):
    error =mean_squared_error(test["PopEst"],pred)
    print(f"{label} MSE:{error}:.2f")   

#Expected output (approximate) 
#AR(1) MSE : 17449.71
#AR(2) MSE : 2713.26
#AR(11) MSE : 3206.15

# Forecast future population
# Retrain AR(2) model on the full dataset for final forecasting
final_model=AutoReg(df["PopEst"],lags=2).fit()

#forecast next 12 months
forecast = final_model.predict(start=len(df),end=len(df)+12,dynamic=False)

print(forecast.head())
#Expected first future prediction (values slightly higher than last PopEst)

#plot forecast vs historical data
plt.figure(figsize=(12,6))
plt.plot(df.index,df['PopEst'],label="historical data")
plt.legend()
plt.title("US Population Forecast using AR(2)")
plt.show()
#expected ploT red forecast line continue the upward trend of population         