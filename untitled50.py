# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 16:11:08 2026

@author: shrih
"""
import pandas as pd
import numpy as np
import statsmodels.graphics.tsaplots as tsa_plots
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
from sklearn.metrics import mean_squared_error
from math import sqrt
from matplotlib import pyplot

#load dataset
Walmart =pd.read_csv("C:/Time Series/Walmart Footfalls Raw.csv")

#data partition train =first 147,test=last12
Train=Walmart.head(147)
Test=Walmart.tail(12)

#step 1 check stationary with ADF test

print("==== Stationarity check (ADF test)===")
result= adfuller(Train.Footfalls)
print("ADF statistic",result[0])
print("p=value:",result[1])

#rule of thumb:
# if p -value > 0.05 - series is NOT stationary - apply differencing
#if p-value< 0.05 - series is stationary- d=0


#try 1st order fifferencing    
diff1=Train.Footfalls.diff().dropna()
result1=adfuller(diff1)
print("aafter 1st difference - p-value:",result[1])

#try 2nd order difference if needed
diff2=diff1.diff().dropna()
result2=adfuller(diff2)
print("After 2nd difference - p-value:",result[1])


#step 2 plot ACF & PACF (to decide p and q)
tsa_plots.plot_acf(Walmart.Footfalls,lags=12) #suggest q
tsa_plots.plot_pacf(Walmart.Footfalls,lags=12) #suggest p

#step 3 Fit ARIMA model
#example ARIMA with AR =4 d=1 MA=6
#AR (p)=4-taken from PACF
#d=1-from ADF test differencing
#MA (q) = 6-taken from ACF
model1 =ARIMA(Train.Footfalls, order=(4,1,6))
res1 =model1.fit()

print("\n===ARIMA model summary")
print(res1.summary())

'''
model selection criteria
AIC = 1813.093
BIC = 1845.913
HQIC = 1826.428
These are penalized fit measure
AIC (Akaike information criteruan)
balances model fit vs complexity
lower is better
BIC (Bayesian Information Criterian)
similar to AIC but penalizes complex models more strongly
HOIC (hanman ouinn criterian)

Interpretion of each coefficient
AR terms
ar.l1=-0.7199,p=0.211 -> not sigginificant
ar.l2-0.7579,p=0.043 -> sigginificant
ar.l3 =-7094 ,p=0.220 -> not sigginificant
ar.l4 =0.2441,p=0.515 -> not siggnificant

only AR(2) is contributing meaningfully
MA terms
ma.l1 = 0.2439 ,p=0.625 -> not sigginificant
ma.l2= 0.7279,p=0.093 -> borderline(weak evidence)
ma.l3 =0.1224,p=0.843 -> not siggnificant
ma.l4=-0.7716 ,p=0.215 -> not significant
ma.l5 =-0.1027,p=0.694 -> not significant
ma.l6 =-0.5691,p=0.042 -> significant

only MA(6) is clearly significant while MA(2) is borderline

final takeaways
out of 10 parameters (AR4+MA6),only AR(2) and  MA(6) are
statistically significance
the rest any be noise - your model might be over parameterized

A simpler model like ARIMA (2,1,1) or ARIMA(2,1,2)
may perform equally well (with lower AIC/BIC)

In plain words
your ARIMA (4,1,6) modle fits but most coefficients are not statist and comapare AIC/BIC + RMSE
'''

#step 4 forecast for test data
start_index=len(Train)
end_index=start_index+len(Test) -1 
forecast_test =res1.predict(start=start_index,end=end_index)

print("\nForecasted Values")
print(forecast_test)


#step 5 evaluate forecast accuracy
rmse_test=sqrt(mean_squared_error(Test.Footfalls,forecast_test))
print("\ntest RMSE: %.3",rmse_test)

# step 6 Plot Actual vs predicted
pyplot.plot(Test.Footfalls, label="Actual")
pyplot.plot(forecast_test,color='red',label="Forecast")
pyplot.legend()
pyplot.show()

      

##################################################################################

import pandas as pd 
import statsmodels.graphics.tsaplots as tsa_plots
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
from math import sqrt
from matplotlib import pyplot

walmart =pd.read_csv("C:/Time Series/Walmart Footfalls Raw.csv")
#data partition
Train=Walmart.head(147)
Test=Walmart.tail(12)

tsa_plots.plot_acf(walmart.Footfalls,lags=12)
tsa_plots.plot_pacf(walmart.Footfalls,lags=12)

'''
[5:21 pm, 27/6/2026] Shrihari Bhale: When analyzing ACF and PACF plots, we folLow these rules:

AR Order (p) from PACF:

Look at the Partial Autocorrelation Function (PACF) plot. The number of significant Lags before the PACF drops to near zero suggests the AR order.

If PACF shows a sharp cutoff after Lag 4, we take AR(4). MA Order (q) from ACF:

Look at the Autocorrelation Function (ACF) plot. The number of sianificant Laas d

Stop sharing

zero suaaest
ook at the Autocorrelation Function (ACF) plot.

he number of significant lags before the ACF drops to near zero s. f ACF shows a sharp cutoff after lag 6, we take MA(6).

First you try p=4 and q=4 Then you try p=4 and q=6
'''
#ARIMA wirh AR=4, MA =6
model1=ARIMA(Train.Footfalls,order=(4,1,6))
res1=model1.fit()
print(res1.summary())

'''
Creates an ARIMA model with:

AR (Auto-Regressive) term = 4

I (Integrated) term = 1 (indicates first-order differencing to make the data stationary

MA (Moving average) term= 6
'''

#forecast for next 12 month
start_index=len(Train)
end_index=start_index+11
forecast_test =res1.predict(start=start_index,end=end_index)

print(forecast_test)
'''
start_index =len (Train begins prediction after the training dataset)
end_index =start_index +11: predicts the next 12 periods
res1.predict(start=start_index,end=end_index) generate forecast
'''
#evaluate forecast
rmse_test=sqrt(mean_squared_error(Test.Footfalls,forecast_test))
print("\ntest RMSE: %.3",rmse_test)

# plot forecast against actual outcomes
pyplot.plot(Test.Footfalls)
pyplot.plot(forecast_test,color='red')
pyplot.show()

#Auto ARIMA Automatically discover the optimal order for an ARIMA model
#php install pmdarima user

'''
pmdarima is an Auto-ARIMA package that automatically selects the best (p,d,q) parameters for ARIMA.
start_p=0, start_q=0: Initial values for AR and MA terms.
max_p=12, max_q=12: Maximum values for AR and MA.
m=1: Indicates a non-seasonal model.
d=None: Automatically determines the differencing order.
seasonal=False: Disables seasonal components.
trace=True: Displays the selection process.
stepwise=True: Uses a stepwise approach for efficiency.
'''

import pmdarima as pm
ar_model=pm.auto_arima(Train.Footfalls,start_p=0,start_q=0,
                       max_p=12,max_q=12, #maximum p and 1
                       m=1, #frequency of series
                       d=None,# let model determine 'd
                       seasonal=False,#no seasonality
                       start_p=0,trace=True,
                       error_action='warm', stepwise=True)

#best parameters ARIMA 
#ARIMA with AR=3, I=1, MA =5
model=ARIMA(Train.Footfalls,order=(3,1,5))
res =model.fit()
print(res.summary())

#forecast for next 12 months
start_index= len(Train)
end_index=start_index + 11
forecast_best=res.predict(start=start_index,end=end_index)

print(forecast_best)

#evlueate forecasts
rmse_best =sqrt(mean_squared_error(Test.Footfalls,forecast_best))
print('test RMSE:%.3f' %rmse_best)

#plot forecast against actual outcomes
pyplot.plot(Test.Footfalls)
pyplot.plot(forecast_best,color='red')
pyplot.show()

#forecast for future 12 months
start_index=len(Walmart)
end_index=start_index+ 11
forecast=res1.predict(start=start_index,end=end_index)

print(forecast)
