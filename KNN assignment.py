# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 11:37:39 2026

@author: shrih
"""
#Dataset 1
# BUSINESS UNDERSTANDING

# 1. Business Problem Statement:
# Glass production involves different chemical compositions.
# Manually classifying glass types based on composition
# is time-consuming and inconsistent.
# 2. Simplified Context of the Problem:
# Different glass types are produced using varying proportions
# of elements such as Na, Mg, Al, Si, Ca, etc.
# These compositions determine the glass type.

# 3. Problem Identification:
# - Manual classification is inefficient
# - Chemical composition varies continuously
# - Misclassification leads to quality and compliance issues

# 4. Business Objective:
# Maximize: Accuracy of glass type classification
# Minimize: Manual intervention and classification errors
# Enable: Automated, data-driven decision-making

# 5. Stakeholder Expectations:
# - Manufacturing team: consistent quality
# - Compliance team: reduced hazardous substances
# - Management: reduced cost and emissions

# 6. Constraints & Limitations:
# - Climate change regulations
# -Energy consumption constraints
#-Presence of outliers in chemical composition data

# 7. Feasibility Check:
# -Historical labeled data is available tyFl dty
# -KNN is suitable for multivariate numeric data

# 8. Success Criteria:
# Business Success Criteria:
# - Correct glass type identification
#-  Reduced manual effort

# ML Success Criteria:     
# - Improved classification accuracy
# - Stable performance on unseen data
#############################################################
# DATA UNDERSTANDING

'''
Feature    | Description          |Type

RI   |Refractive index           Quantitative, Continuous

Na   |Sodium content             Quantitative, Continuous

Mg   |Magnesium content          Quantitative, Continuous

AL   |Aluminum content           Quantitative, Continuous

Si   |Silicon content            Quantitative, Continuous

K    |Potassium content          Quantitative, Continuous

Ca   |Calcium content            Quantitative, Continuous

Ba   |Barium content             Quantitative, Continuous

Fe   | Iron content              Quantitative, Continuous

type  |Glass category            Categorical target variable

'''
#step 1 Report required
import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#step2 load dataset
glass= pd.read_csv("C:/KNN/glass.csv")
#step 3 basic data understanding
glass.dtypes
glass.shape
glass.columns
glass.describe()


#all input feature are numeric
#target column type is categorical encoded as integers

#EDA (exploratory data analysis)

#rename columns for consitancy 
glass.columns=['ri','na','mg','al','si','k','ca','ba','fe','type']

#check data types
glass.dtypes
#inference:'
#all input feature are numeric (float)
#target column type is integer (categorical encoded).

#shape and size

print("Shape of dataset:" ,glass.shape)
print("Shape of dataset:" ,glass.size)

#summary stat
glass.describe()
'''
ELement Meaning

Min / Max | Range of chemical composition | Helps define safe and usabi Mean | Average concentration | Typical composition used in production 01-03 | Middle 50% spread | Indicates consistency in raw material mix Median | Central tendency | Robust benchmark against extreme batches | | IQR | Q3 - Q1 | Detects stability 
of production process
'''
#first moment : mean (central tendancy)
mean_values= glass.mean(numeric_only=True)
print("\nMean (first moment):\n",mean_values)

#inference 
#mean shows the typical chemical compsition

#2 variance and std 
var_values =glass.var(numeric_only=True)
std_values =glass.std(numeric_only=True)

print("\nvariance (second momemnt):\n",var_values)
print("\nstandard deviation (second momemnt):\n",std_values)


#3 third moment :skewness 
skew_values =glass.skew(numeric_only=True)
print("\nSkewness (Third moment):\n",skew_values)    

#inference:
#positive skew -> few samples with high concentration 
#negative skew -> few smaples with very low concentration
#indicates non nomial chemical distributions

#4 moment : Kurtosis(peakedness)
kurt_values = glass.kurtosis(numeric_only=True)
print("\nKurtosis (4 mpmemt):\n", kurt_values)

#inference;
#platkurtic (<0): flater distribution uniform composition 
#leptokurtosis (>0): sharp peak extreme composition present

#univartate analysis histogram    
glass.drop(columns=['type']).hist(
    figsize=(12,10),
    edgecolor='black'
    )
plt.suptitle("Histograms of glass Cgemical feature")
plt.tight_layout()
plt.show()

#inference
#ri and na are near normaly distributed 
#mg and k shoew skewness 
#si has tight concentratoon renage

#BOXPLOT outlier detection

plt.figure(figsize=(12,6))
sns.boxplot(data=glass.drop(columns=['type']),orient='h')
plt.title("Boxplt of chemical feature ")
plt.show()

#inference:
#outliers observed in na al ca ba and k
#these may represent special purpose or  industrial glass types    

#joint plot
sns.jointplot(data=glass, x="K", y="Ri", kind="scatter")
plt.suptitle("Joint Plot: K vs Ri", y=1.02)
plt.show()

#pair plot
sns.pairplot(glass.drop(columns='type'), hue="species")
plt.suptitle("Pair Plot of All Features", y=1.02)
plt.show()


#hetmap 
plt.figure(figsize=(10,8))
sns.heatmap(
    glass.drop(columns=['type']).corr(),
    annot=True,
    cmap='coolwarm'
    )
plt.title("Correlation Heatmap - Glass Dataset")
plt.show()

'''
RI (Refractive Index): Strongly increases with Ca and decreases
with Si, indicating calcium-rich glass has higher refractive index. Na (Sodium): Shows weak to moderate correlations, slightly positive with Ba and negative with Mg and Ca.
Ma (Magnesium): Negatively correlated with Al, Ca, and Ba,
suggesting magnesium content reduces these components.
AL (ALuminium): Moderately positively related to Ba and K,
but negatively related to Mg and RI.
Si (Silicon): Strongly negatively correlated with RI, implying silica-rich glass Lowers refractive index.
K (Potassium): Mild positive correlation with Al and weak
negative correlation with Ca, showing Limited influence overall.
Ca (Calcium): Strongly positively correlated with RI and
negatively with Ma and K, highlighting its key role in glass properties.
Ba (Barium): Moderately positively correlated with Al and Na,
but negatively with Mg.
Fe (Iron): Very weak correlations with all features,
indicating minimal interaction with other elements.
'''
#pdf cdf
num_cols=glass.select_dtypes(include=np.number).columns.drop(['type'])

for col in num_cols:
    plt.figure(figsize=(12,5))
    
    
    #pdf
    plt.subplot(1,2,1)
    sns.kdeplot(glass[col],fill=True)
    plt.title(f"PDF Of {col}")
    
    
    #CDF
    plt.subplot(1,2,2)
    sorted_vals=np.sort(glass[col])
    y_vals=np.arange(len(sorted_vals)) / float(len(sorted_vals))
    plt.plot(sorted_vals,y_vals,marker='.',linestyle='name')
    plt.title(f"CDF of {col}")
    
    plt.tight_layout()
    plt.show()
    
#Inference
'''
'''
#pdf-shows distribution shape of each chemical
#Cdf- helps decide percentile based threshold
#useful for quality control and segmentation

#class distribution (target analusis)

sns.countplot(x=glass['type'])
plt.title("Distribution of Glass Types")
plt.show()

#inference
#the dataset is imabalanced with glass types 1 and 2 having the 
#highest number of samples while types 3,5 and 6 are 

# FINAL EDA INSIGHTS
# - Dataset is multivariate and numeric
# - Outliers are present → need treatment
# - Features are on different scales normalization required 
# - Chemical composition strongly influences glass type
###############################################################################

#step 6 
#data Preprocessing
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

from feature_engine.outliers import Winsorizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

#1: load the dataset
glass =pd.read_csv("C:/KNN/glass.csv")

print("Initial Shape",glass.shape)
glass.head()

#2: basic data qulity check
glass.info()
print("\nMissing Values:\n ", glass.isnull().sum())
 
#inference 
#dataset has no missing vallues 
#all input feature are numerric
#target column Type is integer encoded

#3 outliers detection
   
plt.figure(figsize=(12,6))
sns.boxplot(data=glass.drop(columns=['Type']),orient='h')
plt.title("Boxplt of chemical feature ")
plt.show()

#based on eda outliers were detected in:'
#RI NA SI K CA FE 
#mg does not have significant outliers

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
for col in ['RI', 'Na', 'Al', 'Si', 'K', 'Ca', 'Fe']:
    glass[col] = winsorizer_column(glass, col)    
    
    
print("Outliers treatment Completed")

#7 target variable label encoding
#convert numeric class labels into meaningful glass types 
glass['Type']=np.where['Type']==1, 'build_win_fl',glass['Type']
glass['Type']=np.where['Type']==2, 'build_win_nfl',glass['Type']
glass['Type']=np.where['Type']==3, 'veh_win_fl',glass['Type']
glass['Type']=np.where['Type']==4, 'veh_win_nfl',glass['Type']
glass['Type']=np.where['Type']==5, 'containers',glass['Type']
glass['Type']=np.where['Type']==6, 'tabeleware',glass['Type']
glass['Type']=np.where['Type']==7, 'headlamp',glass['Type']

glass['Type'].value_counts()

#8: feature scaling - min max noemalization

#why scaling is mandatory:
# KNN is distance based
# chemical feature are on different scales
# prevents domiance of large magnitute feature


X_features = glass.drop(columns=['Type'])
scaler = MinMaxScaler()
X_scaled = pd.DataFrame(scaler.fit_transform(X_features), columns=X_features.columns)

#step 9 split input and output

X=np.array(X_scaled)
y= np.array(glass['Type']) 

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
#########################################################################

#10: KNN Model Training

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=13)
knn.fit(X_train,y_train)

#11: step model evaluation
from sklearn.metrices import accuracy_score
pred_test =knn.predict(X_test)
accuracy_score(pred_test,y_test)

pred_train =knn.predict(X_train)
accuracy_score(pred_test, y_test)



#step 12: hyperparameter tuning k value

acc=[]

for i in range(3, 50,2):
    knn1=KNeighborsClassifier(n_neighbors=i)
    knn1.fit(X_train ,y_train)
    acc.append([
        np.mean(knn1.pred)])
    

plt.plot(range(3,30,2), [i[0] for i in acc],'ro-')
plt.plot(range(3,50,2),[i[0] for i in acc],'bo-')
plt.xlabel("K value")
plt.ylabel("Accuracy")
plt.title("KNN Accuracy Tuning")
plt.show()


'''
What the graph shows
X axis: K value (number of neighbors)
y axis: acuracy
red line : training acciracy 
blue line : testing accuracy
this plot is used   



best K value (Find Answer)
optimal k = 13 to15
highest testing accuracy
minimal gap between training and tasting
best real world performance
'''
from sklearn.neighbors import KNeighborsClassifier
knn =KNeighborsClassifier(n_neighbors=15)
knn.fit(X_train, y_train)

#13: model evaluation

from sklearn.metrices import accuracy_score
pred_test =knn.predict(X_test)
accuracy_score(pred_test,y_test)

pred_train =knn.predict(X_train)
accuracy_score(pred_test, y_test)


#14 model evaluation
from sklearn.metrices import accuracy_score

pred_test =knn.predict(X_test)
accuracy_score(pred_test, y_test)

pred_train = knn.predict(X_train)
accuracy_score(pred_train,y_train)

# final business interpretation
# knn can classify glass types based on chemical composition
# proper scaling and outlier treatment are critical
#model supports atomated glass classification

print("Glass Typen classification using KNN completed")

##########################################################################


#dataset 2

#step 1 Report required
import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#step2 load dataset
pd= pd.read_csv("C:/Assignment/K nearest Neighbour/Fraud_check.csv")
#step 3 basic data understanding
pd.dtypes
pd.shape
pd.columns
pd.describe()

pd1= pd.drop(["Marital.Status","Undergrad"],axis=1)

#EDA (exploratory data analysis)
#shape and size

print("Shape of dataset:" ,pd1.shape)
print("Shape of dataset:" ,pd1.size)


#first moment : mean (central tendancy)
mean_values= pd1.mean(numeric_only=True)
print("\nMean (first moment):\n",mean_values)

#2 variance and std 
var_values =pd1.var(numeric_only=True)
std_values =pd1.std(numeric_only=True)

print("\nvariance (second momemnt):\n",var_values)
print("\nstandard deviation (second momemnt):\n",std_values)

#3 third moment :skewness 
skew_values =pd1 .skew(numeric_only=True)
print("\nSkewness (Third moment):\n",skew_values)    

#inference:
#positive skew -> few samples with high concentration 
#negative skew -> few smaples with very low concentration

#4 moment : Kurtosis(peakedness)
kurt_values = pd1.kurtosis(numeric_only=True)
print("\nKurtosis (4 mpmemt):\n", kurt_values)

#inference;
#platkurtic (<0): flater distribution uniform composition 
#leptokurtosis (>0): sharp peak extreme composition present

#univartate analysis histogram    
pd1.drop(columns=['Urban']).hist(
    figsize=(12,10),
    edgecolor='black'
    )
plt.suptitle("Histograms of fraud check feature")
plt.tight_layout()
plt.show()

#BOXPLOT outlier detection

plt.figure(figsize=(12,6))
sns.boxplot(data=pd1.drop(columns=['Urban']),orient='h')
plt.title("Boxplt of fraud check feature ")
plt.show()

#joint plot
sns.jointplot(data=pd1, x="Taxable.Income", y="City.Population", kind="scatter")
plt.suptitle("Joint Plot: Taxable income and City population", y=1.02)
plt.show()

#pair plot
#sns.pairplot(pd.drop(columns='Urban'),orient='h')
#plt.suptitle("Pair Plot of All Features", y=1.02)
#plt.show()

#hetmap 
numeric_data = pd1.select_dtypes(include=np.number)
plt.figure(figsize=(10,8))
sns.heatmap(
    pd.drop(columns=['Work.Experience']).corr(),
    annot=True,
    cmap='coolwarm'
    
    )
plt.title("Correlation Heatmap - fraud check")
plt.show()


#pdf cdf
num_cols=pd1.select_dtypes(include=np.number).columns.drop(['Work.Experience'])

for col in num_cols:
    plt.figure(figsize=(12,5))
    
    
    #pdf
    plt.subplot(1,2,1)
    sns.kdeplot(pd1[col],fill=True)
    plt.title(f"PDF Of {col}")
    
    
    #CDF
    plt.subplot(1,2,2)
    sorted_vals=np.sort(pd1[col])
    y_vals=np.arange(len(sorted_vals)) / float(len(sorted_vals))
    plt.plot(sorted_vals,y_vals,marker='.',linestyle='name')
    plt.title(f"CDF of {col}")
    
    plt.tight_layout()
    plt.show()
    
#countplot
sns.countplot(x=pd1['Urban'])
plt.title("Distribution of fraud check Types")
plt.show()

# FINAL EDA INSIGHTS
# - Dataset is multivariate and numeric
# - Outliers are present → need treatment
# - Features are on different scales normalization required 
# - Chemical composition strongly influences glass type
################################################################

#step 6 
#data Preprocessing
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

from feature_engine.outliers import Winsorizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

#1: load the datas
pd= pd.read_csv("C:/Assignment/K nearest Neighbour/Fraud_check.csv")

pd1= pd.drop(["Marital.Status","Undergrad"],axis=1)

print("Initial Shape",pd1.shape)
pd1.head()

#2: basic data qulity check
pd1.info()
print("\nMissing Values:\n ", pd1.isnull().sum())
 
#inference 
#dataset has no missing vallues 
#all input feature are numerric or object
#target column Type is integer encoded

#3 outliers detection
   
plt.figure(figsize=(12,6))
sns.boxplot(data=pd1.drop(columns=['Urban']),orient='h')
plt.title("Boxplt of fraud check feature ")
plt.show()

#4: outlier treatment using winsorization

def winsorizer_column(pd1,col):
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
    return winsor.fit_transform(pd1[[col]])

#winsor = Winsorizer(
#    capping_method='iqr',
#    tail='both',
#    fold=1.5,
#    variables=["CLMAGE","LOSS"]
#)

#c1 = winsor.fit_transform(c1)

#apply distribution

# Ensure the name matches your 'def winsorizer_column'
    
    
print("Outliers treatment Completed")

#7 target variable label encoding
#convert numeric class labels into meaningful glass types 
glass['Type']=np.where['Type']==1, 'build_win_fl',glass['Type']
glass['Type']=np.where['Type']==2, 'build_win_nfl',glass['Type']
glass['Type']=np.where['Type']==3, 'veh_win_fl',glass['Type']
glass['Type']=np.where['Type']==4, 'veh_win_nfl',glass['Type']
glass['Type']=np.where['Type']==5, 'containers',glass['Type']
glass['Type']=np.where['Type']==6, 'tabeleware',glass['Type']
glass['Type']=np.where['Type']==7, 'headlamp',glass['Type']

glass['Type'].value_counts()

#8: feature scaling - min max noemalization

#why scaling is mandatory:
# KNN is distance based
# chemical feature are on different scales
# prevents domiance of large magnitute feature


X_features = pd1.drop(columns=['Urban'])
scaler = MinMaxScaler()
X_scaled = pd.DataFrame(scaler.fit_transform(X_features), columns=X_features.columns)

#step 9 split input and output

X=np.array(X_scaled)

y= np.array(pd1['Urban']) 

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

print("Fraud check Datapreprocessing completed succesfully ")

#10: KNN Model Training

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=13)
knn.fit(X_train,y_train)

#11: step model evaluation
from sklearn.metrices import accuracy_score
pred_test =knn.predict(X_test)
accuracy_score(pred_test,y_test)

pred_train =knn.predict(X_train)
accuracy_score(pred_test, y_test)



#step 12: hyperparameter tuning k value

acc=[]

for i in range(3, 50,2):
    knn1=KNeighborsClassifier(n_neighbors=i)
    knn1.fit(X_train ,y_train)
    acc.append([
        np.mean(knn1.pred)])
    

plt.plot(range(3,30,2), [i[0] for i in acc],'ro-')
plt.plot(range(3,50,2),[i[0] for i in acc],'bo-')
plt.xlabel("K value")
plt.ylabel("Accuracy")
plt.title("KNN Accuracy Tuning")
plt.show()


'''
What the graph shows
X axis: K value (number of neighbors)
y axis: acuracy
red line : training acciracy 
blue line : testing accuracy
this plot is used   



best K value (Find Answer)
optimal k = 13 to15
highest testing accuracy
minimal gap between training and tasting
best real world performance
'''
from sklearn.neighbors import KNeighborsClassifier
knn =KNeighborsClassifier(n_neighbors=15)
knn.fit(X_train, y_train)

#13: model evaluation

from sklearn.metrices import accuracy_score
pred_test =knn.predict(X_test)
accuracy_score(pred_test,y_test)

pred_train =knn.predict(X_train)
accuracy_score(pred_test, y_test)


#14 model evaluation
from sklearn.metrices import accuracy_score

pred_test =knn.predict(X_test)
accuracy_score(pred_test, y_test)

pred_train = knn.predict(X_train)
accuracy_score(pred_train,y_train)

# final business interpretation
# knn can classify glass types based on chemical composition
# proper scaling and outlier treatment are critical
#model supports atomated glass classification

print("Fraud check Typen classification using KNN completed")


################################################

#Data set 3

#step 1 Report required
import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#step2 load dataset
df= pd.read_csv("C:/Assignment/K nearest Neighbour/Computer_Data.csv")
#step 3 basic data understanding
df.dtypes
df.shape
df.columns
df.describe()

#check data types
df.dtypes
#inference:'
#all input feature are numeric (float)
#target column type is integer (categorical encoded).

#shape and size

print("Shape of dataset:" ,df.shape)
print("Shape of dataset:" ,df.size)

#summary stat
df.describe()

#first moment : mean (central tendancy)
mean_values= df.mean(numeric_only=True)
print("\nMean (first moment):\n",mean_values)

#2 variance and std 
var_values =df.var(numeric_only=True)
std_values =df.std(numeric_only=True)

print("\nvariance (second momemnt):\n",var_values)
print("\nstandard deviation (second momemnt):\n",std_values)


#3 third moment :skewness 
skew_values =df.skew(numeric_only=True)
print("\nSkewness (Third moment):\n",skew_values)    

#inference:
#positive skew -> few samples with high concentration 
#negative skew -> few smaples with very low concentration

#4 moment : Kurtosis(peakedness)
kurt_values = df.kurtosis(numeric_only=True)
print("\nKurtosis (4 mpmemt):\n", kurt_values)

#inference;
#platkurtic (<0): flater distribution uniform composition 
#leptokurtosis (>0): sharp peak extreme composition present

#univartate analysis histogram    
df.drop(columns=['trend']).hist(
    figsize=(12,10),
    edgecolor='black'
    )
plt.suptitle("Histograms of computer data feature")
plt.tight_layout()
plt.show()



#BOXPLOT outlier detection

plt.figure(figsize=(12,6))
sns.boxplot(data=df.drop(columns=['trend']),orient='h')
plt.title("Boxplt of computer data feature ")
plt.show()

#inference:    

#joint plot
sns.jointplot(data=df, x="price", y="speed", kind="scatter")
plt.suptitle("Joint Plot: price vs speed", y=1.02)
plt.show()

#pair plot
sns.pairplot(df.drop(columns='trend'), hue="species")
plt.suptitle("Pair Plot of All Features", y=1.02)
plt.show()


#hetmap 
plt.figure(figsize=(10,8))
sns.heatmap(
    df.drop(columns=['trend']).corr(),
    annot=True,
    cmap='coolwarm'
    )
plt.title("Correlation Heatmap - computer Dataset")
plt.show()

'''
'''
#pdf cdf
num_cols=df.select_dtypes(include=np.number).columns.drop(['trend'])

for col in num_cols:
    plt.figure(figsize=(12,5))
    
    
    #pdf
    plt.subplot(1,2,1)
    sns.kdeplot(df[col],fill=True)
    plt.title(f"PDF Of {col}")
    
    
    #CDF
    plt.subplot(1,2,2)
    sorted_vals=np.sort(df[col])
    y_vals=np.arange(len(sorted_vals)) / float(len(sorted_vals))
    plt.plot(sorted_vals,y_vals,marker='.',linestyle='name')
    plt.title(f"CDF of {col}")
    
    plt.tight_layout()
    plt.show()
    
#Inference
'''
'''


#class distribution (target analusis)

sns.countplot(x=df['trend'])
plt.title("Distribution of computer data Types")
plt.show()


# FINAL EDA INSIGHTS
# - Dataset is multivariate and numeric
# - Outliers are present → need treatment
# - Features are on different scales normalization required 

#step 6 
#data Preprocessing
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

from feature_engine.outliers import Winsorizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

#1: load the dataset
df =pd.read_csv("C:/Assignment/K nearest Neighbour/Computer_Data.csv")

print("Initial Shape",df.shape)
df.head()

#2: basic data qulity check
df.info()
print("\nMissing Values:\n ", df.isnull().sum())
 
#inference 
#dataset has no missing vallues 
#all input feature are numerric

#3 outliers detection
   
plt.figure(figsize=(12,6))
sns.boxplot(data=df.drop(columns=['trend']),orient='h')
plt.title("Boxplt of computer data feature ")
plt.show()



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
    
print("Outliers treatment Completed")

plt.figure(figsize=(12,6))
sns.boxplot(data=df.drop(columns=['trend']),orient='h')
plt.title("Boxplt of computer data feature ")
plt.show()

#8: feature scaling - min max noemalization

#why scaling is mandatory:
# KNN is distance based
# chemical feature are on different scales
# prevents domiance of large magnitute feature


X_features = df.drop(columns=['trend'])
scaler = MinMaxScaler()
X_scaled = pd.DataFrame(scaler.fit_transform(X_features), columns=X_features.columns)

#step 9 split input and output

X=np.array(X_scaled)
y= np.array(glass['Type']) 

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

#10: KNN Model Training

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=13)
knn.fit(X_train,y_train)

#11: step model evaluation
from sklearn.metrices import accuracy_score
pred_test =knn.predict(X_test)
accuracy_score(pred_test,y_test)

pred_train =knn.predict(X_train)
accuracy_score(pred_test, y_test)



#step 12: hyperparameter tuning k value

acc=[]

for i in range(3, 50,2):
    knn1=KNeighborsClassifier(n_neighbors=i)
    knn1.fit(X_train ,y_train)
    acc.append([
        np.mean(knn1.pred)])
    

plt.plot(range(3,30,2), [i[0] for i in acc],'ro-')
plt.plot(range(3,50,2),[i[0] for i in acc],'bo-')
plt.xlabel("K value")
plt.ylabel("Accuracy")
plt.title("KNN Accuracy Tuning")
plt.show()


'''
What the graph shows
X axis: K value (number of neighbors)
y axis: acuracy
red line : training acciracy 
blue line : testing accuracy
this plot is used   



best K value (Find Answer)
optimal k = 13 to15
highest testing accuracy
minimal gap between training and tasting
best real world performance
'''
from sklearn.neighbors import KNeighborsClassifier
knn =KNeighborsClassifier(n_neighbors=15)
knn.fit(X_train, y_train)

#13: model evaluation

from sklearn.metrices import accuracy_score
pred_test =knn.predict(X_test)
accuracy_score(pred_test,y_test)

pred_train =knn.predict(X_train)
accuracy_score(pred_test, y_test)


#14 model evaluation
from sklearn.metrices import accuracy_score

pred_test =knn.predict(X_test)
accuracy_score(pred_test, y_test)

pred_train = knn.predict(X_train)
accuracy_score(pred_train,y_train)

# final business interpretation
# knn can classify glass types based on chemical composition
# proper scaling and outlier treatment are critical
#model supports atomated glass classification

print("Glass Typen classification using KNN completed")





##########################################################################


#dataset 4

#step 1 Report required
import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#EDA (exploratory data analysis)

#step2 load dataset
df= pd.read_csv("C:/Assignment/K nearest Neighbour/SAT_GPA.csv")
#step 3 basic data understanding
df.dtypes
df.shape
df.columns
df.describe()

#shape and size

print("Shape of dataset:" ,df.shape)
print("Shape of dataset:" ,df.size)

'''
ELement Meaning

Min / Max | Range of chemical composition | Helps define safe and usabi Mean | Average concentration | Typical composition used in production 01-03 | Middle 50% spread | Indicates consistency in raw material mix Median | Central tendency | Robust benchmark against extreme batches | | IQR | Q3 - Q1 | Detects stability 
of production process
'''
#first moment : mean (central tendancy)
mean_values= df.mean(numeric_only=True)
print("\nMean (first moment):\n",mean_values)

#2 variance and std 
var_values =df.var(numeric_only=True)
std_values =df.std(numeric_only=True)

print("\nvariance (second momemnt):\n",var_values)
print("\nstandard deviation (second momemnt):\n",std_values)


#3 third moment :skewness 
skew_values =df.skew(numeric_only=True)
print("\nSkewness (Third moment):\n",skew_values)    

#inference:
#positive skew -> few samples with high concentration 
#negative skew -> few smaples with very low concentration

#4 moment : Kurtosis(peakedness)
kurt_values = df.kurtosis(numeric_only=True)
print("\nKurtosis (4 mpmemt):\n", kurt_values)

#inference;
#platkurtic (<0): flater distribution uniform composition 
#leptokurtosis (>0): sharp peak extreme composition present

#univartate analysis histogram    
df.drop(columns=['GPA']).hist(
    figsize=(12,10),
    edgecolor='black'
    )
plt.suptitle("Histograms of sat score feature")
plt.tight_layout()
plt.show()


#BOXPLOT outlier detection

plt.figure(figsize=(12,6))
sns.boxplot(data=df.drop(columns=['GPA']),orient='h')
plt.title("Boxplt of sat score feature ")
plt.show()

#inference:

#joint plot
sns.jointplot(data=df,kind="scatter")
plt.suptitle("Joint Plot", y=1.02)
plt.show()

#pair plot
sns.pairplot(df.drop(columns='GPA'))
plt.suptitle("Pair Plot of All Features", y=1.02)
plt.show()


#hetmap 
plt.figure(figsize=(10,8))
sns.heatmap(
    df.drop(columns=['GPA']).corr(),
    annot=True,
    cmap='coolwarm'
    )
plt.title("Correlation Heatmap - sat score Dataset")
plt.show()

#pdf cdf
num_cols=glass.select_dtypes(include=np.number).columns.drop(['type'])

for col in num_cols:
    plt.figure(figsize=(12,5))
    
    
    #pdf
    plt.subplot(1,2,1)
    sns.kdeplot(glass[col],fill=True)
    plt.title(f"PDF Of {col}")
    
    
    #CDF
    plt.subplot(1,2,2)
    sorted_vals=np.sort(glass[col])
    y_vals=np.arange(len(sorted_vals)) / float(len(sorted_vals))
    plt.plot(sorted_vals,y_vals,marker='.',linestyle='name')
    plt.title(f"CDF of {col}")
    
    plt.tight_layout()
    plt.show()
    
#Inference
'''
'''
#pdf-shows distribution shape of each chemical
#Cdf- helps decide percentile based threshold
#useful for quality control and segmentation

#class distribution (target analusis)

sns.countplot(x=glass['type'])
plt.title("Distribution of Glass Types")
plt.show()

#inference
#the dataset is imabalanced with glass types 1 and 2 having the 
#highest number of samples while types 3,5 and 6 are 

# FINAL EDA INSIGHTS
# - Dataset is multivariate and numeric
# - Outliers are present → need treatment
# - Features are on different scales normalization required 
# - Chemical composition strongly influences glass type

#step 6 
#data Preprocessing
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

from feature_engine.outliers import Winsorizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

#1: load the dataset
df=pd.read_csv("C:/Assignment/K nearest Neighbour/SAT_GPA.csv")

print("Initial Shape",df.shape)
df.head()

#2: basic data qulity check
df.info()
print("\nMissing Values:\n ", df.isnull().sum())
 
#inference 
#dataset has no missing vallues 
#all input feature are numerric
#target column Type is integer encoded

#3 outliers detection
   
plt.figure(figsize=(12,6))
sns.boxplot(data=df.drop(columns=['GPA']),orient='h')
plt.title("Boxplt of chemical feature ")
plt.show()



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
for col in ['SAT_Scores','GPA']:
    df[col] = winsorizer_column(df, col)    
    
    
print("Outliers treatment Completed")

#7 target variable label encoding
#convert numeric class labels into meaningful glass types 
glass['Type']=np.where['Type']==1, 'build_win_fl',glass['Type']
glass['Type']=np.where['Type']==2, 'build_win_nfl',glass['Type']
glass['Type']=np.where['Type']==3, 'veh_win_fl',glass['Type']
glass['Type']=np.where['Type']==4, 'veh_win_nfl',glass['Type']
glass['Type']=np.where['Type']==5, 'containers',glass['Type']
glass['Type']=np.where['Type']==6, 'tabeleware',glass['Type']
glass['Type']=np.where['Type']==7, 'headlamp',glass['Type']

glass['Type'].value_counts()

#8: feature scaling - min max noemalization

#why scaling is mandatory:
# KNN is distance based
# chemical feature are on different scales
# prevents domiance of large magnitute feature


X_features = glass.drop(columns=['Type'])
scaler = MinMaxScaler()
X_scaled = pd.DataFrame(scaler.fit_transform(X_features), columns=X_features.columns)

#step 9 split input and output

X=np.array(X_scaled)
y= np.array(glass['Type']) 

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

#10: KNN Model Training

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=13)
knn.fit(X_train,y_train)

#11: step model evaluation
from sklearn.metrices import accuracy_score
pred_test =knn.predict(X_test)
accuracy_score(pred_test,y_test)

pred_train =knn.predict(X_train)
accuracy_score(pred_test, y_test)



#step 12: hyperparameter tuning k value

acc=[]

for i in range(3, 50,2):
    knn1=KNeighborsClassifier(n_neighbors=i)
    knn1.fit(X_train ,y_train)
    acc.append([
        np.mean(knn1.pred)])
    

plt.plot(range(3,30,2), [i[0] for i in acc],'ro-')
plt.plot(range(3,50,2),[i[0] for i in acc],'bo-')
plt.xlabel("K value")
plt.ylabel("Accuracy")
plt.title("KNN Accuracy Tuning")
plt.show()


'''
What the graph shows
X axis: K value (number of neighbors)
y axis: acuracy
red line : training acciracy 
blue line : testing accuracy
this plot is used   



best K value (Find Answer)
optimal k = 13 to15
highest testing accuracy
minimal gap between training and tasting
best real world performance
'''
from sklearn.neighbors import KNeighborsClassifier
knn =KNeighborsClassifier(n_neighbors=15)
knn.fit(X_train, y_train)

#13: model evaluation

from sklearn.metrices import accuracy_score
pred_test =knn.predict(X_test)
accuracy_score(pred_test,y_test)

pred_train =knn.predict(X_train)
accuracy_score(pred_test, y_test)


#14 model evaluation
from sklearn.metrices import accuracy_score

pred_test =knn.predict(X_test)
accuracy_score(pred_test, y_test)

pred_train = knn.predict(X_train)
accuracy_score(pred_train,y_train)

# final business interpretation
# knn can classify glass types based on chemical composition
# proper scaling and outlier treatment are critical
#model supports atomated glass classification

print("Glass Typen classification using KNN completed")
