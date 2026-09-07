# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 17:12:35 2026

@author: shrih
"""

import pandas as pd

df=pd.read_csv("C:/Bagging technique/diabetes_puma.csv")
df.head()
df.isnull().sum()
df.describe()
df.Outcome.value_counts()
#0 500
#1 286
#there is slight imbalance is our datset but since
#it is not major we will not worry about it!

x= df.drop('Outcome',axis='columns')
y=df.Outcome

#x contains all features except outcome
#y contains the target variable (0 or 1)

from sklearn.preprocessing import StandardScaler

scaler= StandardScaler()
x_scaled=scaler.fit_transform(x)
##scales feature to have mean =0 std =1
x_scaled[:3]
#in order to make your data balance while spliting you can 
# use stratify
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x_scaled,y,stratify=y,random_state=10)

x_train.shape
x_test.shape
y_train.value_counts()

201/375

y_test.value_counts()

#train using stand alone model
#train a std tree

from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
# here k fold cross validation is used

scores=cross_val_score(DecisionTreeClassifier(),x,y,cv=5)
scores
score=scores.mean()
print(score)

#accuracy = 0.7188
#train using bagging

from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier 

bag_model=BaggingClassifier(
    estimator=DecisionTreeClassifier(),
    n_estimators=100,
    max_samples=0.8,
    oob_score=True,
    random_state=0
  )
bag_model.fit(x_train,y_train)
print("OOB Score:",bag_model.oob_score_)
bag_model.fit(x_train,y_train)
bag_model.oob_score_ #= 0.753
bag_model.score(x_test,y_test)#0.776
'''
Bagging improves accuracy over a standalone Decision Tree. 
00B score is Like cross-validation, but without needing a
separate test set.

What is OOB (Out-of-Bag) Score?
00B score is a way to evaluate the performance of
ensemble models Like Bagging and Random Forests without
needing a separate validation set or cross-validation.

What Happens in Bagging?
When you use Bagging (Bootstrap Aggregating): For each estimator (e.g., DecisionTree), a random sample 
(with replacement) is drawn from the training data.
Typically, each bootstrap sample contains ~63% of the 
training instances,

The remaining ~**37% of the data is not used to train
that specific tree - these are called Out-of-Bag (OOB) samples.
'''

#0.7534
#note here we are not using test data using
#oob samples results are tested
bag_model.score(x_test,y_test)
#0.776

#how let us apply cross validation
bag_model=BaggingClassifier(
    estimator=DecisionTreeClassifier(),
    n_estimators=100,
    max_samples=0.8,
    oob_score=True,
    random_state=0
  )
scores =cross_val_score(bag_model,x,y,cv=5)
scores 
scores.mean()
#0.757872
#we can see some improvement in test score with bagging classifier as  compared to a standard classifier
#train using random forest

from sklearn.ensemble import RandomForestClassifier

scores = cross_val_score(RandomForestClassifier(n_estimators=50),x,y,cv=5)
scores.mean()
"""
summary
model            accuracy
decision tree    -0.719
bagging (oob)    -0.753
bagging (cv)     -0.758
random forest    -0.763
"""


##################################################################

import pandas as pd

df=pd.read_csv("C:/Assignment/Bagging/Startups (1).csv")
df.head()
df.isnull().sum()
df.describe()
df.Profit.value_counts()
#0 500
#1 286
#there is slight imbalance is our datset but since
#it is not major we will not worry about it!

x= df.drop('Profit',axis='columns')
y=df.Profit

#x contains all features except outcome
#y contains the target variable (0 or 1)

from sklearn.preprocessing import StandardScaler

scaler= StandardScaler()
x_scaled=scaler.fit_transform(x)
##scales feature to have mean =0 std =1
x_scaled[:3]
#in order to make your data balance while spliting you can 
# use stratify
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x_scaled,y,stratify=y,random_state=10)

x_train.shape
x_test.shape
y_train.value_counts()

37/13

y_test.value_counts()

#train using stand alone model
#train a std tree

from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
# here k fold cross validation is used

scores=cross_val_score(DecisionTreeClassifier(),x,y,cv=5)
scores
score=scores.mean()
print(score)

#accuracy = 0.18
#train using bagging

from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier 

bag_model=BaggingClassifier(
    estimator=DecisionTreeClassifier(),
    n_estimators=100,
    max_samples=0.8,
    oob_score=True,
    random_state=0
  )
bag_model.fit(x_train,y_train)
print("OOB Score:",bag_model.oob_score_)
bag_model.fit(x_train,y_train)
bag_model.oob_score_ #= 0.189
bag_model.score(x_test,y_test)#0.153
'''
Bagging improves accuracy over a standalone Decision Tree. 
00B score is Like cross-validation, but without needing a
separate test set.

What is OOB (Out-of-Bag) Score?
00B score is a way to evaluate the performance of
ensemble models Like Bagging and Random Forests without
needing a separate validation set or cross-validation.

What Happens in Bagging?
When you use Bagging (Bootstrap Aggregating): For each estimator (e.g., DecisionTree), a random sample 
(with replacement) is drawn from the training data.
Typically, each bootstrap sample contains ~63% of the 
training instances,

The remaining ~**37% of the data is not used to train
that specific tree - these are called Out-of-Bag (OOB) samples.
'''

#0.7534
#note here we are not using test data using
#oob samples results are tested
bag_model.score(x_test,y_test)
#0.153

#how let us apply cross validation
bag_model=BaggingClassifier(
    estimator=DecisionTreeClassifier(),
    n_estimators=100,
    max_samples=0.8,
    oob_score=True,
    random_state=0
  )
scores =cross_val_score(bag_model,x,y,cv=5)
scores 
scores.mean()
#0.220
#we can see some improvement in test score with bagging classifier as  compared to a standard classifier
#train using random forest

from sklearn.ensemble import RandomForestClassifier

scores = cross_val_score(RandomForestClassifier(n_estimators=50),x,y,cv=5)
scores.mean()
"""
summary
model            accuracy
decision tree    0.18
bagging (oob)    0.189
bagging (cv)     0.220
random forest    0.18
"""




########################################################################

import pandas as pd

df=pd.read_csv("C:/Assignment/Bagging/Cars (1).csv")
df.head()
df.isnull().sum()
df.describe()
df.VOL.value_counts()
#0 500
#1 286
#there is slight imbalance is our datset but since
#it is not major we will not worry about it!

x= df.drop('HP',axis='columns')
y=df.VOL

#x contains all features except outcome
#y contains the target variable (0 or 1)

from sklearn.preprocessing import StandardScaler

scaler= StandardScaler()
x_scaled=scaler.fit_transform(x)
##scales feature to have mean =0 std =1
x_scaled[:3]
#in order to make your data balance while spliting you can 
# use stratify
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x_scaled,y,stratify=y,random_state=10)

x_train.shape
x_test.shape
y_train.value_counts()

201/375

y_test.value_counts()

#train using stand alone model
#train a std tree

from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
# here k fold cross validation is used

scores=cross_val_score(DecisionTreeClassifier(),x,y,cv=5)
scores
score=scores.mean()
print(score)

#accuracy = 0.7188
#train using bagging

from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier 

bag_model=BaggingClassifier(
    estimator=DecisionTreeClassifier(),
    n_estimators=100,
    max_samples=0.8,
    oob_score=True,
    random_state=0
  )
bag_model.fit(x_train,y_train)
print("OOB Score:",bag_model.oob_score_)
bag_model.fit(x_train,y_train)
bag_model.oob_score_ #= 0.753
bag_model.score(x_test,y_test)#0.776
'''
Bagging improves accuracy over a standalone Decision Tree. 
00B score is Like cross-validation, but without needing a
separate test set.

What is OOB (Out-of-Bag) Score?
00B score is a way to evaluate the performance of
ensemble models Like Bagging and Random Forests without
needing a separate validation set or cross-validation.

What Happens in Bagging?
When you use Bagging (Bootstrap Aggregating): For each estimator (e.g., DecisionTree), a random sample 
(with replacement) is drawn from the training data.
Typically, each bootstrap sample contains ~63% of the 
training instances,

The remaining ~**37% of the data is not used to train
that specific tree - these are called Out-of-Bag (OOB) samples.
'''

#0.7534
#note here we are not using test data using
#oob samples results are tested
bag_model.score(x_test,y_test)
#0.776

#how let us apply cross validation
bag_model=BaggingClassifier(
    estimator=DecisionTreeClassifier(),
    n_estimators=100,
    max_samples=0.8,
    oob_score=True,
    random_state=0
  )
scores =cross_val_score(bag_model,x,y,cv=5)
scores 
scores.mean()
#0.757872
#we can see some improvement in test score with bagging classifier as  compared to a standard classifier
#train using random forest

from sklearn.ensemble import RandomForestClassifier

scores = cross_val_score(RandomForestClassifier(n_estimators=50),x,y,cv=5)
scores.mean()
"""
summary
model            accuracy
decision tree    -0.719
bagging (oob)    -0.753
bagging (cv)     -0.758
random forest    -0.763
"""

##############################################################

import pandas as pd

df=pd.read_csv("C:/Bagging technique/diabetes_puma.csv")
df.head()
df.isnull().sum()
df.describe()
df.Outcome.value_counts()
#0 500
#1 286
#there is slight imbalance is our datset but since
#it is not major we will not worry about it!

x= df.drop('Outcome',axis='columns')
y=df.Outcome

#x contains all features except outcome
#y contains the target variable (0 or 1)

from sklearn.preprocessing import StandardScaler

scaler= StandardScaler()
x_scaled=scaler.fit_transform(x)
##scales feature to have mean =0 std =1
x_scaled[:3]
#in order to make your data balance while spliting you can 
# use stratify
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x_scaled,y,stratify=y,random_state=10)

x_train.shape
x_test.shape
y_train.value_counts()

201/375

y_test.value_counts()

#train using stand alone model
#train a std tree

from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
# here k fold cross validation is used

scores=cross_val_score(DecisionTreeClassifier(),x,y,cv=5)
scores
score=scores.mean()
print(score)

#accuracy = 0.7188
#train using bagging

from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier 

bag_model=BaggingClassifier(
    estimator=DecisionTreeClassifier(),
    n_estimators=100,
    max_samples=0.8,
    oob_score=True,
    random_state=0
  )
bag_model.fit(x_train,y_train)
print("OOB Score:",bag_model.oob_score_)
bag_model.fit(x_train,y_train)
bag_model.oob_score_ #= 0.753
bag_model.score(x_test,y_test)#0.776
'''
Bagging improves accuracy over a standalone Decision Tree. 
00B score is Like cross-validation, but without needing a
separate test set.

What is OOB (Out-of-Bag) Score?
00B score is a way to evaluate the performance of
ensemble models Like Bagging and Random Forests without
needing a separate validation set or cross-validation.

What Happens in Bagging?
When you use Bagging (Bootstrap Aggregating): For each estimator (e.g., DecisionTree), a random sample 
(with replacement) is drawn from the training data.
Typically, each bootstrap sample contains ~63% of the 
training instances,

The remaining ~**37% of the data is not used to train
that specific tree - these are called Out-of-Bag (OOB) samples.
'''

#0.7534
#note here we are not using test data using
#oob samples results are tested
bag_model.score(x_test,y_test)
#0.776

#how let us apply cross validation
bag_model=BaggingClassifier(
    estimator=DecisionTreeClassifier(),
    n_estimators=100,
    max_samples=0.8,
    oob_score=True,
    random_state=0
  )
scores =cross_val_score(bag_model,x,y,cv=5)
scores 
scores.mean()
#0.757872
#we can see some improvement in test score with bagging classifier as  compared to a standard classifier
#train using random forest

from sklearn.ensemble import RandomForestClassifier

scores = cross_val_score(RandomForestClassifier(n_estimators=50),x,y,cv=5)
scores.mean()
"""
summary
model            accuracy
decision tree    -0.719
bagging (oob)    -0.753
bagging (cv)     -0.758
random forest    -0.763
"""