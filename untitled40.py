# -*- coding: utf-8 -*-
"""
Created on Tue May 12 16:56:38 2026

@author: shrih
"""

from sklearn.datasets import load_iris
iris =load_iris()
import pandas as pd
df=pd.DataFrame(iris.data,columns=iris.feature_names)
df.head()
df['target']=iris.target
df.head()
from sklearn.model_selection import train_test_split
X_train, X_test, y_train,y_test=train_test_split(df.drop(['target'],axis='columns'),iris.target,test_size=0.2)
from sklearn.ensemble import RandomForestClassifier

model=RandomForestClassifier()
model.fit(X_train,y_train)

model.score(X_test,y_test)
#let us change the parameters
model=RandomForestClassifier(n_estimators=40)
model.fit(X_train,y_train)
model.score(X_test,y_test)
