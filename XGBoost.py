# -*- coding: utf-8 -*-
"""
Created on Wed May 20 16:07:34 2026

@author: HP
"""

#pip install xgboost
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedKFold, RandomizedSearchCV
from sklearn.metrics import accuracy_score, classification_report,confusion_matrix
import xgboost as xgb
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
path="C:/13-Decision_Tree/movies_classification.csv"
df=pd.read_csv(path)
#Basic check
print("Shape", df.shape)
df.head()
df.columns
df.dtypes
print("Missing values per column:\n", df.isnull().sum())
target_col="Start_Tech_Oscar"
print("Target distribution:\n", df[target_col].value_counts())
#Convert categorical columns
cat_cols=df.select_dtypes(include=['object','category']).columns.tolist()
cols_to_dummy=list(set(cat_cols+[c for c in ['3D_available','Gerne']
                                 if c in df.columns]))
print("Converting to dummies:", cols_to_dummy)
df=pd.get_dummies(df,columns=cols_to_dummy, drop_first=True)
#Prepare X,y And split
X=df.drop(columns=[target_col])
y=df[target_col].astype(int)
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2,
                                                  random_state=0, stratify=y)
#Baseline model
baseline = xgb.XGBClassifier(
    use_label_encoder=False,
    eval_metric='logloss',
    random_state=42
)
#It false
#eval_metric='logloss': most common evaluation metric
#n_jobs=-1:Use all CPU cores
baseline.fit(X_train, y_train)
y_pred_baseline=baseline.predict(X_test)
print("Baseline Accuracy:", accuracy_score(y_test, y_pred_baseline))
print(classification_report(y_test, y_pred_baseline))
print("Confission matrix:\n", confusion_matrix(y_test, y_pred_baseline))
#Randomized search for tuning 
param_dist = {
    'n_estimators': [100, 300, 500, 800, 1200],#no of trees
    'max_depth': [3, 4, 5, 6, 7, 9],
    'learning_rate': [0.01, 0.03, 0.05, 0.08, 0.1],
    'gamma': [0, 0.05, 0.1, 0.2, 0.3],   #min loss reduction required to make a split
    'subsample': [0.6, 0.7, 0.8, 0.9, 1.0],#Fraction of training rows used to build a tree
    'colsample_bytree': [0.6, 0.7, 0.8, 0.9, 1.0],#Fraction of features columns used per tree
    'reg_alpha': [0, 0.001, 0.01, 0.1, 1],#L1 regularization on leaf weights
    'reg_lambda': [0.1, 1, 5, 10] #L2 regularization on leaf weights
}
xgb_clf=xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss',
                          random_state=42, n_jobs=-1)
cv=StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

rs = RandomizedSearchCV(
    estimator=xgb_clf,
    param_distributions=params_dist,
    n_iter=20,
    scoring='f1',
    cv=cv,
    verbose=1,
    random_state=42,
    n_jobs=-1
)
rs.fit(X_train,y_train)
print("Best param:",rs.best_params_)
print("Best CV f1:", rs.best_score_)
best=rs.best_estimator_
y_pred=best.predict(X_test)
print("Tunned Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
print("Confusion matrix:\n", confusion_matrix(y_test, y_pred))
#Feature importances
f1=pd.DataFrame({'feature': X.columns, 'importance':
                 best.feature_importances_}).sort_values('importance', ascending=False)
print(f1.head(20))
plt.figure(figsize=(8,6))
plt.barh(f1['feature'].head(20)[::-1], f1['importance'].head(20)[::-1])
plt.xlabel('Importance')
plt.title('Top 20 feature importances (XGBoost)')
plt.tight_layout()
plt.show()

'''
WHY ACCURACY IS STUCK AT 62%
1. All models are converging to the same accuracy
You already tried:
Logistic Regression
Random Forest
XGBoost (default)
XGBoost (tuned)
GridSearch
Randomized Search
CV scores
All these models giving 60–65% is the strongest possible evidence that:
The features simply do not contain enough information to predict the 
target reliably.
Machine learning cannot create signal where none exists.
2. Your dataset is very small
Only 506 rows
After splitting: ~400 train rows
Many categorical variables → converted to many dummy variables
High dimensionality + small dataset = low generalization ability
Small datasets simply do not support high accuracy unless the problem is trivially
 separable.
3. Your target variable is extremely noisy
From the dataset:
Start_Tech_Oscar is influenced by:
Critics’ ratings
Technical innovation
Production quality, VFX quality
Real Oscar jury decisions 
'''   