# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 16:36:08 2026

@author: shrih
"""

#simple expoential smoothing (ses)
#used when the data has no trend and no seasonality
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import SimpleExpSmoothing
#simple level data (no trend)
data=[100,102,101,99,98,100,101,99,100,102]
ts=pd.Series(data)

#show nature of data
plt.figure()
plt.plot(ts,marker='o')
plt.title('Nature of Data: level only (no trend,no seasonality)')
plt.xlabel('Time')
plt.ylabel('Value')
plt.show()
###########################

#Holts Method (Double Expoential Smoothing)
#used when trend exists but no seasonality
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import Holt

#simple trend data
data=[50,55,60,65,70,75,80,85,90,95]
ts=pd.Series(data)

#show nature of data
plt.figure()
plt.plot(ts,marker='o')
plt.title('Nature of Data: trend present')
plt.xlabel('Time')
plt.ylabel('Value')
plt.show()

#model
model = Holt(ts)
fit = model.fit()

forecast = fit.forecast(3)
print("Forecast:",forecast)

#plot forecast
plt.figure()
plt.plot(ts,label="Actual")
plt.plot(fit.fittedvalues,label="Fitted")
plt.plot(forecast,label='Forecast')
plt.legend()
plt.title("Holt Trend Model Forecast")
plt.show()

##################################################

#Holt-winters method (triple Expoential smmothing)
#used when method + seasonality both exist
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

data=[120,130,150,170,
      140,150,170,190,
      160,170,190,210]

ts=pd.Series(data)

model= ExponentialSmoothing(ts,trend='add',seasonal='add',seasonal_periods=4)

fit= model.fit()
forecast=fit.forecast(4)
plt.figure()
#actual data

plt.plot(ts.index ,ts,marker='o',label="Actual")

#fitted values
plt.plot(ts.index,fit.fittedvalues,linestyle='--',label="Fitted")

#forecast index
future_index=range(len(ts),len(ts)+len(forecast))

plt.plot(future_index,forecast,marker='o',label='Forecast')

plt.title("Holt-winters forecast")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.show()



















forecast=fit.forecast(4)
plt.figure()

#actual data
plt.plot(ts.index,ts,marker='o',label="Actual")

#fitted values

plt.plot(ts)