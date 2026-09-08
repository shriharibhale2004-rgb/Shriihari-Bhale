# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 16:36:28 2026

@author: shrih
"""
'''
1 business problem statement:
organization handling large volumes of handwritten documents
(eg postal services,bank,educational institutions,government offices)
need to automaticaly recogenize handwritten english alphabets
manual processing of handwritten forms is:
time-consuming
error-prone
Expensive
operationally inefficient
automating letter recognition improves efficiency and accuracy
in document processing




2 Motivation:
Understanding handwritten letter patternshelps
automate postal code reading 
digitize 

'''


# data preprocessing





#EDA
#required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler


#step 2 Load dataset
letter =pd.read_csv("C:/Linear Regression/letterdata.csv")
print("Shape of Dataset:",letter.shape)
print(letter.head())


#step 3 basic information
print("\nData Types:\n",letter.dtypes)
print("\nSummary Statistics:\n",letter.describe())
print("\nMissing values",letter.isnull().sum())


#step 4 Target variable analysis

print("\nClass Distribution:\n",letter['letter'].value_counts())

plt.figure(figsize=(10,4))
sns.countplot(x='letter',data=letter)
plt.xticks(rotation=90)
plt.title('Class Distribution')
plt.show() 

'''
Inference
Clases are evenly distributed
No major class imbalance
SVM can perform well without class weighting
'''

#step 5 Business moment decisions

#first moment
print("\nMean:\n",letter.mean(numeric_only=True))   
#second moment
print("\nVariance:\n",letter.var(numeric_only=True))   
#third moment
print("\nSkewness:\n",letter.skew(numeric_only=True))   
#fourth Kartosis
print("\nKurtosis:\n",letter.kurtosis(numeric_only=True))  

'''
feature have different scales
Variance differs significantly across variables
scale is mandatory before apply
'''
#step6 Histogram Distribution

letter.hist(figsize=(14,10))
plt.suptitle("Histogram of Numerical feature")
plt.show() 

'''
Histogram inference - letter dataset

'''

#step7 outlier detection

plt.figure(figsize=(12,6))
sns.boxplot(data=letter.drop(column=['letter']))
plt.xticks(rotation=90)
plt.title('boxplot for outlier detection')
plt.show()


#step 8 correlation analysis
plt.figure(figsize=(10,8))
sns.heatmap(letter.drop(columns=['letter']).corr(),cmap='coolwarm')
plt.title('correlation matrix')
plt.show

'''
correlation heatmap inference - letter dataset (svm)

SVM oriented conclusion 
1 

final insights:
the dataset shows meaningful geomatric and pixel based relationship
structure suggests that nonliear boundries (RBF kernek) will likely
perform better than purely linear seperation
    
'''
#step 9 PAIRWISE CLASS SEPARABILITY (SAMPLE)
#=============================================

sample_data = letter.sample(500, random_state=42)
sns.pairplot(sample_data, hue='Letter',vars=letter.columns[1:5])
plt.show()




#step 10 feature scaling check (mandatory for svm)
X=letter.drop(columns=['letter'])

scaler =StandardScaler()
X_scaled=scaler.fit_transform(X)
print('\nMean after scaling\n:',np.round(np.mean(X_scaled,axis=0), 4))
print('\nStd after scaling:\n',np.round(np.std(X_scaled,axis=0), 4))




#Data Preprocessing for letter classification
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.feature_selection import VarianceThreshold
from sklearn.model_selection import train_test_split

#step 1 Load dataset

df=pd.read_csv("C:/Linear Regression/letterdata.csv")
print("initial Shape:",df.shape)
print(df.head())

#step 2 DAta Types Check

df.info()

'''
inference 
all feature are numerical
target variable letter is categorical (A-Z)
this is a multiclass problem
'''
#step 3 missing value check
print("missing value",df.isnull().sum())

'''
inference

'''

#step 4 duplicate removal

print("\nShape after duplicate removal:",df.shape)

'''
Removes redundent samples
improves generalization of svm

'''

#step 5 separable featuere and target

X=df.drop(coluns=['letter'])
y=df['letter']

#step 6 encode target variable

le=LabelEncoder()
y_encoded=le.fit_transform(y)

'''
inference
converts
'''

#step 7 Zero variance feature removal
selector = VarianceThreshold(threshold=0.0)
X_var = selector.fit_transform(X)

print('Shape after variance filtering:',X_var.shape)

#step 8 zero variance feature removal
scaler=StandardScaler()
X_scaled= scaler.fit_transform(X_var)

#step 9 train test split

X_train,X_test,y_train,y_test=train_test_split(
    X_scaled,
    y_encoded,
    test_size=0.2,
    random_state=42,
    stratfy=y_encoded
   )
print('Training Shape :',X_train.shape)
print('Testing shape :',X_test.shape)


#SVM model building & Hyperparameter tuning

#required libraries
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import GridSearchCV

#Helpern function for training and testing

def evaluate_svc(**kwargs):

    """Train SVC with given parameters and return test accuracy""" 
    model = SVC(**kwargs)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"Params: {kwargs} --> Accuracy:{acc:.4f}")
    return acc

#1 Effect of Kernel
print('\n---Kernel Comparison---')
for k in ['linear','poly','rbf','sigmoid']:
    evaluate_svc(kernel=k)

'''
Kernel Interpretation:

Linear:

* Works if data is Linearly separable.

* Moderate performance expected.

Accuracy: 0.8390

rbf:

* Handles nonLinear boundaries.

* Usually best for Letter dataset.

Accuracy: 0.9371

poLy:

* Captures polynomial relationships, 
• Risk of overfitting at higher degree,

Accuracy: 0.8835
'''

#2 Effect of regularization parameter c

print('\n---c parameter (Regularization)---')
for c in [0.1,1,10,100]:
    evaluate_svc(kernel='rbf',C=c)
   
'''
C Interpretation:

Low C (0.1):

Wider morgin

Higher bias

* May underfit

Accuracy: 0,8302

Moderate C (1-10):

* Balanced model

* Usually best performance for c=1 Accuracy: 0,9371 for c-10, Accuracy: 0,9679

High C (100):

Narrow margin

* Risk of overfitting
Accuracy: 0.9681
'''    
    
#3 Effect of Gamma (RBF Kernel) 

print('\n---Gamma Parameter---')
for g in [0.01 ,0.1,1,10]:
    evaluate_svc(kernel="rbf",gamma=g)
    
    
    


#4 effect of degree  (polynomial kernel) 
print('\n---Polynomial Degree---')
for d in [2 ,3,4,5]:
    evaluate_svc(kernel="poly",degree=d)
    
    
#5 Effect of coef0 (polynomial kernel)    
print('\n---coef0 Parameter---')
for c0 in [0.0 ,0.5,1,2]:
    evaluate_svc(kernel="rbf",degerr=3, coef0=c0)
    
    
    
    
# 6. AUTOMATIC HYPERPARAMETER TUNING (GridSearchCV)

print("\n--- Grid Search for Best Parameters (RBF) ---")

param_grid = {
    "kernel": ["rbf"],
    "C": [0.1, 1, 10, 100],
    "gamma": [0.01, 0.1, 1]
}

grid = GridSearchCV(
    SVC(),
    param_grid,
    cv=3,
    scoring="accuracy",
    n_jobs=-1
)    

grid.fit(X_train, y_train)

print("Best Parameters:", grid.best_params )
print ("Best Cross-Validation Accuracy:", grid.best_score_)


'''
Best Parameters:{'C': 10,'gamma': 0.1, 'kernel': 'rbf'}
Best Cross-Validation Accuracy: 0.9657158162582027
'''

# Evaluate Best Model on Test Data


best_model = grid.best_estimator_
test_preds = best_model.predict(X_test)

print("\nFinal Test Accuracy:", 
      accuracy_score(y_test, test_preds))

print("\nCLassification Report:\n", 
      classification_report(y_test, test_preds))



'''
BUSINESS IMPACT - LETTER RECOGNITION USING SVM

1 Operational Efficiency Improvement

Automates handwritten character recognition.
Reduces manual data entry effort.
Minimizes human error in document processing.
Speeds up digitization of physical records.

2 Cost Reduction

Reduces labor cost for manual transcription,
Decreases error correction expenses,
Minimizes reprocessing time in banking, postal, and administrative sectors
Scales efficiently without increasing workforce,

3 Accuracy & Reliability

High classification accuracy (95%) improves system trust,
Consistent perfonmance across large datasets,
Reduced misclassification improves downstream decision

Example:
Bank chegue processing
Postal code reading
Form scanning systems

4 Scalability & Automation

Can process millions of records quickly.
Supports large-scale document digitization projects.
Enables integration with OCR pipelines.

5 Competitive Advantage

Organizations using automated recognition:
Deliver faster customer service
Improve turnaround time
Enhance digital transformation initiatives
Gain technological edge over competitors

6 Risk Reduction

Lower probability ility of transcription errors
Reduces compliance risks in regulated industries 
Improves audit traceability




  '''   
        

    
 