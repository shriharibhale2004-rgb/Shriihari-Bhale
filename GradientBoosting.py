# -*- coding: utf-8 -*-
"""
Created on Mon May 18 16:26:21 2026

@author: HP
"""

import pandas as pd
df=pd.read_csv("C:/13-Decision_Tree/movies_classification.csv")
df.head()
df.columns
df.dtypes
#There are two columns of object type
df=pd.get_dummies(df, columns=["3D_available", "Genre"],drop_first=True)
##########
#Assign input and output
predictors=df.loc[:,df.columns!="Start_Tech_Oscar"]
target=df["Start_Tech_Oscar"]
###################
#train_test_split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test=train_test_split(predictors,
    target,
    test_size=0.2,
    random_state=42)
from sklearn.ensemble import GradientBoostingClassifier
grand_boost=GradientBoostingClassifier()
grand_boost.fit(X_train, y_train)
#
pred1=grand_boost.predict(X_test)
from sklearn.metrics import accuracy_score,confusion_matrix
accuracy_score(y_test,pred1)
confusion_matrix(y_test,pred1)
###############
#Evaluation on training data
pred2=grand_boost.predict(X_train)
accuracy_score(y_test,pred2)
#############
#Let us change the hyperparameter
grand_boost1=GradientBoostingClassifier(learning_rate=0.02,
                                        n_estimators=5000,max_depth=1)
'''
Learning_rate=0.02
Controls how much each tree contributions to the overall predictions.
Lower value-slower learning, but potentially better accuracy
Works well with larger n_estimators
n_estimators=5000
Number of boosting rounds (or trees)
Since Learning_rate is small, more trees are needed to fit the data
'''
grand_boost1.fit(X_train,y_train) 
'''
Trains the GradientBoostingClassifier on the features and target
Each tree is built sequentially to connect
the errors of previous model.
After 5000 trees, you get the final boosted model.
'''
##############
from sklearn.metrics import accuracy_score,confusion_matrix
pred3=grand_boost1.predict(X_test)
acc = accuracy_score(y_test, pred3)
print("Accuracy Score:", acc)
cm = confusion_matrix(y_test, pred3)
print("\nConfusion Matrix:")
print(cm)