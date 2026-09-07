# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 17:17:42 2026

@author: shrih
"""

#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.preprocessing.sequence import TimeseriesGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,LSTM
from sklearn.metrics import mean_squared_error
from math import sqrt


#load data set
df= pd.read_csv("C:/Time Series/monthly-milk-production.csv",index_col='Month',parse_dates=True)

#ensure the frequency of the index is monthly start (MS)
df.index.freq="MS"

#rename the production column to a shorter name for convenience
df.rename(columns={'Monthly milk production (pounds per cow)':"Production"},inplace=True)

print(df.head()) # display first 5 rows

#plot the original milk production time series
df.plot(figsize=(12,6),title="Monthly Milk Production")

#train test split
#use first 156 months (about 13 years) as training set
train=df.iloc[:156]
#remaining months are used as testing set
test=df.iloc[156:]

#scale the data between 0 and 1 (LSTMs work better with scaled input)
scaler=MinMaxScaler()
scaler.fit(train)   #fit only on training data
scaled_train=scaler.transform(train)
scaled_test=scaler.transform(test)

#create time series generator

#we will the past 12 months to predict the next month
n_input=12 # lookback window 12 month
n_features=1#univarate time series only production column

# time series generator automaticaly creates input output pairs for LSTM

generator=TimeseriesGenerator(scaled_train,scaled_train,length=n_input,batch_size=1)

'''

generator is the key part that prepares the training data 
for the LSTM model.
What it does:

TimeseriesGenerator automatically creates input-output pairs from a time 
series for supervised learning.

Inputs (X) = sequences of the last n_input months.

Outputs (y) = the next month’s value after those n_input months.

Here:

scaled_train → the training data (already scaled between 0 and 1).

length=n_input → lookback window = 12 months.

batch_size=1 → one sequence per batch (processed one by one).

Suppose scaled_train has 15 values:

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


and n_input = 3.

The generator will automatically create:

Input (X) → Output (y)

[1, 2, 3] → 4
[2, 3, 4] → 5
[3, 4, 5] → 6
...
[12, 13, 14] → 15


So the LSTM learns:
Given the last 3 numbers, predict the next one.

In our milk production dataset:
Given the last 12 months of milk production, predict the next month.
'''


#build LSTM model
model=Sequential()
#LSTM layer with 100 units relu activation input is (12 time steps, 1feature)
model.add(LSTM(100,activation='relu',input_shape=(n_input,n_features)))
#dense layer with 1 neuron(output = next months production)
model.add(Dense(1))
#compile model with adam optimizer and mean squared error lens
model.compile(optimizer='adam',loss='mse')

#train the model for 50 epochs using the training generator
model.fit(generator,epochs=50,verbose=1)


# Forecasting
test_predictions=[]
#take the last 12 months from training data as the first prediction input
first_eval_batch=scaled_train[-n_input:]
#scaled_train[-n_input:]- grabs the last 12 scaled values from the training
#these are used as the starting point to being forecasting

current_batch=first_eval_batch.reshape((1,n_input,n_features))
'''
LSTM expects input in 3D shapes
(batch_size timesteps feature)
here:
batch_size=1(one sequence at a time)
timesteps=n_input=12
feature =1(just one columns: milk production)
so current_batch is shaped is (1,12,1)    
'''

#predict step by step for each month in test set
for i in range(len(test)):
    #loop through the entire test dataset
    #we will predict one step at a time for the same length as the best data
    current_pred=model.predict(current_batch, verbose=0)[0]
    #the trained LSTM model predicts the next time step
    #current_batch contains the latest sequence of past observations
    #verbose=0 suppresses prediction logs
    #[0] extracts the predicted value from the returned array
    
    test_predictions.append(current_pred)
    #store the predicted value in the list 'test_predictions'
    #so that we can compare it later with the actual test values
    
    #update the batch (drop oldest month append newest predictions)
    
    current_batch=np.append(current_batch[:,1:,:],[[current_pred]],axis=1)
    #current batch[:, 1:,:] removes the oldest time step from the sequence 
    # This keeps the sliding window moving forward.
    
    
true_predictions=scaler.inverse_transform(test_predictions)
'''
sience training data was scaled (0-1) , predictions are also in that range
inverse_transform maps then back to the original milk production units(pound)

'''

#evaluation
#add prediction to set dataframe 
test['Predictions']=true_predictions
#calculate root mean squared error(RMSE)
rmse=sqrt(mean_squared_error(test['Production'],test['Predictions']))
print(f"Test RMSE:{rmse:.4f}")

#plot actual vs predicted values
test.plot(figsize=(14,5),title="Milk Production Forecast")
plt.show()    