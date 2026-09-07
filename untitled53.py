# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 16:32:43 2026

@author: shrih
"""



'''
'Sarima ' is not about fitting a model directly it is about
answering six questions

is my data stationary
how many regular difference (d)
how many seasonal difference (D)
what are p and q
what are P and Q
can this model forecast future values

step1 load dataset
we need historical data
here we are using the famous AirPassangers dataset
it contains
monthly passengers
from 1949 - 1960
the original dataset has only numbers
time series models require

date as index 
we create a proper date column 
step2 plot original series
before building any model what should we do 

visualize the data
look for trend 
sesnality
cycles
noise

data is not stationary
step 3 ADF tesst
can ARIMA work directly on this data
answer
no 
because ARIMA assumes 
stationary data
therefore

need differencing
step4 first difference
we calculate
118-112 =6

129-132=-3
again perform
ADF test
if stationary

monthly data
season = 12

so 
ts.diff(12)
this removes yearly seasonality
again
ADF test 

if stationary
D=1
step 6 create stationary series

now perform 
both difference
ts.diff().diff(12)
meaning
remove
trend
seasonality
now data becomes stationary
again verify using
ADF

students should understand
this stationary series is not used for forecasting
it is only used to identify
p,q,P,Q
step7 ACF plot
ACF
=
AutoCorrelation function
it tells
How today value depends upon previous error
if spike appears
at log 1
q=1
if spike appears
at log12
Q=1
remeber 
ACF gives
moving average terms

step8 PACF plot
PACF
partial Autocorrelation
measures direct relationship
if spike
log1
p=1
seasonal spike
log12
P=1
|graph             parameter
PACF               p
ACF                q
seasonal PACF           P
seasonal ACF          Q

step 9 fit SARIMA 
now all parameter are availabel
step 10 model evaluation
explain
AIC and BIC
both measure
model quality
Step 11 forecast
forcast =result.forecast(24)
means
predict
next
24 months
studentd should understand
model uses
'''
# complete SARIMA workflow
#suppress warnings
import warnings
warnings.filterwarnings('ignore')

#libraries
import pandas as pd
import matplotlib.pyplot as plt

from statsmodels.datasets import get_rdataset
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
from statsmodels.tsa.statespace.sarimax import SARIMAX 

#step 1 load data

#AirPassengers dataset (monthly airline passengers)
data=get_rdataset("AirPassengers").data

#create date column
data['Month']=pd.date_range(
    start="1949-01-01",
    periods=len(data),
    freq='MS'
    )
#set datetime index
data.set_index('Month',inplace=True)

# time series
ts=data['value']
print("First 5 Records")
print(ts.head())

#step 2 plot original serites

plt.figure(figsize=(12,5))
plt.plot(ts)

plt.title("Monthly Airline Passengers")
plt.xlabel("Date")
plt.ylabel("Passengers")

plt.grid(True)
plt.show()


#step 3 ADF test on original serites

print("\nADF Test : Original Series")

result = adfuller(ts)
print("ADF p-valueL:",result[1])

if result[1] <0.05:
    print("seris is stationary")
else:
    print("series is Not stationary")    

#step 4 First Differencing
#determines d

ts_diff=ts.diff().dropna()

plt.figure(figsize=(12,5))
plt.plot(ts.diff())

plt.title("First Differenced Series")
plt.grid(True)
plt.show()

print("\nADF test : first difference")

result=adfuller(ts_diff)

print("ADF p-value:",result[1])
if result[1] <0.05:
    print("Series is stationary")
else:
    print("Series is not Stationary")    

#if stationary here d=1

#step 5 Seasonal Differencing
#datermine D

#monthly data-> yearly sesonality
s=12 
ts_seasonal_diff=ts.diff(12).dropna()

plt.figure(figsize=(12,5))
plt.plot(ts_seasonal_diff)

plt.title("Seasonal Difference (Log=12)")
plt.grid(True)
plt.show()

print("\nADF test Seasonal difference")
result = adfuller(ts_seasonal_diff)

print("ADF p-value:", result[1])

if result[1]<0.05:
    print("series is stationary")
else:
    print("series is not stationary")
    
#used for ACF/PACF

#regular difference + seasonal difference
stationary_series=ts.diff().diff(12).dropna()
plt.figure(figsize=(12,5))
plt.plot(stationary_series)

plt.title("stationary series")
plt.grid(True)
plt.show()

print("\nADF test : stationary series")

result=adfuller(stationary_series)

print("ADF p-value:",result[1])

if result[1]<0.05:
    print("series is stationary")
else:
    print("series is not stationary")


# step 7 ACF Plot
#used to estimate q and p

plot_acf(
    stationary_series,
    lags=40)
plt.show()

#significant spike at lag 1 -> q=1
#singificant spike at lag 12 -> Q=1

#step 8 PACF plot
#used to estimate p and q

plot_pacf(
    stationary_series,
    lags=40
    )
plt.show()

#step 9 fit sarima model

#example 
#p =1 ,d=1,q=1
#P=1,D=1,Q=1
#s=12

model = SARIMAX(
    ts,
    order=(1,1,1),
    seasonal_order=(1,1,1,12)
    )
result = model.fit()

#model summary
print(result.summary())

#step 10 Model Evaluation
print("\n AIC:",result.aic)
print("\nBIC:",result.bic)

#lower AIC/BIC generally indicates a better model


#step 11  Forecast next 24 Months

forecast = result.forecast(steps=24)

print("\nForecast Value")
print(forecast)

#step 12 plot forecast

plt.figure(figsize=(14,6))

plt.plot(
    ts,
    label="Actual"
    )
plt.plot(
    forecast,
    color='red',
    label="Forecast"
    )

plt.title("SARIMA Forecast")
plt.xlabel("Date")
plt.ylabel("Passengers")
plt.legend()
plt.grid(True)
plt.show()