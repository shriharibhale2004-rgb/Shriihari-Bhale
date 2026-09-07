# -*- coding: utf-8 -*-
"""
Created on Sat May 23 15:33:46 2026

@author: HP
"""

#
#Divide the diabetes data into train and test datasets and build a Random Forest and Decision Tree model with 
#Outcome as the output variable. 
#
#Business Understanding
#1.Business Problem Statement
#Diabetes data of patient have a diabetes
#Pregnancies,glucose,BP,Skin thickness,insulin,BMI,Age are factors of diabetes prediction

#2.Business Objectives:
#Identify diabetes affected patient
#And control the diabetes of patient 
#
#3.Business Motivation:
#Uderstand demand patterns helps:
#Maintain the glucose and BP 
#Use the shugar free products to eat
#
#4.Constraints
#only numeric data
#presence of outlier
#Highly affected patient by diabetes 
#
#Success Criteria
# Business Success:
#Predict the diabetes of patients and give advice them to control diabetes
#ML Success:
#Good test accuracy
#Interpretable decision rules
#reduced overfitting
########################################
#Data Uderstanding
#
'''
|Feature Name |            |Type
|-------------|------------|-------------
|Pregnancies  |            |Numeric
|Glucose      |            |Numeric
|BloodPressure|            |Numeric
|SkinThickness|            |Numeric 
|Insulin      |            |Numeric
|BMI          |            |Numeric
|Diabetespedigreefunction| |Numeric
|age         |             |Numeric
|outcome     |             |Numeric
'''
#Step 1: Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

sns.set(style="whitegrid")
#
#Load Dataset
df=pd.read_csv("C:/Assignments/Diabetes.csv")
df.head()
df.dtypes
print(df.columns.tolist())
df.columns = df.columns.str.strip()
print(df.columns)
#1 First Moment - Mean
df.mean(numeric_only=True)
'''
Mean represents the average diabetes affected patients.
*Average Pregnant women are less affected by diabetes
*Average Blood Pressure patient highly affected by diabetes
*Average 33 age of people are mostly affected by diabetes
'''
#2 Second Moment-Variance and Standard Deviation
df.var(numeric_only=True)
df.std(numeric_only=True)
'''
Inference:
High variance observed in:
*Plasma glucose concentration    
*Diastolic blood pressure         
*Triceps skin fold thickness
*Hour serum insulin           
Business Meaning:
The diabetes affected patients have above symptonses. 
'''
#3 Third Moment-Skewness
df.skew(numeric_only=True)
'''
Inference:
Right skew indicates:
Highly patients are affected by diabetes due to Hour serum insulin,Diabetes pedigree function,Age.
Tree-based models are suitable for such distribution
'''
#4 Fourth Moment-Kurtosis
df.kurtosis(numeric_only=True)
'''
Inference:
Number of times pregnant 0.159220- Right skew
Plasma glucose concentration 0.640780-Moderately left skewed
Diastolic blood pressure 5.180157-left skewed
Triceps skin fold thickness -0.520072 -Moderately right skewed
Hour serum insulin 7.214260 -right skewed
Body mass index 3.290443 -Similarly distributed skewed
Diabetes pedigree function 5.594954 -right skewed
Age (years) 0.643159-Moderately Right skewed
'''
#Step 5 Histogram (Distribution Analysis)
df.hist(figsize=(14,10), edgecolor='black')
plt.suptitle("Histogram of All Numerical Features")
plt.show()
'''
Inference:
Number of times pregnant is the right skwed there is less chance of diabetes
Plasma glucose concentration is the highly recommended for affect of diabetes    
Diastolic blood pressure is the highly recommended for affect of diabetes    
Triceps skin fold thickness is the less chance of affect of diabetes     
2-Hour serum insulin is the high chance of affect of diabetes         
Body mass index is similarly distributed skewed there is mediam chance of diabetes               
Diabetes pedigree function is the less chance of affect of diabetes      
Age (years) is the moderate chance of affect of diabetes                   
'''
#Step 6 Boxplots (Outlier Detection)
plt.figure(figsize=(14,6))
sns.boxplot(data=df.select_dtypes(include=np.number), orient='h')
plt.title("Boxplot of all numerical features")
plt.show()
'''
Inference:
Number of times pregnant have few outlier there is less chance of diabetes
Plasma glucose concentration have outlier that affect of diabetes    
Diastolic blood pressure have a more outlier there is affect of diabetes    
Triceps skin fold thickness have a one outlier. less chance of affect of diabetes     
2-Hour serum insulin have a more outlier there is affect of diabetes         
Body mass index have a outlier there is mediam chance of diabetes               
Diabetes pedigree function have a outlier there is less chance of affect of diabetes      
Age (years) have a outlier there is moderate chance of affect of diabetes                   
'''
'''
Business Interpretation:
These represent the paitents are affected by diabetes by different symptones.
outlier should be retained.
Tree based models handle them effectively.
'''
#Step 7: Target variable distribution
#Create category (if not already created)
bins = [0, 5, 10]
labels=['Yes','No']
df['Diastolic blood pressure'] = pd.cut(
    df['Diastolic blood pressure'],
    bins=bins,
    labels=labels
)
sns.countplot(x="Class variable", data=df)
plt.title("Class variable Category Distribution")
plt.show()
'''
Inference:

'''
#Step 8: Correlation Heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Feature Correlation Heatmap')
plt.show()
'''

'''
#Step 9: Scatter plot (business relationship)
sns.scatterplot(x='Age (years)', y='Class variable', data=df)
plt.title('Age (years) vs Class variable')
plt.show()
'''
Inference:

'''
#Step 10: PDF & CDF Analysis
for col in df.select_dtypes(include=np.number).columns:
    plt.figure(figsize=(12,4))
    #PDF
    plt.subplot(1,2,1)
    sns.kdeplot(df[col], fill=True)
    plt.title(f'PDF of {col}')
    #CDF
    plt.subplot(1,2,2)
    sorted_vals=np.sort(df[col])
    y=np.arange(len(sorted_vals))/len(sorted_vals)
    plt.plot(sorted_vals, y)
    plt.title(f'CDF of {col}')
    plt.show()
'''
Inference:
PDF shows diabetes patients are affected by different symptons.
CDF helps indentify thresholds, e.g.,
Most of diabetes patients are affected by BP, BMS, age,etc.
'''
#Step 10: Pairplot (Feature Interpretation)
sns.pairplot(df[['Number of times pregnant', 'Plasma glucose concentration',
       'Diastolic blood pressure', 'Triceps skin fold thickness',
       '2-Hour serum insulin', 'Body mass index', 'Diabetes pedigree function',
       'Age (years)']])
plt.show()
'''
Inference:

'''
#Step 11: Fianl EDA Summary
'''
*Dataset is clean and business-realistic

Suitable Models:
Decision Tree
Random Forest
Ensemble Tree Models
'''
################################
#Data Pre-processing
#Company_Data (Sales Analysis)
############################
#Step 1: Import Required Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from feature_engine.outliers import Winsorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
sns.set(style="whitegrid")
from scipy.stats import skew
#It sets a presefined visual theme for all upcoming Seaborn/Matplotlib plot
#Step 2: Load Dataset
df =pd.read_csv("C:/Assignments/Diabetes.csv")
print("Initial Shape",df.shape)
df.head()
df.columns = df.columns.str.strip()
print(df.columns)
'''
Inference:
Dataset contains diabetes patient data with
numeric feature
'''
#Step 3: Data type chech
df.dtypes
'''
Inference:
Moxed data types present
Categorical encoding required.
'''
#Step 4: Missing value check
df.info()
print("\nMissing Values:\n ", df.isnull().sum())
''' 
Inference 
dataset has no missing vallues 
all input feature are numerric
target column Type is integer encoded
'''
#Step 5: Duplicate removal
df.drop_duplicates(inplace=True)
print("After removing duplicates:", df.shape)
'''
Inference:
Ensures no repeated records.
Prevents biased learning
''' 
#Step 6: Target variable creation (Sales Categiry)
bins=[0,5,10,15,20]
labels=['Low','Average','Good','Better']
df['Age (years)'] = pd.cut(
    df['Age (years)'],
    bins=bins,
    labels=labels
)

#Handle missing values in target
#Not required
df['Age (years)'].value_counts()
'''
Inference:
age categories are reasonably balanced.
No severe class imbalance
SMOTE is not required
Why SMOTE is a bad idea here
Your models are Dicision Tree/Random Forest
Tree-based models:
Learn from class boundaries, not distance
'''
#Step 7: Encoding  Categorical Variable
le=LabelEncoder()
df['Number of times pregnant']=le.fit_transform(df['Number of times pregnant'])
df['Plasma glucose concentration']=le.fit_transform(df['Plasma glucose concentration'])
df['Diastolic blood pressure']=le.fit_transform(df['Diastolic blood pressure'])
df['Triceps skin fold thickness']=le.fit_transform(df['Triceps skin fold thickness'])
df['2-Hour serum insulin']=le.fit_transform(df['2-Hour serum insulin'])
df['Body mass index']=le.fit_transform(df['Body mass index'])
df['Diabetes pedigree function']=le.fit_transform(df['Diabetes pedigree function'])
df['Age (years)']=le.fit_transform(df['Age (years)'])
df['Class variable']=le.fit_transform(df['Class variable'])
'''
Why label Encoding?
Tree-based models to do required one-hot encoding
Preserves ordinal nature of Shelve Location
'''
#Step 8: outliers detection
   
plt.figure(figsize=(12,6))
sns.boxplot(data=df.select_dtypes(include=np.number),orient='h')
plt.title("Boxplt Before Outlier Treatment ")
plt.show()
'''
Observation:
Outlier present in:
Skin fold thickness
2 hour serum insulin
BMS
These represent real high-value business cases.
'''
#4: outlier treatment using winsorization
print(df.columns)
winsor = Winsorizer(
    capping_method='iqr',
    tail='both',
    fold=1.5,
    variables=['Triceps skin fold thickness', '2-Hour serum insulin', 'Body mass index']
)

df[['Triceps skin fold thickness', '2-Hour serum insulin', 'Body mass index']] = winsor.fit_transform(
    df[['Triceps skin fold thickness', '2-Hour serum insulin', 'Body mass index']]
)

plt.figure(figsize=(12,6))

sns.boxplot(
    data=df[['Triceps skin fold thickness', '2-Hour serum insulin', 'Body mass index']],
    orient='h'
)

plt.title("Boxplot After Winsorization")
plt.show()
'''
Inference:
Extreme values capped.
Model stability improved.
'''
#Step 10: Skewness Detection 
num_cols=df.select_dtypes(include=np.number).columns
skew_values=df[num_cols].apply(lambda x: skew(x))
skew_values
'''
Inference:
Some feature are skewed
Tree-based models can handle skewness naturally.
'''
#IMPORTANT NOTE: Log Transformation
'''
Do we need Log Transformation?
Case 1: Tree-based models (DT, RF, Bagging)
No
Why?
*Trees split based on order, not distribution 
*Skewness does not affect tree performance
*Winsorization is sufficient (even optional)
Case 2: Linear/Distance-Based Models
YES (Log + Scaling required)
'''
#Step 11: Feature Scaling
'''
Feature scaling is NOT required for:
Decision Tree
Random Forest
Bagging 
Boosting
Reason:
Tree models are scale-invarient.
'''

#Verify distribution
print(df['Diabetes pedigree function'].value_counts())
df=df[df['Diabetes pedigree function'] != 1]
#here 1=better
print(df['Diabetes pedigree function'].value_counts())
          
     
X=df.drop(columns=['Number of times pregnant', 'Age (years)'])
y=df['Age (years)']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
#
#Model 1: Decision Tree (BASELINE)
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix,classification_report

dt=DecisionTreeClassifier(
    criterion='entropy',
    random_state=42
)
#Train the model
dt.fit(X_train, y_train)
#Predictions on training and testing data
y_train_pred=dt.predict(X_train)
y_test_pred=dt.predict(X_test)
#Model Performance
print("Decision Tree Train Accuracy:", accuracy_score(y_train, y_train_pred))
print("Decision Tree Test Accuracy:", accuracy_score(y_test, y_test_pred))
#Confusion Matrix
print("\nConfusion Matrix (Test Data):\n")
print(confusion_matrix(y_test, y_test_pred))
#Classification Report
print("\nClassification Report (Test Data):\n")
print(classification_report(y_test, y_test_pred))
#
#DECISION TREE OPTIMIZATION (OVERFITTING CONTROL
#
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix,classification_report
#Step 1: Define a Regularized Decision Tree
dt_reg=DecisionTreeClassifier(
    criterion='entropy',
    random_state=42
)
#Step 2: Hyperparameter Grid (Controls Complexity)
param_grid={
    'max_depth':[3,5,7,9],
    'min_samples_split':[10,20,30],
    'min_samples_leaf': [5,10,15]
}
'''
Why these parameters?
max_depth-limits tree growth
min_samples_split-avoids aggressive splits
min_samples_leaf-prevents tiny leaf nodes
'''
#Step 3: GridSearchCV (Cross-Validated Optimization)
grid_dt=GridSearchCV(
    estimator=dt_reg,
    param_grid=param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)
grid_dt.fit(X_train, y_train)
#Step 4: Best Model from Grid Search
print("Best Parameters:", grid_dt.best_params_) 
#Step 5: Train optimized  Decision tree
dt_opt=grid_dt.best_estimator_
#Predictions
y_train_pred_opt=dt_opt.predict(X_train)
y_test_pred_opt=dt_opt.predict(X_test)
#Performance
print("Optimized DT Train Accuracy:", accuracy_score(y_train, y_train_pred))
print("Optimized DT Test Accuracy:", accuracy_score(y_test, y_test_pred))
#Confusion Matrix
print("\nConfusion Matrix (Test Data):\n")
print(confusion_matrix(y_test, y_test_pred))
#Classification Report
print("\nClassification Report (Test Data):\n")
print(classification_report(y_test, y_test_pred))
'''
The decision tree has improved (earlier it was near 100% train accuracy)
BUt Decision Trees still have high variance
The dataset is small + noisy + multi-class
DT  alone is not powerful enough to generalize well
This is expected behavior, not a failure
Why This is happening (very important)
Company_data has:
Small sample size
Categorical + numeric mix
Weak linear separability
Sales categorical overlap heavily
Trees struggle when class boundariesvoverlap
2 Decision Trees are HIGH-VARIANCE MODELS
Even with:
max_depth
min_samples_leaf
min_samples_split
A single tree:
Still memorizes local patterns
This is a know limation, not bad tuning
3 Accuracy is a harsh metric here
3-class problem
Random guessing = 33%
55% test accuracy is meaningfully better than chance
But yes - not production-grade yet
What is the correct next step?
You do not fight overfitting further with a single Decision Tree
You change the model class.
'''
from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier(
    n_estimators=300,
    max_depth=6,
    min_samples_leaf=10,
    max_features='sqrt',
    class_weight='balanced',
    random_state=42,
    n_jobs=-1
)
rf.fit(X_train, y_train)
y_train_pred_rf=rf.predict(X_train)
y_test_pred_rf=rf.predict(X_test)
print("Random Forest Train Accuracy:", accuracy_score(y_train, y_train_pred_rf))
print("Random Forest Test Accuracy:", accuracy_score(y_test, y_test_pred_rf))
'''
This is exactly the right moment to pause and 
interpret, not panic.
What you're seeing now is Not a tuning failure
-it's a data-limited ceiling.
'''
'''
Key Insights:

Business Benefits:

ML Benefits:
'''
####################################################################
#Random Forest
import pandas as pd
df=pd.read_csv("C:/Assignments/Diabetes.csv")
df.head
df.head()
df.columns = df.columns.str.strip()
print(df.columns)
X = df.drop("Class variable", axis=1)   # replace target_column
y = df["Class variable"]
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    #stratify=y
)
from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier()
model.fit(X_train, y_train)
model.score(X_test, y_test)
#let us change the parameter 
model=RandomForestClassifier(n_estimators=40)
model.fit(X_train, y_train)
model.score(X_test,y_test)
####################################
# Step 1: Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Step 2: Load dataset
df = pd.read_csv("C:/Assignments/Diabetes.csv")
df.columns = df.columns.str.strip()
print(df.columns)
df.dtypes
# Step 3: Define features and target
X = df.drop("Class variable", axis=1)   # replace target_column
y = df["Class variable"]

# Step 4: Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 5: Create Random Forest model
rf_model = RandomForestClassifier(
    n_estimators=100,
    criterion='gini',
    max_depth=5,
    random_state=42
)

# Step 6: Train model
rf_model.fit(X_train, y_train)

# Step 7: Prediction
y_pred = rf_model.predict(X_test)

# Step 8: Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

######################################################
#
#Divide the diabetes data into train and test datasets and build a Random Forest and Decision Tree model with 
#Outcome as the output variable. 
#
#Business Understanding
#1.Business Problem Statement
#Diabetes data of patient have a diabetes
#Pregnancies,glucose,BP,Skin thickness,insulin,BMI,Age are factors of diabetes prediction

#2.Business Objectives:
#Identify diabetes affected patient
#And control the diabetes of patient 
#
#3.Business Motivation:
#Uderstand demand patterns helps:
#Maintain the glucose and BP 
#Use the shugar free products to eat
#
#4.Constraints
#only numeric data
#presence of outlier
#Highly affected patient by diabetes 
#
#Success Criteria
# Business Success:
#Predict the diabetes of patients and give advice them to control diabetes
#ML Success:
#Good test accuracy
#Interpretable decision rules
#reduced overfitting
########################################
#Data Uderstanding
#
'''
|Feature Name |            |Type
|-------------|------------|-------------
|Pregnancies  |            |Numeric
|Glucose      |            |Numeric
|BloodPressure|            |Numeric
|SkinThickness|            |Numeric 
|Insulin      |            |Numeric
|BMI          |            |Numeric
|Diabetespedigreefunction| |Numeric
|age         |             |Numeric
|outcome     |             |Numeric
'''
#Step 1: Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

sns.set(style="whitegrid")
#
#Load Dataset
df=pd.read_csv("C:/Assignments/Fraud_check.csv")
df.head()
df.dtypes
print(df.columns.tolist())
df.columns = df.columns.str.strip()
print(df.columns)
#1 First Moment - Mean
df.mean(numeric_only=True)
'''
Mean represents the average diabetes affected patients.
*Average Pregnant women are less affected by diabetes
*Average Blood Pressure patient highly affected by diabetes
*Average 33 age of people are mostly affected by diabetes
'''
#2 Second Moment-Variance and Standard Deviation
df.var(numeric_only=True)
df.std(numeric_only=True)
'''
Inference:
High variance observed in:
*Plasma glucose concentration    
*Diastolic blood pressure         
*Triceps skin fold thickness
*Hour serum insulin           
Business Meaning:
The diabetes affected patients have above symptonses. 
'''
#3 Third Moment-Skewness
df.skew(numeric_only=True)
'''
Inference:
Right skew indicates:
Highly patients are affected by diabetes due to Hour serum insulin,Diabetes pedigree function,Age.
Tree-based models are suitable for such distribution
'''
#4 Fourth Moment-Kurtosis
df.kurtosis(numeric_only=True)
'''
Inference:
Number of times pregnant 0.159220- Right skew
Plasma glucose concentration 0.640780-Moderately left skewed
Diastolic blood pressure 5.180157-left skewed
Triceps skin fold thickness -0.520072 -Moderately right skewed
Hour serum insulin 7.214260 -right skewed
Body mass index 3.290443 -Similarly distributed skewed
Diabetes pedigree function 5.594954 -right skewed
Age (years) 0.643159-Moderately Right skewed
'''
#Step 5 Histogram (Distribution Analysis)
df.hist(figsize=(14,10), edgecolor='black')
plt.suptitle("Histogram of All Numerical Features")
plt.show()
'''
Inference:
Number of times pregnant is the right skwed there is less chance of diabetes
Plasma glucose concentration is the highly recommended for affect of diabetes    
Diastolic blood pressure is the highly recommended for affect of diabetes    
Triceps skin fold thickness is the less chance of affect of diabetes     
2-Hour serum insulin is the high chance of affect of diabetes         
Body mass index is similarly distributed skewed there is mediam chance of diabetes               
Diabetes pedigree function is the less chance of affect of diabetes      
Age (years) is the moderate chance of affect of diabetes                   
'''
#Step 6 Boxplots (Outlier Detection)
plt.figure(figsize=(14,6))
sns.boxplot(data=df.select_dtypes(include=np.number), orient='h')
plt.title("Boxplot of all numerical features")
plt.show()
'''
Inference:
Number of times pregnant have few outlier there is less chance of diabetes
Plasma glucose concentration have outlier that affect of diabetes    
Diastolic blood pressure have a more outlier there is affect of diabetes    
Triceps skin fold thickness have a one outlier. less chance of affect of diabetes     
2-Hour serum insulin have a more outlier there is affect of diabetes         
Body mass index have a outlier there is mediam chance of diabetes               
Diabetes pedigree function have a outlier there is less chance of affect of diabetes      
Age (years) have a outlier there is moderate chance of affect of diabetes                   
'''
'''
Business Interpretation:
These represent the paitents are affected by diabetes by different symptones.
outlier should be retained.
Tree based models handle them effectively.
'''
#Step 7: Target variable distribution
#Create category (if not already created)
bins = [0, 5, 10]
labels=['Yes','No']
df['City.Population'] = pd.cut(
    df['City.Population'],
    bins=bins,
    labels=labels
)
sns.countplot(x="Urban", data=df)
plt.title("Urban Category Distribution")
plt.show()
'''
Inference:

'''
#Step 8: Correlation Heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Feature Correlation Heatmap')
plt.show()
'''

'''
#Step 9: Scatter plot (business relationship)
sns.scatterplot(x='Taxable.Income', y='City.Population', data=df)
plt.title('Taxable.Income vs City.Population')
plt.show()
'''
Inference:

'''
#Step 10: PDF & CDF Analysis
for col in df.select_dtypes(include=np.number).columns:
    plt.figure(figsize=(12,4))
    #PDF
    plt.subplot(1,2,1)
    sns.kdeplot(df[col], fill=True)
    plt.title(f'PDF of {col}')
    #CDF
    plt.subplot(1,2,2)
    sorted_vals=np.sort(df[col])
    y=np.arange(len(sorted_vals))/len(sorted_vals)
    plt.plot(sorted_vals, y)
    plt.title(f'CDF of {col}')
    plt.show()
'''
Inference:
PDF shows diabetes patients are affected by different symptons.
CDF helps indentify thresholds, e.g.,
Most of diabetes patients are affected by BP, BMS, age,etc.
'''
#Step 10: Pairplot (Feature Interpretation)
sns.pairplot(df[['Undergrad', 
                 'Marital.Status', 
                 'Taxable.Income', 
                 'City.Population',
                 'Work.Experience', 
                 'Urban']])
plt.show()
'''
Inference:

'''
#Step 11: Fianl EDA Summary
'''
*Dataset is clean and business-realistic

Suitable Models:
Decision Tree
Random Forest
Ensemble Tree Models
'''
################################
#Data Pre-processing
#Company_Data (Sales Analysis)
############################
#Step 1: Import Required Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from feature_engine.outliers import Winsorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
sns.set(style="whitegrid")
from scipy.stats import skew
#It sets a presefined visual theme for all upcoming Seaborn/Matplotlib plot
#Step 2: Load Dataset
df=pd.read_csv("C:/Assignments/Fraud_check.csv")
print("Initial Shape",df.shape)
df.head()
df.columns = df.columns.str.strip()
print(df.columns)
'''
Inference:
Dataset contains diabetes patient data with
numeric feature
'''
#Step 3: Data type chech
df.dtypes
'''
Inference:
Moxed data types present
Categorical encoding required.
'''
#Step 4: Missing value check
df.info()
print("\nMissing Values:\n ", df.isnull().sum())
''' 
Inference 
dataset has no missing vallues 
all input feature are numerric
target column Type is integer encoded
'''
#Step 5: Duplicate removal
df.drop_duplicates(inplace=True)
print("After removing duplicates:", df.shape)
'''
Inference:
Ensures no repeated records.
Prevents biased learning
''' 
#Step 6: Target variable creation (Sales Categiry)
bins=[0,5,10,15,20]
labels=['Low','Average','Good','Better']
df['Work.Experience'] = pd.cut(
    df['Work.Experience'],
    bins=bins,
    labels=labels
)

#Handle missing values in target
#Not required
df['Work.Experience'].value_counts()
'''
Inference:
age categories are reasonably balanced.
No severe class imbalance
SMOTE is not required
Why SMOTE is a bad idea here
Your models are Dicision Tree/Random Forest
Tree-based models:
Learn from class boundaries, not distance
'''
#Step 7: Encoding  Categorical Variable
le=LabelEncoder()
df['Undergrad']=le.fit_transform(df['Undergrad'])
df['Marital.Status']=le.fit_transform(df['Marital.Status'])
df['Taxable.Income']=le.fit_transform(df['Taxable.Income'])
df['City.Population']=le.fit_transform(df['Triceps skin fold thickness'])
df['2-Hour serum insulin']=le.fit_transform(df['City.Population'])
df['Work.Experience']=le.fit_transform(df['Work.Experience'])
df['Urban']=le.fit_transform(df['Urban'])
'''
Why label Encoding?
Tree-based models to do required one-hot encoding
Preserves ordinal nature of Shelve Location
'''
#Step 8: outliers detection
   
plt.figure(figsize=(12,6))
sns.boxplot(data=df.select_dtypes(include=np.number),orient='h')
plt.title("Boxplt Before Outlier Treatment ")
plt.show()
'''
Observation:
There is no outlier    
'''
'''
NO need of outlier treatment
#4: outlier treatment using winsorization
print(df.columns)
winsor = Winsorizer(
    capping_method='iqr',
    tail='both',
    fold=1.5,
    variables=['Triceps skin fold thickness', '2-Hour serum insulin', 'Body mass index']
)

df[['Triceps skin fold thickness', '2-Hour serum insulin', 'Body mass index']] = winsor.fit_transform(
    df[['Triceps skin fold thickness', '2-Hour serum insulin', 'Body mass index']]
)

plt.figure(figsize=(12,6))

sns.boxplot(
    data=df[['Taxable.Income', 'City.Population',
           'Work.Experience']],
    orient='h'
)

plt.title("Boxplot After Winsorization")
plt.show()
'''
'''
Inference:
Extreme values capped.
Model stability improved.
'''
#Step 10: Skewness Detection 
num_cols=df.select_dtypes(include=np.number).columns
skew_values=df[num_cols].apply(lambda x: skew(x))
skew_values
'''
Inference:
Some feature are skewed
Tree-based models can handle skewness naturally.
'''
#IMPORTANT NOTE: Log Transformation
'''
Do we need Log Transformation?
Case 1: Tree-based models (DT, RF, Bagging)
No
Why?
*Trees split based on order, not distribution 
*Skewness does not affect tree performance
*Winsorization is sufficient (even optional)
Case 2: Linear/Distance-Based Models
YES (Log + Scaling required)
'''
#Step 11: Feature Scaling
'''
Feature scaling is NOT required for:
Decision Tree
Random Forest
Bagging 
Boosting
Reason:
Tree models are scale-invarient.
'''

#Verify distribution
print(df['City.Population'].value_counts())
df=df[df['City.Population'] != 1]
#here 1=better
print(df['City.Population'].value_counts())
          
     
X=df.drop(columns=['City.Population', 'Work.Experience'])
y=df['Work.Experience']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
#
#Model 1: Decision Tree (BASELINE)
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix,classification_report

dt=DecisionTreeClassifier(
    criterion='entropy',
    random_state=42
)
#Train the model
dt.fit(X_train, y_train)
#Predictions on training and testing data
y_train_pred=dt.predict(X_train)
y_test_pred=dt.predict(X_test)
#Model Performance
print("Decision Tree Train Accuracy:", accuracy_score(y_train, y_train_pred))
print("Decision Tree Test Accuracy:", accuracy_score(y_test, y_test_pred))
#Confusion Matrix
print("\nConfusion Matrix (Test Data):\n")
print(confusion_matrix(y_test, y_test_pred))
#Classification Report
print("\nClassification Report (Test Data):\n")
print(classification_report(y_test, y_test_pred))
#
#DECISION TREE OPTIMIZATION (OVERFITTING CONTROL
#
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix,classification_report
#Step 1: Define a Regularized Decision Tree
dt_reg=DecisionTreeClassifier(
    criterion='entropy',
    random_state=42
)
#Step 2: Hyperparameter Grid (Controls Complexity)
param_grid={
    'max_depth':[3,5,7,9],
    'min_samples_split':[10,20,30],
    'min_samples_leaf': [5,10,15]
}
'''
Why these parameters?
max_depth-limits tree growth
min_samples_split-avoids aggressive splits
min_samples_leaf-prevents tiny leaf nodes
'''
#Step 3: GridSearchCV (Cross-Validated Optimization)
grid_dt=GridSearchCV(
    estimator=dt_reg,
    param_grid=param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)
grid_dt.fit(X_train, y_train)
#Step 4: Best Model from Grid Search
print("Best Parameters:", grid_dt.best_params_) 
#Step 5: Train optimized  Decision tree
dt_opt=grid_dt.best_estimator_
#Predictions
y_train_pred_opt=dt_opt.predict(X_train)
y_test_pred_opt=dt_opt.predict(X_test)
#Performance
print("Optimized DT Train Accuracy:", accuracy_score(y_train, y_train_pred))
print("Optimized DT Test Accuracy:", accuracy_score(y_test, y_test_pred))
#Confusion Matrix
print("\nConfusion Matrix (Test Data):\n")
print(confusion_matrix(y_test, y_test_pred))
#Classification Report
print("\nClassification Report (Test Data):\n")
print(classification_report(y_test, y_test_pred))
'''
The decision tree has improved (earlier it was near 100% train accuracy)
BUt Decision Trees still have high variance
The dataset is small + noisy + multi-class
DT  alone is not powerful enough to generalize well
This is expected behavior, not a failure
Why This is happening (very important)
Company_data has:
Small sample size
Categorical + numeric mix
Weak linear separability
Sales categorical overlap heavily
Trees struggle when class boundariesvoverlap
2 Decision Trees are HIGH-VARIANCE MODELS
Even with:
max_depth
min_samples_leaf
min_samples_split
A single tree:
Still memorizes local patterns
This is a know limation, not bad tuning
3 Accuracy is a harsh metric here
3-class problem
Random guessing = 33%
55% test accuracy is meaningfully better than chance
But yes - not production-grade yet
What is the correct next step?
You do not fight overfitting further with a single Decision Tree
You change the model class.
'''
from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier(
    n_estimators=300,
    max_depth=6,
    min_samples_leaf=10,
    max_features='sqrt',
    class_weight='balanced',
    random_state=42,
    n_jobs=-1
)
rf.fit(X_train, y_train)
y_train = le.fit_transform(y_train)
y_test = le.transform(y_test)
print(X_train.dtypes)
rf.fit(X_train, y_train)
y_train_pred_rf=rf.predict(X_train)
y_test_pred_rf=rf.predict(X_test)
print("Random Forest Train Accuracy:", accuracy_score(y_train, y_train_pred_rf))
print("Random Forest Test Accuracy:", accuracy_score(y_test, y_test_pred_rf))
'''
This is exactly the right moment to pause and 
interpret, not panic.
What you're seeing now is Not a tuning failure
-it's a data-limited ceiling.
'''
'''
Key Insights:

Business Benefits:

ML Benefits:
'''
####################################################################
#Random Forest
import pandas as pd
df=pd.read_csv("C:/Assignments/Fraud_check.csv")
df.head
df.head()
df.columns = df.columns.str.strip()
print(df.columns)
df.dtypes
X = df.drop('Urban', axis=1)   # replace target_column
y = df['Urban']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    #stratify=y
)
from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier()
model.fit(X_train, y_train)
model.score(X_test, y_test)
#let us change the parameter 
model=RandomForestClassifier(n_estimators=40)
model.fit(X_train, y_train)
model.score(X_test,y_test)
####################################