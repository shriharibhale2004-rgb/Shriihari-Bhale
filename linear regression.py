# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 15:54:00 2026

@author: shrih
"""

#dataset 1

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# step 2
#load dataset
cal=pd.read_csv("C:/Linear Regression/calories_consumed.csv")
cal.columns=["wt_gained","cal_consumed"]
print("First 5 Rows:\n",cal.head())

#step3 basic EDA
print("\nData types:\n",cal.dtypes)
print("\nSummary Statistics:\n",cal.describe())

#business moment decision

#mean 
print("\nMean:\n",cal.mean())
'''
Inference:
357.714
2340.714
Average calorie intake represents typical daily consumption. 
Average weight gain shows normal gain pattern. 
If both means are high + population Likely in calorie surptus. 
Indicates calories may be contributing to weight gain.
'''
#variance
print("\nVariance:\n",cal.var())
'''
Inference:

High variance in calories rent eating habits.
High variance in weight gain metabolic differences. 
Larger spread means predictions may vary across individu
'''
#standard deviation 
print("\nStandard Deviation:\n",cal.std())
'''
Inference:
Shows average deviation from mean,
Lower value stable population behavior.
Higher value → more fluctuation in diet and weight gain
'''

#skewness 
print("\nSkewness:\n",cal.skew())
'''
Inference:

Skew = 0 Symmetric distribution.
Positive skew few individuals consume very high calories.
Positive skew in weight cal consumtion too → few individuals gain extreme we
'''
#Kurtosis
print("\nKurtosis:\n",cal.kurtosis())
'''
Inference:

High kurtosis → presence of extreme values.
Low kurtosis → uniform spread.
Extreme calorie or wetght values may influence regression
'''
#correlation
print("\ncorrelation matrix:\n",np.corrcoef(cal.cal_consumed,cal.wt_gained))
#

#step 4 univariate analysis

#histogram- weight gained
plt.figure(figsize=(6,4))
plt.hist(cal.wt_gained)
plt.title("Weight Gained Distribution")
plt.xlabel("weight gained")
plt.ylabel("Frequency")
plt.show()
'''
Inference
Most individuals gained Lower to moderate weight (clustered in the Lower range 
The distribution appears positively skewed (right-skewed). 
A few individuals show very high weight gain, creating a long right tail.
These extreme values may act as outliers and can influence regresston results.
'''
#histogram - calories consumed
plt.figure(figsize=(6,4))
plt.hist(cal.cal_consumed)
plt.title("Calories consumed Distribution")
plt.xlabel("Calories gained")
plt.ylabel("Frequency")
plt.show()
'''
Inference:

Calorie intake is spread across a moderate to high range.
Most individuals consume calories within a normal daily intake band. 
The distribution shows a slight right skew, indicating a few individuals consu 
Presence of high-calorie values suggests potential overconsumption cases.
'''
#Box plot(outlier Detection)
plt.figure(figsize=(8, 5))
sns.boxplot(data=cal[['cal_consumed', 'wt_gained']], orient='h')
plt.title("Boxplot of Numerical Features")
plt.show()
'''
Inference:

The data points Lie within the whisters- no extrene outtiers detected 
Colortes consumed has a wider range compared to weight gained, 
Hediam values eppeur centrally pesitiened, inficating stable distritutions
'''
#bivariate analysis(scatter plot)
plt.figure(figsize=(6,4))
sns.scatterplot(x='cal_consumed', y='wt_gained', data=cal)
plt.title("Calories Consumed vs Weight Gained")
plt.xlabel("Calories Consumed")
plt.ylabel("Weight Gained")
plt.show()
'''
Inference:

Clear positive Linear relationship observed.
As calories consumed increase, weight gained also increases. 
Data points follow an upward trend, indicating a strong correlation. 
No major irregular patterns or clustering observed,
'''
#correlation heatmap
plt.figure(figsize=(5,4))
sns.heatmap(cal.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()
'''
Inference:

The correlation between calòries consumed and weight gained is 0.95, which ina 
This means as calorie intake increases, weight gain increases significantly. 
The value is close to +1, showing a strong Linegr association. 
No negative relationship observed. "
'''
# pdf and cdf analysis
for col in ['cal_consumed', 'wt_gained']: 
    plt.figure(figsize=(12,4))

# PDF
    plt.subplot(1,2,1)
    sns.kdeplot(cal[col], fill=True)
    plt.title(f'PDF of {col}')

# CDF
    plt.subplot(1,2,2)
    sorted_vals = np.sort(cal[col])
    y = np.arange(len(sorted_vals))/len(sorted_vals)
    plt.plot(sorted_vals, y)
    plt.title(f'CDF of (col)')
    plt.show()


#########################################################
# Data Preprocessing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from scipy.stats import skew
from feature_engine.outliers import Winsorizer

#STEP 2: LOAD DATASET
cal = pd.read_csv("c:/360DG/Datasets/calories_consumed.csv") 
cal.columns = ["wt_gained", "cal_consumed"]
print("Initial Shape;", cal.shape) 
print(cal.head())

# step 3 basic cleaning

print("\nMissing Values Before treatment:\n", cal.isnull().sum())

'''
inference :
    dataset contains only numerical variables
    no identifier column present
    if missing values exit - must be handle
    if zero - dataset is clean
'''
#STEP 4: MISSING VALUE TREATMENT if applicable
# Using Median Imputation (robust to skewness)

for col in cal.columns: 
    cal[col].fillna(cal[col].median(), inplace=True)

print("\nMissing Values After Treatment:\n", cal.isnull().sum())

#step 5 duplicate removal if aplicabel

cal.drop_duplicates(inplace=True)
print("\nShape after removing duplicates :",cal.shape)

'''
inference:
    removes repeated observations
    prevents model from learning duplicated patterns
    improves generalization capability
    '''

#step6 outlier detection

plt.figure(figsize=(8, 5))
sns.boxplot(data=cal,orient='h')
plt.title("Boxplot before treatment")
plt.show()    
    
#step 7 outlier treatment (winsorization if applicabel)

winsor = Winsorizer(
    capping_method='iqr',
    tail='both',
    fold=1.5,
    variables=['cal_consumed','wt_gained']
   )
cal[['cal_consumed','wt_gained']] = winsor.fit_transform(
    cal[['cal_consumed', 'wt_gained']]
)

plt.figure(figsize=(8,5))
sns.boxplot(data=cal, orient= 'h')
plt.title("Boxplot After Winsorization") 
plt.show()

'''
Inference:

Extreme values capped using IQR method.)   
'''

#step 8 skewness check
print("\nSkewness:\n",cal.skew())

'''
Inference:
Skewness > 1→ Strong skew (Log transformation may help) 
Mild skew transformation optional.
Helps decide model transformation stage.

'''

# FINAL PREPROCESSING SUMMARY
'''
-Dataset validated and cleaned,
-Missing values handled using median.
-Duplicates removed,
-Outliers treated using IQR-based Winsorization
'''

#################################################################

#model development- simple linear regression 
# let us apply to various models and check the  feasibility

import statsmodels.formula.api as snf
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression

# 1 SIMPLE LINEAR REGRESSION

model1 = snf.ols('wt_gained ~ cal_consumed', data=cal).fit() 
pred1 = model1.predict(cal)
rmse1 = np.sqrt(np.mean((cal.wt_gained - pred1)**2))
print("SLR RMSE:", rmse1)
#103.30
model1.summary()
'''
#R-squared = 0.897 > 0.80, Model is very strong
#p = 0 < 0.05 hence acceptable
#beta-0 = -625.75
#beta-1 = 0.4202
Goal of the Model
We are trying to predict wt_gained (Dependent Variable)
using cal_consumed (Independent Vartable),

1. Model Fit (Goodness of Fit)
R-squared = 0.897(applicable for MLR) 
"Adjusted R2 tells us whether adding more variables truly improves the model 
→ About 89.7% of the variation in wt_gained is explained by cal consumed.
This means the model fits the data very well.
Adjusted R-squared = 0.888
→ Adjusted for number of predictors; still very high
Since there is only one predictor, overfitting is not a concern.

purpose of F-statistic
Does the independent variable(s) collectively explain the dependent variable? 
Or is the relationship happening just by chance?
F-statistic = 104.3
An F-value of 104.3 is very Large.
Model is statistically significant.
It performs much better than a model with no predictor.
Calories consumed significantly explains weight gain.

2. Coefficient Interpretation
Variable Coefficient Interpretation
Intercept -625.75 When calories = 0, predicted weight gain is -625g (not 
                                                                     cal_consumed +0.4202 For every 1 unit increase in calories, weight increases
P-value for cal consumed = 0.000
Highly statistically significant.

This confirms:
Higher calorie intake Leads to higher weight gain.

3. Residual Analysis

The Durbin-Watson statistic checks whether residuals are independent,

DW Value Meaning
= 2 No autocorrelation (Ideal)
< 1.5 Positive autocorrelation
1.5-2.5 Acceptable

Durbin-Watson = 2.537

Slightly above 2 but still acceptable.
No serious autocorrelation problem.

NormaLity Check

Jarque-Bera p-value = 0.541 (> 0.05) 
Residuals are approximately normally distributed. 
Regression assumption satisfied.

'''
#LOG Model(logx)
#model2
model2 = snf.ols('wt_gained ~ np.log(cal_consumed)', data=cal).fit()
pred2 = model2.predict(cal)

rmse2 = np.sqrt(np.mean((cal.wt_gained - pred2)**2))

print("Log-X Model RMSE:", rmse2)

#141.005
model2.summary()
'''
#R-squared = 0.808 = 0.8, 
there is scope for improvement #p = 0.000 < 0.05 hence acceptable

F-statistic = 50.40
Prob(F) = 1.25e-05 (< 0.05)

Model is statistically significant.
The Log transformation of calories significantly explains weight gain. 
The model performs much better than a model with no predictor.

Coefficient Interpretation
Intercept = -6955.65
When Log(calories) = 0, predicted weight gain is -6955.65 (not practically mea

Log(cal_consumed) = +948.37
For every 1 unit increase in Log(calories), weight increases by 948.37 units. 
Strong positive relationship.

P-value for Log(cal_consumed) = 0.000
Highly statistically significant.


This confirms:
Higher calorie intake (even after Log transformation) leads to higher weight g

Residual Analysis

Durbin-watson = 2.438
→ Lies within acceptable range (1.5-2.5). 
serious autocorrelation problem.

Normality Check

Jarque-Bera p-value = 0.566 (> 0.05)
Residuals are approximately normally distributed.
Regression assumptions are satisfied.

Final Comparison Insight
Although the model is statistically significant and explains about 81% of the
In One Sentence
Log(calories) has a statistically significant positive impact on weight gained
'''
#3.EXPONENTIAL MODEL (log y)
model3 = snf.ols('np.log(wt_gained) ~ cal_consumed', data=cal).fit()
pred3 = model3.predict(cal)
# Convert predicted log values back using exp()
pred_3 = np.exp(pred3)
rmse3 = np.sqrt(np.mean((cal.wt_gained - pred_3) ** 2))
print("Exponential Model RMSE:", rmse3)
#118.04
model3.summary()
'''
Inference
R-squared = 0.878 > 0.80, Model is strong
#p = 0.00 < 0.05 hence acceptable
#beta-0 = 2.8387
#beta-1 = 0.0011
Goal of the Model
We are trying to predict log(wt_gained) (Dependent Variable) using cal_consume
Model Fit (Goodness of Fit)
R-squared = 0.878 → About 87.8% of the variation in Log(wt gained) is explained by cal consumed.
'''

# 4 POLYNOMIAL MODEL
model4 = snf.ols(
    'np.log(wt_gained) ~ cal_consumed + I(cal_consumed**2)',
    data=cal
).fit()

pred4 = np.exp(model4.predict(cal))
rmse4 = np.sqrt(np.mean((cal.wt_gained - pred4)**2))
print("Polynomial Model RMSE:", rmse4)
#117.41
model4. summary()

'''
#R-squared = 0.878 > 0.85, Model is strong
#Adjusted R-squared = 0.855 (slightly reduced after adding extra term) 
#p (F-statistic) = 9.61e-06 < 0.05 hence overall model acceptable
#beta-0 = 2.8287
#beta-1 = 0.0011
#beta-2 = -1.675e-09

Goal of the Model
test 2325.py X Hypothels testing_simulation cade 2125.py X 2testpy X chi squzre_test 2025.py X Unear Regression calory 2026.py X Linear_Ragreson Celory 2006 finalgy X

The polynomial term does NOT improve the model.

The relationship remains primarily Linear.

Residual Analysis

Durbin-Watson = 3.131
Greater than 2.5
Possible negative autocorrelation present,

Normality Check
Jarque-Bera p-value = 0.0466 (< 0.05)
Residuals are not perfectly normally distributed.

Final Interpretation
Although the polynomial model has high R2 (0.878), the squared term is complete
"The polynomial model explains about 88% of the variation in Log(weight gainea

'''
##################################
#Model Comparison
results = pd.DataFrame({

     "Model": ["SLR", "Log-X", "Exponential", "Polynomial"],
     "RMSE": [rmse1, rmse2, rmse3, rmse4],
     "R_squared": [model1.rsquared,
                   model2.rsquared,
                   model3.rsquared,
                   model4.rsquared
     ]
})

print("\nModel Comparison:\n", results)

#######################
#SELECT BEST MODEL

best_model_name = results.sort_values("RMSE").iloc[0]["Model"]
print("\nBest Model Based on RMSE:", best_model_name)

# TRAIN-TEST VALIDATION USING BEST MODEL (SLR IS BEST HERE)

train, test = train_test_split(cal, test_size=0.3, random_state=42)

# Since SLR has highest R2 (0.897) and lowest RMSE, choose model1 
final_model = snf.ols('wt_gained ~ cal_consumed', data=train).fit()

train_pred = final_model.predict(train)
test_pred = final_model.predict(test)

train_rmse = np.sqrt(np.mean((train.wt_gained - train_pred)**2)) 
test_rmse = np.sqrt(np.mean((test.wt_gained - test_pred)**2))

print("\nTrain RMSE:", train_rmse)
print("Test RMSE :", test_rmse)
#########################################
#Business Impact of the Project
###############################
'''
Calories Consumed vs Weight Gained Analysis
1️ Data-Driven Diet Planning
The model shows a strong positive relationship between calorie intake and weight gain.
About 80–90% of weight variation is explained by calories.
Enables nutritionists to predict expected weight gain for a given calorie intake.
Helps design personalized calorie-controlled diet plans.

2️ Obesity Risk Identification
Individuals consuming higher calories are statistically more likely to gain more weight.
High-risk calorie thresholds can be identified using CDF analysis.
Supports early intervention programs for obesity prevention.

3️ Preventive Healthcare Strategy
Healthcare providers can estimate:
How much weight gain may occur
What calorie limit keeps weight stable
 Reduces risk of:
Diabetes
Hypertension
Cardiovascular diseases

4️ Fitness & Wellness Industry Application
Gyms and wellness apps can:
Predict weight gain/loss trends
Provide calorie recommendations
Personalize fitness targets
'''
#################################################################

#dataset 2

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# step 2
#load dataset
df=pd.read_csv("C:/Assignment/Simple linear regression/emp_data (1).csv")
df.columns=["salary_hike","chum_rate"]
print("First 5 Rows:\n",df.head())

#step3 basic EDA
print("\nData types:\n",df.dtypes)
print("\nSummary Statistics:\n",df.describe())

#business moment decision

#mean 
print("\nMean:\n",df.mean())
'''
Inference:
1688.6
72.9

Average calorie intake represents typical daily consumption. 
Average weight gain shows normal gain pattern. 
If both means are high + population Likely in calorie surptus. 
Indicates calories may be contributing to weight gain.
'''
#variance
print("\nVariance:\n",df.var())
'''
Inference:

High variance in calories rent eating habits.
High variance in weight gain metabolic differences. 
Larger spread means predictions may vary across individu
'''
#standard deviation 
print("\nStandard Deviation:\n",df.std())
'''
Inference:
Shows average deviation from mean,
Lower value stable population behavior.
Higher value → more fluctuation in diet and weight gain
'''

#skewness 
print("\nSkewness:\n",df.skew())
'''
Inference:

Skew = 0 Symmetric distribution.
Positive skew few individuals consume very high calories.
Positive skew in weight cal consumtion too → few individuals gain extreme we
'''
#Kurtosis
print("\nKurtosis:\n",cal.kurtosis())
'''
Inference:

High kurtosis → presence of extreme values.
Low kurtosis → uniform spread.
Extreme calorie or wetght values may influence regression
'''
#correlation
print("\ncorrelation matrix:\n",np.corrcoef(df.salary_hike,df.chum_rate))
#

#step 4 univariate analysis

#histogram- weight gained
plt.figure(figsize=(6,4))
plt.hist(df.salary)
plt.title("salary hike Distribution")
plt.xlabel("salry hike")
plt.ylabel("Frequency")
plt.show()
'''
Inference
Most individuals gained Lower to moderate weight (clustered in the Lower range 
The distribution appears positively skewed (right-skewed). 
A few individuals show very high weight gain, creating a long right tail.
These extreme values may act as outliers and can influence regresston results.
'''
#histogram - calories consumed
plt.figure(figsize=(6,4))
plt.hist(df.chum_rate)
plt.title("chum out rate Distribution")
plt.xlabel("chum rate")
plt.ylabel("Frequency")
plt.show()
'''
Inference:

Calorie intake is spread across a moderate to high range.
Most individuals consume calories within a normal daily intake band. 
The distribution shows a slight right skew, indicating a few individuals consu 
Presence of high-calorie values suggests potential overconsumption cases.
'''
#Box plot(outlier Detection)
plt.figure(figsize=(8, 5))
sns.boxplot(data=df[['salary_hike', 'chum_rate']], orient='h')
plt.title("Boxplot of Numerical Features")
plt.show()
'''
Inference:

The data points Lie within the whisters- no extrene outtiers detected 
Colortes consumed has a wider range compared to weight gained, 
Hediam values eppeur centrally pesitiened, inficating stable distritutions
'''
#bivariate analysis(scatter plot)
plt.figure(figsize=(6,4))
sns.scatterplot(x='salary_hike', y='chum_rate', data=df)
plt.title("salary hike vs chum rate")
plt.xlabel("salary hike")
plt.ylabel("chum rate")
plt.show()
'''
Inference:

Clear positive Linear relationship observed.
As calories consumed increase, weight gained also increases. 
Data points follow an upward trend, indicating a strong correlation. 
No major irregular patterns or clustering observed,
'''
#correlation heatmap
plt.figure(figsize=(5,4))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()
'''
Inference:

The correlation between calòries consumed and weight gained is 0.95, which ina 
This means as calorie intake increases, weight gain increases significantly. 
The value is close to +1, showing a strong Linegr association. 
No negative relationship observed. "
'''
# pdf and cdf analysis
for col in ['salary_hike', 'chum_rate']: 
    plt.figure(figsize=(12,4))

# PDF
    plt.subplot(1,2,1)
    sns.kdeplot(df[col], fill=True)
    plt.title(f'PDF of {col}')

# CDF
    plt.subplot(1,2,2)
    sorted_vals = np.sort(df[col])
    y = np.arange(len(sorted_vals))/len(sorted_vals)
    plt.plot(sorted_vals, y)
    plt.title(f'CDF of (col)')
    plt.show()


#########################################################
# Data Preprocessing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from scipy.stats import skew
from feature_engine.outliers import Winsorizer

#STEP 2: LOAD DATASET
df = pd.read_csv("c:/360DG/Datasets/calories_consumed.csv") 
df.columns = ["salary_hike", "chum_rate"]
print("Initial Shape;", df.shape) 
print(df.head())

# step 3 basic cleaning

print("\nMissing Values Before treatment:\n", df.isnull().sum())

'''
inference :
    dataset contains only numerical variables
    no identifier column present
    if missing values exit - must be handle
    if zero - dataset is clean
'''
#STEP 4: MISSING VALUE TREATMENT if applicable
# Using Median Imputation (robust to skewness)

for col in cal.columns: 
    df[col].fillna(df[col].median(), inplace=True)

print("\nMissing Values After Treatment:\n", df.isnull().sum())

#step 5 duplicate removal if aplicabel

df.drop_duplicates(inplace=True)
print("\nShape after removing duplicates :",df.shape)

'''
inference:
    removes repeated observations
    prevents model from learning duplicated patterns
    improves generalization capability
    '''

#step6 outlier detection

plt.figure(figsize=(8, 5))
sns.boxplot(data=df,orient='h')
plt.title("Boxplot before treatment")
plt.show()    
    
#step 7 outlier treatment (winsorization if applicabel)

winsor = Winsorizer(
    capping_method='iqr',
    tail='both',
    fold=1.5,
    variables=['salary_hike','chum_rate']
   )
df[['salary_hike','chum_rate']] = winsor.fit_transform(
    df[['cal_consumed', 'wt_gained']]
)

plt.figure(figsize=(8,5))
sns.boxplot(data=df, orient= 'h')
plt.title("Boxplot After Winsorization") 
plt.show()

'''
Inference:

Extreme values capped using IQR method.)   
'''

#step 8 skewness check
print("\nSkewness:\n",df.skew())

'''
Inference:
Skewness > 1→ Strong skew (Log transformation may help) 
Mild skew transformation optional.
Helps decide model transformation stage.

'''

# FINAL PREPROCESSING SUMMARY
'''
-Dataset validated and cleaned,
-Missing values handled using median.
-Duplicates removed,
-Outliers treated using IQR-based Winsorization
'''

#################################################################

#model development- simple linear regression 
# let us apply to various models and check the  feasibility

import statsmodels.formula.api as snf
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression

# 1 SIMPLE LINEAR REGRESSION

model1 = snf.ols('salary_hike ~ chum_rate', data=df).fit() 
pred1 = model1.predict(df)
rmse1 = np.sqrt(np.mean((df.salary_hike - pred1)**2))
print("SLR RMSE:", rmse1)
#35.892
model1.summary()
'''
#R-squared = 0.897 > 0.80, Model is very strong
#p = 0 < 0.05 hence acceptable
#beta-0 = -625.75
#beta-1 = 0.4202
Goal of the Model
We are trying to predict wt_gained (Dependent Variable)
using cal_consumed (Independent Vartable),

1. Model Fit (Goodness of Fit)
R-squared = 0.897(applicable for MLR) 
"Adjusted R2 tells us whether adding more variables truly improves the model 
→ About 89.7% of the variation in wt_gained is explained by cal consumed.
This means the model fits the data very well.
Adjusted R-squared = 0.888
→ Adjusted for number of predictors; still very high
Since there is only one predictor, overfitting is not a concern.

purpose of F-statistic
Does the independent variable(s) collectively explain the dependent variable? 
Or is the relationship happening just by chance?
F-statistic = 104.3
An F-value of 104.3 is very Large.
Model is statistically significant.
It performs much better than a model with no predictor.
Calories consumed significantly explains weight gain.

2. Coefficient Interpretation
Variable Coefficient Interpretation
Intercept -625.75 When calories = 0, predicted weight gain is -625g (not 
                                                                     cal_consumed +0.4202 For every 1 unit increase in calories, weight increases
P-value for cal consumed = 0.000
Highly statistically significant.

This confirms:
Higher calorie intake Leads to higher weight gain.

3. Residual Analysis

The Durbin-Watson statistic checks whether residuals are independent,

DW Value Meaning
= 2 No autocorrelation (Ideal)
< 1.5 Positive autocorrelation
1.5-2.5 Acceptable

Durbin-Watson = 2.537

Slightly above 2 but still acceptable.
No serious autocorrelation problem.

NormaLity Check

Jarque-Bera p-value = 0.541 (> 0.05) 
Residuals are approximately normally distributed. 
Regression assumption satisfied.

'''
#LOG Model(logx)
#model2
model2 = snf.ols('salary_hike ~ np.log(chum_rate)', data=df).fit()
pred2 = model2.predict(df)

rmse2 = np.sqrt(np.mean((df.salary_hike - pred2)**2))

print("Log-X Model RMSE:", rmse2)

#31.069
model2.summary()
'''
#R-squared = 0.808 = 0.8, 
there is scope for improvement #p = 0.000 < 0.05 hence acceptable

F-statistic = 50.40
Prob(F) = 1.25e-05 (< 0.05)

Model is statistically significant.
The Log transformation of calories significantly explains weight gain. 
The model performs much better than a model with no predictor.

Coefficient Interpretation
Intercept = -6955.65
When Log(calories) = 0, predicted weight gain is -6955.65 (not practically mea

Log(cal_consumed) = +948.37
For every 1 unit increase in Log(calories), weight increases by 948.37 units. 
Strong positive relationship.

P-value for Log(cal_consumed) = 0.000
Highly statistically significant.


This confirms:
Higher calorie intake (even after Log transformation) leads to higher weight g

Residual Analysis

Durbin-watson = 2.438
→ Lies within acceptable range (1.5-2.5). 
serious autocorrelation problem.

Normality Check

Jarque-Bera p-value = 0.566 (> 0.05)
Residuals are approximately normally distributed.
Regression assumptions are satisfied.

Final Comparison Insight
Although the model is statistically significant and explains about 81% of the
In One Sentence
Log(calories) has a statistically significant positive impact on weight gained
'''
#3.EXPONENTIAL MODEL (log y)
model3 = snf.ols('np.log(salary_hike) ~ chum_rate', data=df).fit()
pred3 = model3.predict(df)
# Convert predicted log values back using exp()
pred_3 = np.exp(pred3)
rmse3 = np.sqrt(np.mean((df.salary_hike - pred_3) ** 2))
print("Exponential Model RMSE:", rmse3)
#34.268
model3.summary()
'''
Inference
R-squared = 0.878 > 0.80, Model is strong
#p = 0.00 < 0.05 hence acceptable
#beta-0 = 2.8387
#beta-1 = 0.0011
Goal of the Model
We are trying to predict log(wt_gained) (Dependent Variable) using cal_consume
Model Fit (Goodness of Fit)
R-squared = 0.878 → About 87.8% of the variation in Log(wt gained) is explained by cal consumed.
'''

# 4 POLYNOMIAL MODEL
model4 = snf.ols(
    'np.log(salary_hike) ~ chum_rate + I(chum_rate**2)',
    data=df
).fit()

pred4 = np.exp(model4.predict(df))
rmse4 = np.sqrt(np.mean((df.salary_hike - pred4)**2))
print("Polynomial Model RMSE:", rmse4)
#13.025
model4. summary()

'''
#R-squared = 0.878 > 0.85, Model is strong
#Adjusted R-squared = 0.855 (slightly reduced after adding extra term) 
#p (F-statistic) = 9.61e-06 < 0.05 hence overall model acceptable
#beta-0 = 2.8287
#beta-1 = 0.0011
#beta-2 = -1.675e-09

Goal of the Model
test 2325.py X Hypothels testing_simulation cade 2125.py X 2testpy X chi squzre_test 2025.py X Unear Regression calory 2026.py X Linear_Ragreson Celory 2006 finalgy X

The polynomial term does NOT improve the model.

The relationship remains primarily Linear.

Residual Analysis

Durbin-Watson = 3.131
Greater than 2.5
Possible negative autocorrelation present,

Normality Check
Jarque-Bera p-value = 0.0466 (< 0.05)
Residuals are not perfectly normally distributed.

Final Interpretation
Although the polynomial model has high R2 (0.878), the squared term is complete
"The polynomial model explains about 88% of the variation in Log(weight gainea

'''
##################################
#Model Comparison
results = pd.DataFrame({

     "Model": ["SLR", "Log-X", "Exponential", "Polynomial"],
     "RMSE": [rmse1, rmse2, rmse3, rmse4],
     "R_squared": [model1.rsquared,
                   model2.rsquared,
                   model3.rsquared,
                   model4.rsquared
     ]
})

print("\nModel Comparison:\n", results)

#######################
#SELECT BEST MODEL

best_model_name = results.sort_values("RMSE").iloc[0]["Model"]
print("\nBest Model Based on RMSE:", best_model_name)

# TRAIN-TEST VALIDATION USING BEST MODEL (SLR IS BEST HERE)

train, test = train_test_split(df, test_size=0.3, random_state=42)

# Since SLR has highest R2 (0.897) and lowest RMSE, choose model1 
final_model = snf.ols('salary_hike ~ chum_rate', data=train).fit()

train_pred = final_model.predict(train)
test_pred = final_model.predict(test)

train_rmse = np.sqrt(np.mean((train.salary_hike - train_pred)**2)) 
test_rmse = np.sqrt(np.mean((test.salary_hike - test_pred)**2))

print("\nTrain RMSE:", train_rmse)
print("Test RMSE :", test_rmse)

#40.994
#19.554
#########################################
#Business Impact of the Project
###############################
'''
lories Consumed vs Weight Gained Analysis
1️ Dat0a'-Driven Diet Planning
The mod'el shows a strong positive relationship between calorie intake and weight gain.
About 80–90% of weight variation is explained by calories.
Enables nutritionists to predict expected weight gain for a given calorie intake.
Helps design personalized calorie-controlled diet plans.

2️ Obesity Risk Identification
Individuals consuming higher calories are statistically more likely to gain more weight.
High-risk calorie thresholds can be identified using CDF analysis.
Supports early intervention programs for obesity prevention.

3️ Preventive Healthcare Strategy
Healthcare providers can estimate:
How much weight gain may occur
What calorie limit keeps weight stable
 Reduces risk of:
Diabetes
Hypertension
Cardiovascular diseases

4️ Fitness & Wellness Industry Application
Gyms and wellness apps can:
Predict weight gain/loss trends
Provide calorie recommendations
Personalize fitness targets
'''
##############################################################


#dataset 3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# step 2
#load dataset
df=pd.read_csv("C:/Assignment/Simple linear regression/SAT_GPA (2).csv")
df.columns=["Sat_score","Gpa"]
print("First 5 Rows:\n",df.head())

#step3 basic EDA
print("\nData types:\n",df.dtypes)
print("\nSummary Statistics:\n",df.describe())

#business moment decision

#mean 
print("\nMean:\n",df.mean())
'''
Inference:
357.714
2340.714
Average calorie intake represents typical daily consumption. 
Average weight gain shows normal gain pattern. 
If both means are high + population Likely in calorie surptus. 
Indicates calories may be contributing to weight gain.
'''
#variance
print("\nVariance:\n",df.var())
'''
Inference:

High variance in calories rent eating habits.
High variance in weight gain metabolic differences. 
Larger spread means predictions may vary across individu
'''
#standard deviation 
print("\nStandard Deviation:\n",df.std())
'''
Inference:
Shows average deviation from mean,
Lower value stable population behavior.
Higher value → more fluctuation in diet and weight gain
'''

#skewness 
print("\nSkewness:\n",df.skew())
'''
Inference:

Skew = 0 Symmetric distribution.
Positive skew few individuals consume very high calories.
Positive skew in weight cal consumtion too → few individuals gain extreme we
'''
#Kurtosis
print("\nKurtosis:\n",cal.kurtosis())
'''
Inference:

High kurtosis → presence of extreme values.
Low kurtosis → uniform spread.
Extreme calorie or wetght values may influence regression
'''
#correlation
print("\ncorrelation matrix:\n",np.corrcoef(df.Sat_score,df.Gpa))
#

#step 4 univariate analysis

#histogram- weight gained
plt.figure(figsize=(6,4))
plt.hist(df.Sat_score)
plt.title("sat score Distribution")
plt.xlabel("sat score")
plt.ylabel("Frequency")
plt.show()
'''
Inference
Most individuals gained Lower to moderate weight (clustered in the Lower range 
The distribution appears positively skewed (right-skewed). 
A few individuals show very high weight gain, creating a long right tail.
These extreme values may act as outliers and can influence regresston results.
'''
#histogram - calories consumed
plt.figure(figsize=(6,4))
plt.hist(df.Gpa)
plt.title("Gpa Distribution")
plt.xlabel("Gpa score")
plt.ylabel("Frequency")
plt.show()
'''
Inference:

Calorie intake is spread across a moderate to high range.
Most individuals consume calories within a normal daily intake band. 
The distribution shows a slight right skew, indicating a few individuals consu 
Presence of high-calorie values suggests potential overconsumption cases.
'''
#Box plot(outlier Detection)
plt.figure(figsize=(8, 5))
sns.boxplot(data=df[['Sat_score', 'Gpa']], orient='h')
plt.title("Boxplot of Numerical Features")
plt.show()
'''
Inference:

The data points Lie within the whisters- no extrene outtiers detected 
Colortes consumed has a wider range compared to weight gained, 
Hediam values eppeur centrally pesitiened, inficating stable distritutions
'''
#bivariate analysis(scatter plot)
plt.figure(figsize=(6,4))
sns.scatterplot(x='Sat_score', y='Gpa', data=df)
plt.title("Sat_score vs Gpa")
plt.xlabel("sat_score")
plt.ylabel("gpa")
plt.show()
'''
Inference:

Clear positive Linear relationship observed.
As calories consumed increase, weight gained also increases. 
Data points follow an upward trend, indicating a strong correlation. 
No major irregular patterns or clustering observed,
'''
#correlation heatmap
plt.figure(figsize=(5,4))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()
'''
Inference:

The correlation between calòries consumed and weight gained is 0.95, which ina 
This means as calorie intake increases, weight gain increases significantly. 
The value is close to +1, showing a strong Linegr association. 
No negative relationship observed. "
'''
# pdf and cdf analysis
for col in ['Sat_score', 'Gpa']: 
    plt.figure(figsize=(12,4))

# PDF
    plt.subplot(1,2,1)
    sns.kdeplot(df[col], fill=True)
    plt.title(f'PDF of {col}')

# CDF
    plt.subplot(1,2,2)
    sorted_vals = np.sort(df[col])
    y = np.arange(len(sorted_vals))/len(sorted_vals)
    plt.plot(sorted_vals, y)
    plt.title(f'CDF of (col)')
    plt.show()


#########################################################
# Data Preprocessing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from scipy.stats import skew
from feature_engine.outliers import Winsorizer

#STEP 2: LOAD DATASET
df = pd.read_csv("C:/Assignment/Simple linear regression/SAT_GPA (2).csv") 
df.columns = ["Sat_score", "gpa"]
print("Initial Shape;", df.shape) 
print(df.head())

# step 3 basic cleaning

print("\nMissing Values Before treatment:\n", df.isnull().sum())

'''
inference :
    dataset contains only numerical variables
    no identifier column present
    if missing values exit - must be handle
    if zero - dataset is clean
'''
#STEP 4: MISSING VALUE TREATMENT if applicable
# Using Median Imputation (robust to skewness)

for col in df.columns: 
    df[col].fillna(df[col].median(), inplace=True)

print("\nMissing Values After Treatment:\n", df.isnull().sum())

#step 5 duplicate removal if aplicabel

cal.drop_duplicates(inplace=True)
print("\nShape after removing duplicates :",df.shape)

'''
inference:
    removes repeated observations
    prevents model from learning duplicated patterns
    improves generalization capability
    '''

#step6 outlier detection

plt.figure(figsize=(8, 5))
sns.boxplot(data=df,orient='h')
plt.title("Boxplot before treatment")
plt.show()    
    
#step 7 outlier treatment (winsorization if applicabel)

winsor = Winsorizer(
    capping_method='iqr',
    tail='both',
    fold=1.5,
    variables=['Sat_score','gpa']
   )
df[['Sat_score','gpa']] = winsor.fit_transform(
    df[['Sat_score', 'gpa']]
)

plt.figure(figsize=(8,5))
sns.boxplot(data=df, orient= 'h')
plt.title("Boxplot After Winsorization") 
plt.show()

'''
Inference:

Extreme values capped using IQR method.)   
'''

#step 8 skewness check
print("\nSkewness:\n",df.skew())

'''
Inference:
Skewness > 1→ Strong skew (Log transformation may help) 
Mild skew transformation optional.
Helps decide model transformation stage.

'''

# FINAL PREPROCESSING SUMMARY
'''
-Dataset validated and cleaned,
-Missing values handled using median.
-Duplicates removed,
-Outliers treated using IQR-based Winsorization
'''

#################################################################

#model development- simple linear regression 
# let us apply to various models and check the  feasibility

import statsmodels.formula.api as snf
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression

# 1 SIMPLE LINEAR REGRESSION

model1 = snf.ols('Sat_score ~ gpa', data=df).fit() 
pred1 = model1.predict(df)
rmse1 = np.sqrt(np.mean((df.Sat_score - pred1)**2))
print("SLR RMSE:", rmse1)
#166.770
model1.summary()
'''
#R-squared = 0.897 > 0.80, Model is very strong
#p = 0 < 0.05 hence acceptable
#beta-0 = -625.75
#beta-1 = 0.4202
Goal of the Model
We are trying to predict wt_gained (Dependent Variable)
using cal_consumed (Independent Vartable),

1. Model Fit (Goodness of Fit)
R-squared = 0.897(applicable for MLR) 
"Adjusted R2 tells us whether adding more variables truly improves the model 
→ About 89.7% of the variation in wt_gained is explained by cal consumed.
This means the model fits the data very well.
Adjusted R-squared = 0.888
→ Adjusted for number of predictors; still very high
Since there is only one predictor, overfitting is not a concern.

purpose of F-statistic
Does the independent variable(s) collectively explain the dependent variable? 
Or is the relationship happening just by chance?
F-statistic = 104.3
An F-value of 104.3 is very Large.
Model is statistically significant.
It performs much better than a model with no predictor.
Calories consumed significantly explains weight gain.

2. Coefficient Interpretation
Variable Coefficient Interpretation
Intercept -625.75 When calories = 0, predicted weight gain is -625g (not 
                                                                     cal_consumed +0.4202 For every 1 unit increase in calories, weight increases
P-value for cal consumed = 0.000
Highly statistically significant.

This confirms:
Higher calorie intake Leads to higher weight gain.

3. Residual Analysis

The Durbin-Watson statistic checks whether residuals are independent,

DW Value Meaning
= 2 No autocorrelation (Ideal)
< 1.5 Positive autocorrelation
1.5-2.5 Acceptable

Durbin-Watson = 2.537

Slightly above 2 but still acceptable.
No serious autocorrelation problem.

NormaLity Check

Jarque-Bera p-value = 0.541 (> 0.05) 
Residuals are approximately normally distributed. 
Regression assumption satisfied.

'''
#LOG Model(logx)
#model2
model2 = snf.ols('Sat_score ~ np.log(gpa)', data=df).fit()
pred2 = model2.predict(df)

rmse2 = np.sqrt(np.mean((df.Sat_score - pred2)**2))

print("Log-X Model RMSE:", rmse2)

#166.74
model2.summary()
'''
#R-squared = 0.808 = 0.8, 
there is scope for improvement #p = 0.000 < 0.05 hence acceptable

F-statistic = 50.40
Prob(F) = 1.25e-05 (< 0.05)

Model is statistically significant.
The Log transformation of calories significantly explains weight gain. 
The model performs much better than a model with no predictor.

Coefficient Interpretation
Intercept = -6955.65
When Log(calories) = 0, predicted weight gain is -6955.65 (not practically mea

Log(cal_consumed) = +948.37
For every 1 unit increase in Log(calories), weight increases by 948.37 units. 
Strong positive relationship.

P-value for Log(cal_consumed) = 0.000
Highly statistically significant.


This confirms:
Higher calorie intake (even after Log transformation) leads to higher weight g

Residual Analysis

Durbin-watson = 2.438
→ Lies within acceptable range (1.5-2.5). 
serious autocorrelation problem.

Normality Check

Jarque-Bera p-value = 0.566 (> 0.05)
Residuals are approximately normally distributed.
Regression assumptions are satisfied.

Final Comparison Insight
Although the model is statistically significant and explains about 81% of the
In One Sentence
Log(calories) has a statistically significant positive impact on weight gained
'''
#3.EXPONENTIAL MODEL (log y)
model3 = snf.ols('np.log(Sat_score) ~ gpa', data=df).fit()
pred3 = model3.predict(df)
# Convert predicted log values back using exp()
pred_3 = np.exp(pred3)
rmse3 = np.sqrt(np.mean((df.Sat_score - pred_3) ** 2))
print("Exponential Model RMSE:", rmse3)
#169.66
model3.summary()
'''
Inference
R-squared = 0.878 > 0.80, Model is strong
#p = 0.00 < 0.05 hence acceptable
#beta-0 = 2.8387
#beta-1 = 0.0011
Goal of the Model
We are trying to predict log(wt_gained) (Dependent Variable) using cal_consume
Model Fit (Goodness of Fit)
R-squared = 0.878 → About 87.8% of the variation in Log(wt gained) is explained by cal consumed.
'''

# 4 POLYNOMIAL MODEL
model4 = snf.ols(
    'np.log(Sat_score) ~ gpa + I(gpa**2)',
    data=df
).fit()

pred4 = np.exp(model4.predict(df))
rmse4 = np.sqrt(np.mean((df.Sat_score - pred4)**2))
print("Polynomial Model RMSE:", rmse4)
#169.49
model4. summary()

'''
#R-squared = 0.878 > 0.85, Model is strong
#Adjusted R-squared = 0.855 (slightly reduced after adding extra term) 
#p (F-statistic) = 9.61e-06 < 0.05 hence overall model acceptable
#beta-0 = 2.8287
#beta-1 = 0.0011
#beta-2 = -1.675e-09

Goal of the Model
test 2325.py X Hypothels testing_simulation cade 2125.py X 2testpy X chi squzre_test 2025.py X Unear Regression calory 2026.py X Linear_Ragreson Celory 2006 finalgy X

The polynomial term does NOT improve the model.

The relationship remains primarily Linear.

Residual Analysis

Durbin-Watson = 3.131
Greater than 2.5
Possible negative autocorrelation present,

Normality Check
Jarque-Bera p-value = 0.0466 (< 0.05)
Residuals are not perfectly normally distributed.

Final Interpretation
Although the polynomial model has high R2 (0.878), the squared term is complete
"The polynomial model explains about 88% of the variation in Log(weight gainea

'''
##################################
#Model Comparison
results = pd.DataFrame({

     "Model": ["SLR", "Log-X", "Exponential", "Polynomial"],
     "RMSE": [rmse1, rmse2, rmse3, rmse4],
     "R_squared": [model1.rsquared,
                   model2.rsquared,
                   model3.rsquared,
                   model4.rsquared
     ]
})

print("\nModel Comparison:\n", results)

#######################
#SELECT BEST MODEL

best_model_name = results.sort_values("RMSE").iloc[0]["Model"]
print("\nBest Model Based on RMSE:", best_model_name)

# TRAIN-TEST VALIDATION USING BEST MODEL (SLR IS BEST HERE)

train, test = train_test_split(df, test_size=0.3, random_state=42)

# Since SLR has highest R2 (0.897) and lowest RMSE, choose model1 
final_model = snf.ols('Sat_score ~ gpa', data=train).fit()

train_pred = final_model.predict(train)
test_pred = final_model.predict(test)

train_rmse = np.sqrt(np.mean((train.Sat_score - train_pred)**2)) 
test_rmse = np.sqrt(np.mean((test.Sat_score - test_pred)**2))

print("\nTrain RMSE:", train_rmse)
print("Test RMSE :", test_rmse)
#########################################
#Business Impact of the Project
###############################
'''
Calories Consumed vs Weight Gained Analysis
1️ Data-Driven Diet Planning
The model shows a strong positive relationship between calorie intake and weight gain.
About 80–90% of weight variation is explained by calories.
Enables nutritionists to predict expected weight gain for a given calorie intake.
Helps design personalized calorie-controlled diet plans.

2️ Obesity Risk Identification
Individuals consuming higher calories are statistically more likely to gain more weight.
High-risk calorie thresholds can be identified using CDF analysis.
Supports early intervention programs for obesity prevention.

3️ Preventive Healthcare Strategy
Healthcare providers can estimate:
How much weight gain may occur
What calorie limit keeps weight stable
 Reduces risk of:
Diabetes
Hypertension
Cardiovascular diseases

4️ Fitness & Wellness Industry Application
Gyms and wellness apps can:
Predict weight gain/loss trends
Provide calorie recommendations
Personalize fitness targets
'''
#####################################################################

#dataset 4

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# step 2
#load dataset
df=pd.read_csv("C:/Assignment/Simple linear regression/delivery_time (1).csv")
df.columns=["delivery_time","sorting_time"]
print("First 5 Rows:\n",df.head())

#step3 basic EDA
print("\nData types:\n",df.dtypes)
print("\nSummary Statistics:\n",df.describe())

#business moment decision

#mean 
print("\nMean:\n",df.mean())
'''
Inference:
16.790
6.190
If both means are high delivery time. 
'''
#variance
print("\nVariance:\n",df.var())
'''
Inference:

High variance in delivery time.
'''
#standard deviation 
print("\nStandard Deviation:\n",df.std())
'''
Inference:
'''

#skewness 
print("\nSkewness:\n",df.skew())
'''
Inference:

Skew = 0 Symmetric distribution.
Positive skew few individuals consume very high time.
'''
#Kurtosis
print("\nKurtosis:\n",df.kurtosis())
'''
Inference:

High kurtosis → presence of extreme values.
Low kurtosis → uniform spread.
'''
#correlation
print("\ncorrelation matrix:\n",np.corrcoef(df.delivery_time,df.sorting_time))
#

#step 4 univariate analysis

#histogram- weight gained
plt.figure(figsize=(6,4))
plt.hist(df.delivery_time)
plt.title("delivery time Distribution")
plt.xlabel("delivery time")
plt.ylabel("Frequency")
plt.show()
'''
Inference
Most individuals gained Lower to moderate weight (clustered in the Lower range 
The distribution appears positively skewed (right-skewed). 
A few individuals show very high weight gain, creating a long right tail.
These extreme values may act as outliers and can influence regresston results.
'''
#histogram - calories consumed
plt.figure(figsize=(6,4))
plt.hist(df.sorting_time)
plt.title("sorting time Distribution")
plt.xlabel("sorting time")
plt.ylabel("Frequency")
plt.show()
'''
Inference:

Calorie intake is spread across a moderate to high range.
Most individuals consume calories within a normal daily intake band. 
The distribution shows a slight right skew, indicating a few individuals consu 
Presence of high-calorie values suggests potential overconsumption cases.
'''
#Box plot(outlier Detection)
plt.figure(figsize=(8, 5))
sns.boxplot(data=df[['delivery_time', 'sorting_time']], orient='h')
plt.title("Boxplot of Numerical Features")
plt.show()
'''
Inference:

The data points Lie within the whisters- no extrene outtiers detected 
Colortes consumed has a wider range compared to weight gained, 
Hediam values eppeur centrally pesitiened, inficating stable distritutions
'''
#bivariate analysis(scatter plot)
plt.figure(figsize=(6,4))
sns.scatterplot(x='delivery_time', y='sorting_time', data=df)
plt.title("delivery_time vs sorting_time")
plt.xlabel("delivery_time")
plt.ylabel("sorting_time")
plt.show()
'''
Inference:

Clear positive Linear relationship observed.
As calories consumed increase, weight gained also increases. 
Data points follow an upward trend, indicating a strong correlation. 
No major irregular patterns or clustering observed,
'''
#correlation heatmap
plt.figure(figsize=(5,4))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()
'''
Inference:

The correlation between calòries consumed and weight gained is 0.95, which ina 
This means as calorie intake increases, weight gain increases significantly. 
The value is close to +1, showing a strong Linegr association. 
No negative relationship observed. "
'''
# pdf and cdf analysis
for col in ['delivery_time', 'sorting_time']: 
    plt.figure(figsize=(12,4))

# PDF
    plt.subplot(1,2,1)
    sns.kdeplot(df[col], fill=True)
    plt.title(f'PDF of {col}')

# CDF
    plt.subplot(1,2,2)
    sorted_vals = np.sort(df[col])
    y = np.arange(len(sorted_vals))/len(sorted_vals)
    plt.plot(sorted_vals, y)
    plt.title(f'CDF of (col)')
    plt.show()


#########################################################
# Data Preprocessing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from scipy.stats import skew
from feature_engine.outliers import Winsorizer

#STEP 2: LOAD DATASET
df= pd.read_csv("C:/Assignment/Simple linear regression/delivery_time (1).csv") 
df.columns = ["delivery_time", "sorting_time"]
print("Initial Shape;", df.shape) 
print(df.head())

# step 3 basic cleaning

print("\nMissing Values Before treatment:\n", df.isnull().sum())

'''
inference :
    dataset contains only numerical variables
    no identifier column present
    if missing values exit - must be handle
    if zero - dataset is clean
'''
#STEP 4: MISSING VALUE TREATMENT if applicable
# Using Median Imputation (robust to skewness)

for col in df.columns: 
    df[col].fillna(df[col].median(), inplace=True)

print("\nMissing Values After Treatment:\n", df.isnull().sum())

#step 5 duplicate removal if aplicabel

df.drop_duplicates(inplace=True)
print("\nShape after removing duplicates :",df.shape)

'''
inference:
    removes repeated observations
    prevents model from learning duplicated patterns
    improves generalization capability
    '''

#step6 outlier detection

plt.figure(figsize=(8, 5))
sns.boxplot(data=df,orient='h')
plt.title("Boxplot before treatment")
plt.show()    
    
#step 7 outlier treatment (winsorization if applicabel)

winsor = Winsorizer(
    capping_method='iqr',
    tail='both',
    fold=1.5,
    variables=['delivery_time','sorting_time']
   )
df[['delivery_time','sorting_time']] = winsor.fit_transform(
    df[['delivery_time', 'sorting_time']]
)

plt.figure(figsize=(8,5))
sns.boxplot(data=df, orient= 'h')
plt.title("Boxplot After Winsorization") 
plt.show()

'''
Inference:

Extreme values capped using IQR method.)   
'''

#step 8 skewness check
print("\nSkewness:\n",df.skew())

'''
Inference:
Skewness > 1→ Strong skew (Log transformation may help) 
Mild skew transformation optional.
Helps decide model transformation stage.

'''

# FINAL PREPROCESSING SUMMARY
'''
-Dataset validated and cleaned,
-Missing values handled using median.
-Duplicates removed,
-Outliers treated using IQR-based Winsorization
'''

#################################################################

#model development- simple linear regression 
# let us apply to various models and check the  feasibility

import statsmodels.formula.api as snf
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression

# 1 SIMPLE LINEAR REGRESSION

model1 = snf.ols('delivery_time ~ sorting_time', data=df).fit() 
pred1 = model1.predict(df)
rmse1 = np.sqrt(np.mean((df.delivery_time - pred1)**2))
print("SLR RMSE:", rmse1)
#2.791
model1.summary()
'''
#R-squared = 0.897 > 0.80, Model is very strong
#p = 0 < 0.05 hence acceptable
#beta-0 = -625.75
#beta-1 = 0.4202
Goal of the Model
We are trying to predict wt_gained (Dependent Variable)
using cal_consumed (Independent Vartable),

1. Model Fit (Goodness of Fit)
R-squared = 0.897(applicable for MLR) 
"Adjusted R2 tells us whether adding more variables truly improves the model 
→ About 89.7% of the variation in wt_gained is explained by cal consumed.
This means the model fits the data very well.
Adjusted R-squared = 0.888
→ Adjusted for number of predictors; still very high
Since there is only one predictor, overfitting is not a concern.

purpose of F-statistic
Does the independent variable(s) collectively explain the dependent variable? 
Or is the relationship happening just by chance?
F-statistic = 104.3
An F-value of 104.3 is very Large.
Model is statistically significant.
It performs much better than a model with no predictor.
Calories consumed significantly explains weight gain.

2. Coefficient Interpretation
Variable Coefficient Interpretation
Intercept -625.75 When calories = 0, predicted weight gain is -625g (not 
                                                                     cal_consumed +0.4202 For every 1 unit increase in calories, weight increases
P-value for cal consumed = 0.000
Highly statistically significant.

This confirms:
Higher calorie intake Leads to higher weight gain.

3. Residual Analysis

The Durbin-Watson statistic checks whether residuals are independent,

DW Value Meaning
= 2 No autocorrelation (Ideal)
< 1.5 Positive autocorrelation
1.5-2.5 Acceptable

Durbin-Watson = 2.537

Slightly above 2 but still acceptable.
No serious autocorrelation problem.

NormaLity Check

Jarque-Bera p-value = 0.541 (> 0.05) 
Residuals are approximately normally distributed. 
Regression assumption satisfied.

'''
#LOG Model(logx)
#model2
model2 = snf.ols('delivery_time ~ np.log(sorting_time)', data=df).fit()
pred2 = model2.predict(df)

rmse2 = np.sqrt(np.mean((df.delivery_time - pred2)**2))

print("Log-X Model RMSE:", rmse2)

#2.733
model2.summary()
'''
#R-squared = 0.808 = 0.8, 
there is scope for improvement #p = 0.000 < 0.05 hence acceptable

F-statistic = 50.40
Prob(F) = 1.25e-05 (< 0.05)

Model is statistically significant.
The Log transformation of calories significantly explains weight gain. 
The model performs much better than a model with no predictor.

Coefficient Interpretation
Intercept = -6955.65
When Log(calories) = 0, predicted weight gain is -6955.65 (not practically mea

Log(cal_consumed) = +948.37
For every 1 unit increase in Log(calories), weight increases by 948.37 units. 
Strong positive relationship.

P-value for Log(cal_consumed) = 0.000
Highly statistically significant.


This confirms:
Higher calorie intake (even after Log transformation) leads to higher weight g

Residual Analysis

Durbin-watson = 2.438
→ Lies within acceptable range (1.5-2.5). 
serious autocorrelation problem.

Normality Check

Jarque-Bera p-value = 0.566 (> 0.05)
Residuals are approximately normally distributed.
Regression assumptions are satisfied.

Final Comparison Insight
Although the model is statistically significant and explains about 81% of the
In One Sentence
Log(calories) has a statistically significant positive impact on weight gained
'''
#3.EXPONENTIAL MODEL (log y)
model3 = snf.ols('np.log(delivery_time) ~ sorting_time', data=df).fit()
pred3 = model3.predict(df)
# Convert predicted log values back using exp()
pred_3 = np.exp(pred3)
rmse3 = np.sqrt(np.mean((df.delivery_time - pred_3) ** 2))
print("Exponential Model RMSE:", rmse3)
#2.940
model3.summary()
'''
Inference
R-squared = 0.878 > 0.80, Model is strong
#p = 0.00 < 0.05 hence acceptable
#beta-0 = 2.8387
#beta-1 = 0.0011
Goal of the Model
We are trying to predict log(wt_gained) (Dependent Variable) using cal_consume
Model Fit (Goodness of Fit)
R-squared = 0.878 → About 87.8% of the variation in Log(wt gained) is explained by cal consumed.
'''

# 4 POLYNOMIAL MODEL
model4 = snf.ols(
    'np.log(delivery_time) ~ sorting_time + I(sorting_time**2)',
    data=df
).fit()

pred4 = np.exp(model4.predict(df))
rmse4 = np.sqrt(np.mean((df.delivery_time - pred4)**2))
print("Polynomial Model RMSE:", rmse4)
#2.799
model4. summary()

'''
#R-squared = 0.878 > 0.85, Model is strong
#Adjusted R-squared = 0.855 (slightly reduced after adding extra term) 
#p (F-statistic) = 9.61e-06 < 0.05 hence overall model acceptable
#beta-0 = 2.8287
#beta-1 = 0.0011
#beta-2 = -1.675e-09

Goal of the Model
test 2325.py X Hypothels testing_simulation cade 2125.py X 2testpy X chi squzre_test 2025.py X Unear Regression calory 2026.py X Linear_Ragreson Celory 2006 finalgy X

The polynomial term does NOT improve the model.

The relationship remains primarily Linear.

Residual Analysis

Durbin-Watson = 3.131
Greater than 2.5
Possible negative autocorrelation present,

Normality Check
Jarque-Bera p-value = 0.0466 (< 0.05)
Residuals are not perfectly normally distributed.

Final Interpretation
Although the polynomial model has high R2 (0.878), the squared term is complete
"The polynomial model explains about 88% of the variation in Log(weight gainea

'''
##################################
#Model Comparison
results = pd.DataFrame({

     "Model": ["SLR", "Log-X", "Exponential", "Polynomial"],
     "RMSE": [rmse1, rmse2, rmse3, rmse4],
     "R_squared": [model1.rsquared,
                   model2.rsquared,
                   model3.rsquared,
                   model4.rsquared
     ]
})

print("\nModel Comparison:\n", results)

#######################
#SELECT BEST MODEL

best_model_name = results.sort_values("RMSE").iloc[0]["Model"]
print("\nBest Model Based on RMSE:", best_model_name)

# TRAIN-TEST VALIDATION USING BEST MODEL (SLR IS BEST HERE)

train, test = train_test_split(df, test_size=0.3, random_state=42)

# Since SLR has highest R2 (0.897) and lowest RMSE, choose model1 
final_model = snf.ols('delivery_time ~ sorting_time', data=train).fit()

train_pred = final_model.predict(train)
test_pred = final_model.predict(test)

train_rmse = np.sqrt(np.mean((train.delivery_time - train_pred)**2)) 
test_rmse = np.sqrt(np.mean((test.delivery_time - test_pred)**2))

print("\nTrain RMSE:", train_rmse)
print("Test RMSE :", test_rmse)
#########################################
#Business Impact of the Project
###############################
'''
Calories Consumed vs Weight Gained Analysis
1️ Data-Driven Diet Planning
The model shows a strong positive relationship between calorie intake and weight gain.
About 80–90% of weight variation is explained by calories.
Enables nutritionists to predict expected weight gain for a given calorie intake.
Helps design personalized calorie-controlled diet plans.

2️ Obesity Risk Identification
Individuals consuming higher calories are statistically more likely to gain more weight.
High-risk calorie thresholds can be identified using CDF analysis.
Supports early intervention programs for obesity prevention.

3️ Preventive Healthcare Strategy
Healthcare providers can estimate:
How much weight gain may occur
What calorie limit keeps weight stable
 Reduces risk of:
Diabetes
Hypertension
Cardiovascular diseases

4️ Fitness & Wellness Industry Application
Gyms and wellness apps can:
Predict weight gain/loss trends
Provide calorie recommendations
Personalize fitness targets
'''
