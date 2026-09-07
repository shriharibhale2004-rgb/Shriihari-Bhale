# -*- coding: utf-8 -*-
"""
Created on Fri May  1 22:57:39 2026

@author: shrih
"""

'''
Dataset 1
Advertiesment dataset
'''
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

from feature_engine.outliers import Winsorizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

#1: load the dataset
df =pd.read_csv("C:/Assignment/EDA/advertising (1).csv")

print("Initial Shape",df.shape)
df.head()
#dataset shape 1000,10

#rename
df.columns=('Time','Age','Area_icon','Internet','Topic','City','Male','Country','Timestamp','Clicked')
#rename column name
#target column is clicked

#2: basic data qulity check
df.info()
print("\nMissing Values:\n ", df.isnull().sum())
 
#inference 
#dataset has no missing vallues 
#three feature is integer 3 feature float and 4 feature is object
#target column Clicked is integer encoded

#3 outliers detection
   
plt.figure(figsize=(12,6))
sns.boxplot(data=df.drop(columns=['Clicked']),orient='h')
plt.title("Boxplt of Advertiesment feature ")
plt.show()

#based on eda outliers were detected in:'
#Area_icon, 
#another column does not have significant outliers

#4: outlier treatment using winsorization

def winsorizer_column(df,col):
    """
    cops extreme values using IQR method.
    Lower cap =Q1- 1.5* IQR
    upper cap =Q3+ 1.5* IQR
    """
    winsor =Winsorizer(
        capping_method='iqr',
        tail='both',
        fold=1.5,
        variables=[col]
        )
    return winsor.fit_transform(df[[col]])

#apply distribution

# Ensure the name matches your 'def winsorizer_column'
for col in ['Time','Age','Area_icon','Internet','Male','Clicked',]:
    df[col] = winsorizer_column(df, col)    
        
print("Outliers treatment Completed")

#7 target variable label encoding
#convert numeric class labels into meaningful glass types 
#df['Clicked']=np.where['Clicked']==1, 'build_win_fl',df['Clicked']
#df['Clicked']=np.where['Clicked']==2, 'build_win_nfl',df['Clicked']
#df['Clicked']=np.where['Clicked']==3, 'veh_win_fl',df['Clicked']
#df['Clicked']=np.where['Clicked']==4, 'veh_win_nfl',df['Clicked']
#df['Clicked']=np.where['Clicked']==5, 'containers',df['Clicked']
#df['Clicked']=np.where['Clicked']==6, 'tabeleware',df['Clicked']
#df['Clicked']=np.where['Clicked']==7, 'headlamp',df['Clicked']

#df['Clicked'].value_counts()

#8: feature scaling - min max noemalization

X_features_numeric = df.drop(columns=['Clicked'])
scaler = MinMaxScaler()
#X_scaled = pd.DataFrame(scaler.fit_transform(X_features), columns=X_features.columns)

X_features_numeric = X_features_numeric.select_dtypes(include=[np.number])

X_scaled = pd.DataFrame(scaler.fit_transform(X_features_numeric), columns=X_features_numeric.columns)


#step 9 split input and output

X=np.array(X_scaled)
y= np.array(df['Clicked']) 

#step 10 train test split

X_train, X_test, y_train, y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42
    )
print("Training set size:", X_train.shape)
print("Test set size:",X_test.shape)

#final preprocessing summary
# identifier removed 
#outliers treated using Winsorization
#target labels made interpretable
#feature nolrmalized (0-1 range)
#data split into  train and test sets

print("Glass Datapreprocessing completed succesfully ")

#######################################################################

'''
Dataset 2
bank dataset
'''
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

from feature_engine.outliers import Winsorizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

#1: load the dataset
bank=pd.read_csv("C:/Assignment/EDA/bank_data (1).csv")

print("Initial Shape",bank.shape)
bank.head()
# shape 45211,32

#2: basic data qulity check
bank.info()
print("\nMissing Values:\n ", bank.isnull().sum())
 
#inference 
#dataset has no missing vallues 
#all input feature are numerric
#target column Y is integer encoded

#3 outliers detection
   
plt.figure(figsize=(12,6))
sns.boxplot(data=bank.drop(columns=['y']),orient='h')
plt.title("Boxplt of Bank feature ")
plt.show()

#based on eda outliers were detected in:'
#all column feature are outlier

#4: outlier treatment using winsorization

def winsorizer_column(df,col):
    """
    cops extreme values using IQR method.
    Lower cap =Q1- 1.5* IQR
    upper cap =Q3+ 1.5* IQR
    """
    winsor =Winsorizer(
        capping_method='iqr',
        tail='both',
        fold=1.5,
        variables=[col]
        )
    return winsor.fit_transform(df[[col]])

#apply distribution

# Ensure the name matches your 'def winsorizer_column'
for col in [""]:
    bank[col] = winsorizer_column(bank, col)    
    
    
print("Outliers treatment Completed")


bank['y']=np.where['y']==1, 'build_win_fl',bank['y']
bank['y']=np.where['y']==2, 'build_win_nfl',bank['y']
bank['y']=np.where['y']==3, 'veh_win_fl',bank['y']
bank['y']=np.where['y']==4, 'veh_win_nfl',bank['y']
bank['y']=np.where['y']==5, 'containers',bank['y']
bank['y']=np.where['y']==6, 'tabeleware',bank['y']
bank['y']=np.where['y']==7, 'headlamp',bank['y']

df['y'].value_counts()



#8: feature scaling - min max noemalization

X_features = bank.drop(columns=['y'])
scaler = MinMaxScaler()
X_scaled = pd.DataFrame(scaler.fit_transform(X_features), columns=X_features.columns)

#step 9 split input and output

X=np.array(X_scaled)
y= np.array(bank['y']) 

#step 10 train test split

X_train, X_test, y_train, y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42
    )
print("Training set size:", X_train.shape)
print("Test set size:",X_test.shape)

#final preprocessing summary
# identifier removed 
#outliers treated using Winsorization
#target labels made interpretable
#feature nolrmalized (0-1 range)
#data split into  train and test sets

print("Bank data Datapreprocessing completed succesfully ")


#################################################################

'''
Dataset 3
company dataset
'''
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

from feature_engine.outliers import Winsorizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

#1: load the dataset
data =pd.read_csv("C:/Assignment/EDA/Company_Data (1).csv")

print("Initial Shape",data.shape)
data.head()
#shape is 
#2: basic data qulity check
data.info()
print("\nMissing Values:\n ", data.isnull().sum())
 
#inference 
#dataset has no missing vallues 
#all input feature are numerric
#target column Type is integer encoded

#3 outliers detection
   
plt.figure(figsize=(12,6))
sns.boxplot(data=data.drop(columns=['Price']),orient='h')
plt.title("Boxplt of company feature ")
plt.show()

#based on eda outliers were detected in:'

#4: outlier treatment using winsorization

def winsorizer_column(df,col):
    """
    cops extreme values using IQR method.
    Lower cap =Q1- 1.5* IQR
    upper cap =Q3+ 1.5* IQR
    """
    winsor =Winsorizer(
        capping_method='iqr',
        tail='both',
        fold=1.5,
        variables=[col]
        )
    return winsor.fit_transform(df[[col]])

#apply distribution

# Ensure the name matches your 'def winsorizer_column'
for col in ['Sales', 'CompPrice', 'Income', 'Advertising', 'Population', 'Price','Age','Education']:
    data[col] = winsorizer_column(data, col)    
    
    
print("Outliers treatment Completed")

#
'''
data['Us']=np.where['Us']==1, 'build_win_fl',data['Us']
data['Us']=np.where['Us']==2, 'build_win_nfl',data['Us']
data['Us']=np.where['Us']==3, 'veh_win_fl',data['Us']
data['Us']=np.where['Us']==4, 'veh_win_nfl',data['Us']
data['Us']=np.where['Us']==5, 'containers',data['Us']
data['Us']=np.where['Us']==6, 'tabeleware',data['Us']
data['Us']=np.where['Us']==7, 'headlamp',data['Us']

df['Rape'].value_counts()
'''

#8: feature scaling - min max noemalization


X_features_numeric = data.drop(columns=['US'])
scaler = MinMaxScaler()
#X_scaled = pd.DataFrame(scaler.fit_transform(X_features_numeric), columns=X_features_numeric.columns)
# This automatically grabs only int and float columns
X_features_numeric = X_features_numeric.select_dtypes(include=[np.number])

X_scaled = pd.DataFrame(scaler.fit_transform(X_features_numeric), columns=X_features_numeric.columns)

#step 9 split input and output

X=np.array(X_scaled)
y= np.array(data['US']) 

#step 10 train test split

X_train, X_test, y_train, y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42
    )
print("Training set size:", X_train.shape)
print("Test set size:",X_test.shape)

#final preprocessing summary
# identifier removed 
#outliers treated using Winsorization
#target labels made interpretable
#feature nolrmalized (0-1 range)
#data split into  train and test sets

print("Comapny Data Datapreprocessing completed succesfully ")


#####################################################################


'''
dataset 4.
crime dataset
'''
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

from feature_engine.outliers import Winsorizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

#1: load the dataset
crime=pd.read_csv("C:/Assignment/EDA/crime_data (1).csv")

print("Initial Shape",crime.shape)
crime.head()
# shape 45211,32

#2: basic data qulity check
crime.info()
print("\nMissing Values:\n ", crime.isnull().sum())
 
#inference 
#dataset has no missing vallues 
#all input feature are numerric
#target column Y is integer encoded

#3 outliers detection
   
plt.figure(figsize=(12,6))
sns.boxplot(data=crime.drop(columns=['Unnamed: 0']),orient='h')
plt.title("Boxplt of Crime feature ")
plt.show()

#based on eda outliers were detected in:
# no outlier    
#all column feature are outlier

#4: outlier treatment using winsorization
#why winsorizer ?
#prevents extreme values from distorting distamce based models
#preserve dataset size
#suitable for manufacturing datasets

def winsorizer_column(df,col):
    """
    cops extreme values using IQR method.
    Lower cap =Q1- 1.5* IQR
    upper cap =Q3+ 1.5* IQR
    """
    winsor =Winsorizer(
        capping_method='iqr',
        tail='both',
        fold=1.5,
        variables=[col]
        )
    return winsor.fit_transform(df[[col]])

#apply distribution

# Ensure the name matches your 'def winsorizer_column'
for col in ['Murder','Assault','UrbanPop','Rape']:
    bank[col] = winsorizer_column(bank, col)    
    
    
print("Outliers treatment Completed")

'''
crime['Rape']=np.where['Rape']==1, 'build_win_fl',crime['Rape']
crime['Rape']=np.where['Rape']==2, 'build_win_nfl',crime['Rape']
crime['Rape']=np.where['Rape']==3, 'veh_win_fl',crime['Rape']
crime['Rape']=np.where['Rape']==4, 'veh_win_nfl',crime['Rape']
crime['Rape']=np.where['Rape']==5, 'containers',crime['Rape']
crime['Rape']=np.where['Rape']==6, 'tabeleware',crime['Rape']
crime['Rape']=np.where['Rape']==7, 'headlamp',crime['Rape']

df['Rape'].value_counts()
'''


#8: feature scaling - min max noemalization

#why scaling is mandatory:
# KNN is distance based
# chemical feature are on different scales
# prevents domiance of large magnitute feature


X_features_numeric = crime.drop(columns=['Unnamed: 0'])
scaler = MinMaxScaler()
#X_scaled = pd.DataFrame(scaler.fit_transform(X_features), columns=X_features.columns)
X_features_numeric = X_features_numeric.select_dtypes(include=[np.number])

X_scaled = pd.DataFrame(scaler.fit_transform(X_features_numeric), columns=X_features_numeric.columns)


#step 9 split input and output

X=np.array(X_scaled)
y= np.array(crime['Unnamed: 0']) 

#step 10 train test split

X_train, X_test, y_train, y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42
    )
print("Training set size:", X_train.shape)
print("Test set size:",X_test.shape)

#final preprocessing summary
# identifier removed 
#outliers treated using Winsorization
#target labels made interpretable
#feature nolrmalized (0-1 range)
#data split into  train and test sets

print("Bank data Datapreprocessing completed succesfully ")

#######################################################################


'''
datset 5
heary dusease datset
'''
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

from feature_engine.outliers import Winsorizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

#1: load the dataset
heart =pd.read_csv("C:/Assignment/EDA/heart disease (1).csv")

print("Initial Shape",heart.shape)
heart.head()
#shape is 
#2: basic data qulity check
heart.info()
print("\nMissing Values:\n ", heart.isnull().sum())
 
#inference 
#dataset has no missing vallues 
#all input feature are numerric
#target column Type is integer encoded

#3 outliers detection
   
plt.figure(figsize=(12,6))
sns.boxplot(data=heart.drop(columns=['target']),orient='h')
plt.title("Boxplt of heart disease feature ")
plt.show()

#based on eda outliers were detected in:'
# find outlier

#4: outlier treatment using winsorization
#why winsorizer ?
#prevents extreme values from distorting distamce based models
#preserve dataset size
#suitable for manufacturing datasets

def winsorizer_column(df,col):
    """
    cops extreme values using IQR method.
    Lower cap =Q1- 1.5* IQR
    upper cap =Q3+ 1.5* IQR
    """
    winsor =Winsorizer(
        capping_method='iqr',
        tail='both',
        fold=1.5,
        variables=[col]
        )
    return winsor.fit_transform(df[[col]])

#apply distribution

# Ensure the name matches your 'def winsorizer_column'
for col in [ 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg','thalach','exang','oldpeak','slope','ca','thal','target']:
    data[col] = winsorizer_column(data, col)    
    
    
print("Outliers treatment Completed")

#8: feature scaling - min max noemalization

#why scaling is mandatory:
# KNN is distance based
# chemical feature are on different scales
# prevents domiance of large magnitute feature


X_features_numeric = heart.drop(columns=['target'])
scaler = MinMaxScaler()
X_scaled = pd.DataFrame(scaler.fit_transform(X_features_numeric), columns=X_features_numeric.columns)
# This automatically grabs only int and float columns
#X_features_numeric = X_features.select_dtypes(include=[np.number])

#X_scaled = pd.DataFrame(scaler.fit_transform(X_features_numeric), columns=X_features_numeric.columns)

#step 9 split input and output

X=np.array(X_scaled)
y= np.array(heart['target']) 

#step 10 train test split

X_train, X_test, y_train, y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42
    )
print("Training set size:", X_train.shape)
print("Test set size:",X_test.shape)

#final preprocessing summary
# identifier removed 
#outliers treated using Winsorization
#target labels made interpretable
#feature nolrmalized (0-1 range)
#data split into  train and test sets

print("Comapny Data Datapreprocessing completed succesfully ")


#######################################################################

'''
dataset 6.
cars datsset
'''
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

from feature_engine.outliers import Winsorizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

#1: load the dataset
car=pd.read_csv("C:/Assignment/EDA/mtcars (1).csv")

print("Initial Shape",car.shape)
car.head()
#shape is 
#2: basic data qulity check
car.info()
print("\nMissing Values:\n ", car.isnull().sum())
 
#inference 
#dataset has no missing vallues 
#all input feature are numerric
#target column Type is integer encoded

#3 outliers detection
   
plt.figure(figsize=(12,6))
sns.boxplot(data=car.drop(columns=['carb']),orient='h')
plt.title("Boxplt of cars feature ")
plt.show()

#based on eda outliers were detected in:'
# find outlier
#4: outlier treatment using winsorization

def winsorizer_column(df,col):
    """
    cops extreme values using IQR method.
    Lower cap =Q1- 1.5* IQR
    upper cap =Q3+ 1.5* IQR
    """
    winsor =Winsorizer(
        capping_method='iqr',
        tail='both',
        fold=1.5,
        variables=[col]
        )
    return winsor.fit_transform(df[[col]])

#apply distribution

# Ensure the name matches your 'def winsorizer_column'
for col in ['mpg','cyl','disp','hp','drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']:
    data[col] = winsorizer_column(data, col)    
    
    
print("Outliers treatment Completed")

#8: feature scaling - min max noemalization

X_features_numeric = car.drop(columns=['carb'])
scaler = MinMaxScaler()
X_scaled = pd.DataFrame(scaler.fit_transform(X_features_numeric), columns=X_features_numeric.columns)
# This automatically grabs only int and float columns
#X_features_numeric = X_features.select_dtypes(include=[np.number])

#X_scaled = pd.DataFrame(scaler.fit_transform(X_features_numeric), columns=X_features_numeric.columns)

#step 9 split input and output

X=np.array(X_scaled)
y= np.array(car['carb']) 

#step 10 train test split

X_train, X_test, y_train, y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42
    )
print("Training set size:", X_train.shape)
print("Test set size:",X_test.shape)


print("Comapny Data Datapreprocessing completed succesfully ")

########################################################################################

'''
dataset 7
'''

import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

from feature_engine.outliers import Winsorizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

#1: load the dataset
air=pd.read_excel("C:/Assignment/EDA/EastWestAirlines (1).xlsx")

print("Initial Shape",air.shape)
air.head()
#shape is 
#2: basic data qulity check
air.info()
print("\nMissing Values:\n ", air.isnull().sum())
 
#inference 
#dataset has no missing vallues 
#all input feature are numerric
#target column Type is integer encoded

#3 outliers detection
   
plt.figure(figsize=(12,6))
sns.boxplot(data=air.drop(columns=['Award?']),orient='h')
plt.title("Boxplt of cars feature ")
plt.show()

#based on eda outliers were detected in:'
# find outlier
#all colimns are finding outiler

#4: outlier treatment using winsorization
def winsorizer_column(air,col):
    """
    cops extreme values using IQR method.
    Lower cap =Q1- 1.5* IQR
    upper cap =Q3+ 1.5* IQR
    """
    winsor =Winsorizer(
        capping_method='iqr',
        tail='both',
        fold=1.5,
        variables=[col]
        )
    return winsor.fit_transform(air[[col]])

#apply distribution

# Ensure the name matches your 'def winsorizer_column'
for col in ['mpg','cyl','disp','hp','drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']:
    data[col] = winsorizer_column(data, col)    
    
    
print("Outliers treatment Completed")
#outlier winsorizer are remove the outilier

#8: feature scaling - min max noemalization

X_features_numeric = car.drop(columns=['carb'])
scaler = MinMaxScaler()
X_scaled = pd.DataFrame(scaler.fit_transform(X_features_numeric), columns=X_features_numeric.columns)
# This automatically grabs only int and float columns
#X_features_numeric = X_features.select_dtypes(include=[np.number])

#X_scaled = pd.DataFrame(scaler.fit_transform(X_features_numeric), columns=X_features_numeric.columns)

#step 9 split input and output

X= np.array(X_scaled)
y= np.array(car['carb']) 

#step 10 train test split

X_train, X_test, y_train, y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42
    )
print("Training set size:", X_train.shape)
print("Test set size:",X_test.shape)

