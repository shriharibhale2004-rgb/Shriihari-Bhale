# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 20:26:19 2026

@author: shrih
"""

# import required libraries

import pandas as pd
import numpy as np

# visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns

#stastical library
from scipy.stats import skew

#preprocessing libraries
from sklearn.preprocessing import StandardScaler

#model building libraries 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier

#evalution libraries
from sklearn.metrics import accuracy_score, confusion_matrix

#set seaborn style
sns.set()

#2 load the dataset

data=pd.read_csv("C:/Boosting/movies_classification.csv")

#display first 5 rows
print(data.head())

#dataset information
print(data.info())

#missing values
print(data.isna().sum)

#explratory data analysis

#target variable distribution
target =data["Start_Tech_Oscar"]

sns.countplot(x=target,palette='winter')
plt.xlabel('Oscar status')
plt.ylabel('Count')
plt.title('distribution of Oscar winning movies')
plt.show()


# correlation heat map

plt.figure(figsize=(16,8))
#select only numerical columns
numeric_df=data.select_dtypes(include=[np.number])
#correlation heatmap
sns.heatmap(numeric_df.corr(),
            annot=True,
            cmap='YlGnBu',
            fmt='.2f'
   )
plt.title("Correlation Heatmap")
plt.show()
'''
1.Rating are highly correlated
2.Budget and production expense affect collection
3.Oscar prediction is not linearly correlated
4.Multicollinearity exists
'''
#genre vs oscar analysis
sns.countplot(
    x='Genre',
    data=data,
    hue='Start_Tech_Oscar',
    palette='pastel'
    )

plt.title('Oscar chance based on Genre')
plt.show()

#thriller and comedy movie has high probability of getting oscar

# 3D availability vs oscar

sns.countplot(
    x='3D_available',
    data=data,
    hue='Start_Tech_Oscar',
    palette='pastel'
    )
plt.title('Oscar chance based on 3D Availability')
plt.show()

#movies with 3D availability have better Oscar chance

#outlier detection using boxplots

plt.figure(figsize=(12,8))

plt.subplot(2,2,1)
sns.boxplot(x=data['Twitter_hastags'])
plt.titel('Twitter hastags')

plt.subplot(2,2,2)
sns.boxplot(x=data['Marketing expense'])
plt.titel('Marketing expense')

plt.subplot(2,2,3)
sns.boxplot(x=data['Time_taken'])
plt.titel('Time_taken')

plt.subplot(2,2,4)
sns.boxplot(x=data['Avg_age_actors'])
plt.titel('Avg_age_actors')



#winsorization for oulier treatment
from feature_engine.outliers import Winsorizer

winsor = Winsorizer(
    capping_method='iqr',
    tail='both',
    fold=1.5,
    variables=[
        'Twitter_hashtags',
        'marketing expense'])



#check skewness

#create dataframe for skewness analysis
skew_df=pd.DataFrame(
    data.select_dtypes(np.number).columns,
    coluns=['Feature']
   )
#calculate skewness
skew_df['Skew']=skew_df['Frature'].apply(
    lambda feature: skew(data[feature])
    )
#absolute skewness
skew_df['Absolute Skew']=skew_df['Skew'].abs()

#mark highly skewed columns
skew_df['Skewed']=skew_df['Absolute Skew']>=0.5

print(skew_df)

#log transformation for skewed features

#apply log transformation
for column in skew_df.query("Skewed==True")['Feature'].values:
    #avoid transformaing target variable
    if column !="Start_Tech_Oscar":
        data[column]=np.log1p(data[column])
        
print(data.head()) 

 #encoding categorical variables

#create copy
dat_encoded = data.copy()
#one hot encoding
data_encoded=pd.get_dummies(dat_encoded)

print(data_encoded.head()) 

#feature scaling    

#seperate target variables
y=data_encoded['Start_Tech_Oscar']

#drop target from predictors
X=data_encoded.drop("Start_Tech_Oscar",axis=1)

#standardization 
scaler=StandardScaler()

X_scaled =scaler.fit_transform(X)

#convert back to dataframe
X_scaled =pd.DataFrame(
    X_scaled,
    columns=X.columns
    )
print(X_scaled.head())

#7 train test spilt
X_train,X_test,y_train,y_test =train_test_split(
    X_scaled,
    y.astype(int),
    test_size=0.2,
    stratify=y,
    random_state=42
    )
print("Training Shape:",X_train.shape)
print("Test shape:",X_test.shape)

#8 model building adaboost

ada_clf=AdaBoostClassifier(
    learning_rate=0.02,
    n_estimators=500,
    random_state=42
    )
#train rhe model
ada_clf.fit(X_train,y_train)

#9 model evaluation
#prediction on test data
y_pred_test =ada_clf.prediction(X_test)

#confusion matrix
cm=confusion_matrix(y_test, y_pred_test)
print("\n Confusion matrix:\n",cm)

#test accuracy
test_accuracy=accuracy_score(y_test,y_pred_test)
print("\nTesting Accuracy:",test_accuracy)

#training accuracy
y_pred_train=ada_clf.predict(X_train)

train_accuracy=accuracy_score(y_train,y_pred_train)
print("\nTesting Accuracy:",train_accuracy)

#final observation

'''
1 adaboost improves classification performance
2 collection and ratings influence Oscar predictive
3 Twitter hashtags have weaker impact
4 feature engineering and preprocessing improve aacuracy

'''

#business benifits
# better mvie investment decisions
#improved production planning strategies
# higher probability of production award winning movies
# better 

#####################################################################



# import required libraries

import pandas as pd
import numpy as np

# visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns

#stastical library
from scipy.stats import skew

#preprocessing libraries
from sklearn.preprocessing import StandardScaler

#model building libraries 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier

#evalution libraries
from sklearn.metrics import accuracy_score, confusion_matrix

#set seaborn style
sns.set()

#2 load the dataset

data=pd.read_csv("C:/Assignment/Boosting/delivery_time (1).csv")

#display first 5 rows
print(data.head())

#dataset information
print(data.info())

#missing values
print(data.isna().sum)

#explratory data analysis

#target variable distribution
target =data["Sorting Time"]

sns.countplot(x=target,palette='winter')
plt.xlabel('dilivery time ')
plt.ylabel('sorting time')
plt.title('distribution of dilivery time')
plt.show()


# correlation heat map

plt.figure(figsize=(16,8))
#select only numerical columns
numeric_df=data.select_dtypes(include=[np.number])
#correlation heatmap
sns.heatmap(numeric_df.corr(),
            annot=True,
            cmap='YlGnBu',
            fmt='.2f'
   )
plt.title("Correlation Heatmap")
plt.show()
'''
1.Rating are highly correlated
2.Budget and production expense affect collection
3.Oscar prediction is not linearly correlated
4.Multicollinearity exists
'''
#genre vs oscar analysis
sns.countplot(
    x='Genre',
    data=data,
    hue='Sorting Time',
    palette='pastel'
    )

plt.title('dilivery time')
plt.show()

#thriller and comedy movie has high probability of getting oscar

# 3D availability vs oscar

sns.countplot(
    x='3D_available',
    data=data,
    hue='Start_Tech_Oscar',
    palette='pastel'
    )
plt.title('Oscar chance based on 3D Availability')
plt.show()

#movies with 3D availability have better Oscar chance

#outlier detection using boxplots

plt.figure(figsize=(12,8))

plt.subplot(2,2,1)
sns.boxplot(x=data['Twitter_hastags'])
plt.titel('Twitter hastags')

plt.subplot(2,2,2)
sns.boxplot(x=data['Marketing expense'])
plt.titel('Marketing expense')

plt.subplot(2,2,3)
sns.boxplot(x=data['Time_taken'])
plt.titel('Time_taken')

plt.subplot(2,2,4)
sns.boxplot(x=data['Avg_age_actors'])
plt.titel('Avg_age_actors')



#winsorization for oulier treatment
from feature_engine.outliers import Winsorizer

winsor = Winsorizer(
    capping_method='iqr',
    tail='both',
    fold=1.5,
    variables=[
        'Twitter_hashtags',
        'marketing expense'])



#check skewness

#create dataframe for skewness analysis
skew_df=pd.DataFrame(
    data.select_dtypes(np.number).columns,
    coluns=['Feature']
   )
#calculate skewness
skew_df['Skew']=skew_df['Frature'].apply(
    lambda feature: skew(data[feature])
    )
#absolute skewness
skew_df['Absolute Skew']=skew_df['Skew'].abs()

#mark highly skewed columns
skew_df['Skewed']=skew_df['Absolute Skew']>=0.5

print(skew_df)

#log transformation for skewed features

#apply log transformation
for column in skew_df.query("Skewed==True")['Feature'].values:
    #avoid transformaing target variable
    if column !="Start_Tech_Oscar":
        data[column]=np.log1p(data[column])
        
print(data.head()) 

 #encoding categorical variables

#create copy
dat_encoded = data.copy()
#one hot encoding
data_encoded=pd.get_dummies(dat_encoded)

print(data_encoded.head()) 

#feature scaling    

#seperate target variables
y=data_encoded['Start_Tech_Oscar']

#drop target from predictors
X=data_encoded.drop("Start_Tech_Oscar",axis=1)

#standardization 
scaler=StandardScaler()

X_scaled =scaler.fit_transform(X)

#convert back to dataframe
X_scaled =pd.DataFrame(
    X_scaled,
    columns=X.columns
    )
print(X_scaled.head())

#7 train test spilt
X_train,X_test,y_train,y_test =train_test_split(
    X_scaled,
    y.astype(int),
    test_size=0.2,
    stratify=y,
    random_state=42
    )
print("Training Shape:",X_train.shape)
print("Test shape:",X_test.shape)

#8 model building adaboost

ada_clf=AdaBoostClassifier(
    learning_rate=0.02,
    n_estimators=500,
    random_state=42
    )
#train rhe model
ada_clf.fit(X_train,y_train)

#9 model evaluation
#prediction on test data
y_pred_test =ada_clf.prediction(X_test)

#confusion matrix
cm=confusion_matrix(y_test, y_pred_test)
print("\n Confusion matrix:\n",cm)

#test accuracy
test_accuracy=accuracy_score(y_test,y_pred_test)
print("\nTesting Accuracy:",test_accuracy)

#training accuracy
y_pred_train=ada_clf.predict(X_train)

train_accuracy=accuracy_score(y_train,y_pred_train)
print("\nTesting Accuracy:",train_accuracy)

#final observation

'''
1 adaboost improves classification performance
2 collection and ratings influence Oscar predictive
3 Twitter hashtags have weaker impact
4 feature engineering and preprocessing improve aacuracy

'''

#business benifits
# better mvie investment decisions
#improved production planning strategies
# higher probability of production award winning movies
# better 

