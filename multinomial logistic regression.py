# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 15:52:33 2026

@author: shrih
"""

#multinomial logistic Regression on Wine Dataset
#complete End to end script with inline explation
#import required libraries

import pandas as pd
import numpy as np
from sklearn.datasets import load_wine
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import sklearn
print(sklearn._version_)
#Load dataset
wine=load_wine()

x=wine.data

y=wine.target

print("Dataset Shape:", x.shape)
print("Target Classes:", wine.target_names)
#2.Train test split
x_train,x_test,y_train,y_test=train_test_split(
    x,y,
    test_size=0.3,
    random_state=42,
    stratify=y
)
print("Training Samples:", x_train.shape[0])
print("Testing Samples:", x_test.shape[0])
#3.Create and train multinomial logistic regression model
model=LogisticRegression(
    
    solver='lbfgs',
    max_iter=1000
)
model.fit(x_train, y_train)
#4.Make prediction
y_pred=model.predict(x_test)
#pedict class labels (0,1,2)
y_proba=model.predict_proba(x_test)
#predicts probability distribution for each class
#Example output: [0.01, 0.95, 0.04]
print(y_proba) 

#5.Evaluate model performance
print("Classification Report:\n")
print(classification_report(
    y_test,
    y_pred,
    target_names=wine.target_names
))
#shows peicision, recall, f1-score for each class
'''
1 What is "Support"?
support=number of actual samples in each class
class support
class_0 18 samples
class_1 21 samples
class_2 22 samples

So:
Total=18+21+15=54 samples
2 Understanding precision
Meaning:
Out of all predicted as class_x, how many were actually correct?
Example:
For class_0-Precision=0.95
That means:
When model predicted class_0,
95% of those predictions were correct.
so only 5% were wrong predictions

3 Understanding Recall
Recall=true positives/actual positives

Meaning:
Out of all actual class_x samples, how many did the 

4 Understanding F1-Score==2**(Precision+Recall)/(Precision*Recall)
It balances precision and recall.
For class_0:
precision=0.95
recall=1.00
F1=0.97
High F1 means model is both accurate and complete

Now let's Analyze class-wise
class_0
Metric Value meaning
Precisions 0.95 Few false alarms
Recall 1.00 No missed samples
F1 0.97 Excellent 
Support 18 sample size

Interpretation:
Model perfectly captured all class_0 samples and model 
class_1
Metric value
class_2
Metric value
Precision 1.00
Recall 0.93
F1 0.97
Support 15
Important observation:
Precision=1.00
Recall=0.93
Meaning:
When model predicts class_2 - always correct
But it missed some actual class_2 samples
So:
Model is conservative for class_2
It does not falsely label other classes as class_2
But it misses a few true class_2 samples

Overall Accuracy
Accuracy=0.96
Meaning:
Out of 54 test samples:
0.96*54=52
0.96*54=54correctpredictions
only about 2 mistakes total 
Very strong model performance.
This model:
Is not overfitting
Is not biased toward any class
Has balanced precisions & recall
Performs excellent multiclass classification
'''
#6:Manual Class-wise Accuracy Calculation
print("Class-wise Accuracy")

for i, class_name in enumerate(wine.target_names):
    class_indices=(y_test==i)
    #Select all test samples belonging to class i
    correct_predictions=np.sum(y_pred[class_indices]==y_test[class_indices])
    #Count correct predoctions for that class
    total_samples=np.sum(class_indices)
    #Total samples of that class
    class_accuracy = correct_predictions/total_samples
    print(f"(class_name) Accuracy: {class_accuracy:.2f}")