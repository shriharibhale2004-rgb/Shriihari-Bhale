# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 14:41:53 2026

@author: shrih
"""

#Step1: Import Required Libraries
#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import statsmodels.api as smf
from statsmodels.stats.outliers_influence import variance_inflation_factor 
from statsmodels.tools.tools import add_constant
#
#Step2: LOAD THE DATASET
cars=pd.read_csv("C:/Linear Regression/Cars.csv")
print("First 5 Rows:\n", cars.head())
print("\nData Types:\n", cars.dtypes)
print("\nSummary Statistics:\n", cars.describe())
print("\nmissing values:\n", cars.isnull().sum())
#
#Business Moment Decisions
#MEAN
print("\nMean:\n", cars.mean())
'''
Inference
Mean:
 HP     117.469136
MPG     34.422076
VOL     98.765432
SP     121.540272
WT      32.412577
'''
#Variance
print("\nVariance:\n", cars.var())
'''
Inference
High variance in price - multiple segments (economy+luxury)
High variance in engine or hoesrpower - diverse product range
'''
#Std Dev
print("\nStd Dev:\n", cars.std())
'''
Inference
Shows spread around mean.
Higher std - less stability in feature values.
'''
#Skewness
print("\nSkewness:\n", cars.skew())
'''
Inference
Positive skew in price - few very expensive cars
Skewed variables may required log transform.
'''
#Kurtosis
print("\nKurtosis:\n", cars.kurtosis())
'''
Inference
High kurtosis - presence of extreme values.
extreme values may in regression influence.
'''
#
#UNIVARIATE ANALYSIS
#
cars.hist(figsize=(12,8))
plt.suptitle("Histogram of Numerical Features")
plt.show()
'''
Inference
HP (Horsepower)
Distribution is positively skewed (right-skewed).
Most cars have moderate horsepower (80-120 HP).
Few cars have very high HP, creating a long right tail.
Indicates presence of some high-performance vehicles.

2 MPG (Mileage)
Distribution appears approximately normal with slight skewness.
Most vehicles fall in the 25-40 MPG range.
Very Low and very high mileage cars are Limited.
Suggests balanced fuel efficiency across vehicles.

3 VOL (Engine Volume)
Slight right skewness observed.
Majority of cars have medium engine volume (80-120 range).
Few Large-engine vehicles exist.
Indicates mix of standard and heavy engine cars.

SP (Speed)
Distribution shows mild right skewness.
Most cars have speeds around 110-130.
Few high-speed vehicles extend the right tail.
Reflects presence of performance segment.

WT (Weight)
Distribution is slightly right-skewed.
Most cars weigh between 28-38 units.
Few heavier cars create upper tail.
Suggests majority are mid-weight vehicles.
'''

#BOX PLOT (OUTLIER DETECTION)
plt.figure(figsize=(12,6))
sns.boxplot(data=cars)
plt.xticks(rotation=45)
plt.title("Boxplot for outlier detection")
plt.show()
'''
Inference
Outlier detects in the all of the features of car
And only MPG has not outlier
'''
#
#Correlation Heatmap
#

plt.figure(figsize=(8,6))
sns.heatmap(cars.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
'''
Inference
'''
#
#PAIRPLOT (BIVARIATE ANALYSIS)
#
sns.pairplot(cars)
plt.show()
'''
Inference
Check linear relationship visually.
Detect non-linear patterns or clusters.
'''
#
#MULTICOLLINEARITY CHECK (VIF)
#
#Assuming 'Milage' is dependent variable
x=cars
x_const=add_constant(x)
'''
When checking multicollinearity for HP:
We run:
'''
vif_data=pd.DataFrame()
vif_data['Feature']=x_const.columns
vif_data['VIF']=[variance_inflation_factor(x_const.values, i)
                 for i in range(x_const.shape[1])]
print("\nvariance inflation factor:\n", vif_data)
'''
Inference
VIF>10-Severe multicollinearity
VIF 5-10-Moderate multicollinearity
Remove or combine variance if VIF high.
'''
########################################
#
#FIT MULTIPLE LINEAR REGRESSION MODEL
#
import statsmodels.api as sm
import scipy.stats as stats
import matplotlib.pyplot as plt
#Dependent Variable
y=cars['MPG']
#Independent Variables (remove MPG)
X=cars.drop(columns=['MPG'])
#Add constant (intercept)
X=sm.add_constant(X)
#Fit model
model=sm.OLS(y,X).fit()
print(model.summary())
#
#RESIDUAL ANALYSIS
#
residuals=model.resid
fitted_vals=model.fittedvalues
#Residual vs Fitted plot
plt.figure(figsize=(6,4))
plt.scatter(fitted_vals,residuals)
plt.axhline(0, color='red')
plt.xlabel("Fitted values")
plt.ylabel("Residuals")
plt.title('Fitted values vs Residuals')
plt.show()
'''
Inference
'''
#
#QQ PLOT (NORMALITY CHECK FOR RESIDUALS
plt.figure(figsize=(6,4))
stats.probplot(residuals, dist="norm", plot=plt)
plt.title("QQ PLOT - RESIDUALS")
plt.show()
'''
Inference
'''

#
#Step1: Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from scipy.stats import skew
from feature_engine.outliers import Winsorizer
#Step 2: Load Data
cars=pd.read_csv("C:/15-Regression/Cars.csv")
print("Initial Shape",cars.shape)
print(cars.head())
#Step 3 Baic Cleaning
print("\nData Types:\n", cars.dtypes)
print("\nMissing Values Before Treatment:\n", cars.isnull().sum())
'''
Inference
Dataset contains only numerical values
No categorical encoding required
If missing values exist - must be handled
MPG is target variables
''' 
#Step 4: Missing values treatment (Median Imputation)
for col in cars.columns:
    cars[col].fillna(cars[col].median(), inplace=True)
print("\nMissing Values After Treatment:\n", cars.isnull().sum())
'''
Inference
Median used beacause
Robust to outlier
Suitable for skwed numerical data
Prevents distortion of coefficients.
'''
#Step 5: Duplicate Removals
cars.drop_duplicates(inplace=True)
print("After removing duplicates:", cars.shape)
'''
Removes repeated vehicle records 
Prevents model bias 
Improves generalization capability.
'''

#Step 6: Outlier Detection
plt.figure(figsize=(8,5))
sns.boxplot(data=cars, orient='h')
plt.title("Boxplot Before Treatment")
plt.show()
'''
HP and SP show extreme values.
VOL and WT show strong correlation.
Outlier can distort regression coefficients.
'''
#Step 7: outlier treatment using winsorization
winsor = Winsorizer(
    capping_method='iqr',
    tail='both',
    fold=1.5,
    variables=list(cars.columns)
)

cars=winsor.fit_transform(cars)

plt.figure(figsize=(8,5))
sns.boxplot(data=cars, orient='h')
plt.title("Boxplt After Outlier Treatment ")
plt.show()
'''
Inference
Extreme values capped using IQR method.
Reduces impact of abnormal vehicles.
Improves regression stability.
'''
#Step 8: SKEWNESS CHECK
print("\nSkewness:\n", cars.skew())
'''
Inference
Skewness>1=Strong Skew (log transformation may help).
Mild skew=acceptable for regression
Helps decide transformation strategy.
'''
#Step 9: TRAIN_TEST_SPLIT
X=cars.drop(columns=['MPG'])
y=cars['MPG']
X_train,X_test,y_train,y_test=train_test_split(
    X,y, test_size=0.2, random_state=42
)
print("\nTraining Shape:", X_train.shape)
print("\nTesting Shape:", X_test.shape)
'''
Inference
80% data used for training.
20% data used for testing.
Ensures model generalization.
'''
#
#STEP 10: BUILD MULTIPLE LINEAR REGRESSION MODEL
#
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
#Combine training data into one dataframe for formula api
cars_train=pd.concat([X_train, y_train], axis=1)    
cars_test=pd.concat([X_test, y_test], axis=1)    
#Initial model with all predctors
ml1=smf.ols('MPG~HP+VOL+SP+WT', data=cars_train).fit()
print(ml1.summary())
'''
Inference
1 Model Strength 
R-Squared = 0.831
Model explains 83.1% of variation in MPG
This is a strong model fit.
Indicates predictirs collectively explain fuel efficiency well.

Adjusted R-Squared=0.820
very close to R-Square
 
Dep. Variable:                    MPG   R-squared:                       0.774
Model:                            OLS   Adj. R-squared:                  0.759
Method:                 Least Squares   F-statistic:                     50.55
Date:                Thu, 04 Jun 2026   Prob (F-statistic):           2.08e-18
Time:                        17:29:54   Log-Likelihood:                -182.24
No. Observations:                  64   AIC:                             374.5
Df Residuals:                      59   BIC:                             385.3
Df Model:                           4                                         
Covariance Type:            nonrobust  

Omnibus:                        2.900   Durbin-Watson:                   1.715
Prob(Omnibus):                  0.235   Jarque-Bera (JB):                2.067
Skew:                           0.391   Prob(JB):                        0.356
Kurtosis:                       3.403   Cond. No.                     6.17e+03        

Indicates:
Strong multicollinearity present
'''
# 
#STEP 11:MULTICOLLINEARITY CHECK (VIF)
#
#Calculating VIF manually
rsq_hp=smf.ols('HP~VOL+SP+WT', data=cars_train).fit().rsquared
vif_hp=1/(1-rsq_hp)                              

rsq_vol=smf.ols('HP~VOL+SP+WT', data=cars_train).fit().rsquared
vif_vol=1/(1-rsq_vol)                              

rsq_sp=smf.ols('HP~VOL+SP+WT', data=cars_train).fit().rsquared
vif_sp=1/(1-rsq_sp)                              

rsq_wt=smf.ols('HP~VOL+SP+WT', data=cars_train).fit().rsquared
vif_wt=1/(1-rsq_wt)                              

vif_frame=pd.DataFrame({
    'Variable':['HP','VOL','SP','WT'],
    'VIF':[vif_hp, vif_vol, vif_sp, vif_wt]
})
print('VIF Frame:', vif_frame)
#
#STEP 12: DROP HIGH VIF VARIABLE (Example: WT)
#
final_ml=smf.ols('MPG~HP+VOL+SP', data=cars_train).fit()
r2 = final_ml.rsquared
print("Summary:", final_ml)
#
#STEP 13:ASSUMPTION CHECKING
#
#Predictions 
train_pred=final_ml.predict(cars_train)
test_pred=final_ml.predict(cars_test)
#Residuals
residuals=final_ml.resid
#---QQ Plot----
sm.qqplot(residuals)
plt.title("QQ Plot - Residuals")
plt.show()
'''
Interpretation:
Residuals are approximately narmally distributed.
Minor tail deviations indicate presence of few mild outliers
'''
#
#Residuals vs Fitted
sns.residplot(x=train_pred, y=y_train, lowess=True)
plt.xlabel("Fitted Values")
plt.ylabel("Residuals")
plt.title("Residuals vs Fitted")
plt.show()
#
#STEP 14: MODEL EVALUATION (RMSE)
#
train_rmse=np.sqrt(np.mean((train_pred-y_train)**2))
test_rmse=np.sqrt(np.mean((test_pred-y_test)**2))
print("Train RMSE:", round(train_rmse,4))
print("Test RMSE:", round(test_rmse,4))
'''
Train RMSE < Test RMSE - Normal case
Train RMSE = Test RMSE - Ideal
Train RMSE >> Test RMSE - Underfitting
Train RMSE << Test RMSE - Overfitting
'''

'''
------------------------------------------------------------
BUSINESS IMPACT
------------------------------------------------------------
1️ Strategic Impact:
Enables automobile manufacturers to design vehicles aligned with fuel-efficiency regulations and sustainability goals.
Supports long-term R&D strategy by identifying performance–efficiency trade-offs.
Strengthens competitive positioning in markets where fuel economy is a key purchase driver.

2️ Financial Impact:

Reduction in fuel consumption improves product attractiveness, leading to higher sales.
Optimized engine and vehicle design reduces material and manufacturing costs (weight optimization).
Minimizes regulatory penalties related to emission and fuel economy standards.
Improves ROI on product development by focusing investment on high-impact features.

3️ Operational Impact:

Assists engineering teams in data-driven vehicle design decisions.
Reduces trial-and-error experimentation during prototype development.
Supports simulation-based testing instead of expensive physical testing.
Enables faster product development cycles using predictive modeling.

4️ Regulatory & Environmental Impact:

Helps manufacturers meet government fuel efficiency and emission norms.
Contributes to lower carbon footprint and environmental sustainability.
Aligns with global climate goals and green mobility initiatives.

️⃣ 5 Customer & Market Impact:

Provides customers with more fuel-efficient and cost-effective vehicles.
Improves brand reputation as an environmentally responsible manufacturer.
Enables data-backed marketing claims (e.g., optimized MPG performance).
Helps customers make informed purchasing decisions based on efficiency metrics.

6️ Analytical & Organizational Impact:

Promotes adoption of data-driven decision-making in automotive engineering.
Builds internal analytics capability within product design teams.
Creates foundation for advanced modeling (non-linear regression, ML models).
Enables continuous performance monitoring and improvement.

7️ Long-Term Impact:

Supports transition toward hybrid and electric vehicle optimization strategies.
Provides scalable modeling framework for future vehicle platforms.
Establishes predictive intelligence in product lifecycle management.
'''

################################################################################################



#dataset 2


#Step1: Import Required Libraries
#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import statsmodels.api as smf
from statsmodels.stats.outliers_influence import variance_inflation_factor 
from statsmodels.tools.tools import add_constant
#
#Step2: LOAD THE DATASET
df=pd.read_csv("C:/Assignment/multi linear rregression/Computer_Data (1).csv")
df=df.drop(["cd","multi","premium"],axis=1)
print("First 5 Rows:\n", df.head())
print("\nData Types:\n", df.dtypes)
print("\nSummary Statistics:\n", df.describe())
print("\nmissing values:\n", df.isnull().sum())
#
#Business Moment Decisions
#MEAN
print("\nMean:\n", df.mean())
'''
Inference
Mean:
 HP     117.469136
MPG     34.422076
VOL     98.765432
SP     121.540272
WT      32.412577
'''
#Variance
print("\nVariance:\n", df.var())
'''
Inference
High variance in price - multiple segments (economy+luxury)
High variance in engine or hoesrpower - diverse product range
'''
#Std Dev
print("\nStd Dev:\n", df.std())
'''
Inference
Shows spread around mean.
Higher std - less stability in feature values.
'''
#Skewness
print("\nSkewness:\n", df.skew())
'''
Inference
Positive skew in price - few very expensive cars
Skewed variables may required log transform.
'''
#Kurtosis
print("\nKurtosis:\n", df.kurtosis())
'''
Inference
High kurtosis - presence of extreme values.
extreme values may in regression influence.
'''
#
#UNIVARIATE ANALYSIS
#
df.hist(figsize=(12,8))
plt.suptitle("Histogram of Numerical Features")
plt.show()
'''
Inference
HP (Horsepower)
Distribution is positively skewed (right-skewed).
Most cars have moderate horsepower (80-120 HP).
Few cars have very high HP, creating a long right tail.
Indicates presence of some high-performance vehicles.

2 MPG (Mileage)
Distribution appears approximately normal with slight skewness.
Most vehicles fall in the 25-40 MPG range.
Very Low and very high mileage cars are Limited.
Suggests balanced fuel efficiency across vehicles.

3 VOL (Engine Volume)
Slight right skewness observed.
Majority of cars have medium engine volume (80-120 range).
Few Large-engine vehicles exist.
Indicates mix of standard and heavy engine cars.

SP (Speed)
Distribution shows mild right skewness.
Most cars have speeds around 110-130.
Few high-speed vehicles extend the right tail.
Reflects presence of performance segment.

WT (Weight)
Distribution is slightly right-skewed.
Most cars weigh between 28-38 units.
Few heavier cars create upper tail.
Suggests majority are mid-weight vehicles.
'''

#BOX PLOT (OUTLIER DETECTION)
plt.figure(figsize=(12,6))
sns.boxplot(data=df)
plt.xticks(rotation=45)
plt.title("Boxplot for outlier detection")
plt.show()
'''
Inference
Outlier detects in the all of the features of car
And only MPG has not outlier
'''
#
#Correlation Heatmap
#

plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
'''
Inference
'''
#
#PAIRPLOT (BIVARIATE ANALYSIS)
#
sns.pairplot(df)
plt.show()
'''
Inference
Check linear relationship visually.
Detect non-linear patterns or clusters.
'''
#
#MULTICOLLINEARITY CHECK (VIF)
#
#Assuming 'Milage' is dependent variable
x=df
x_const=add_constant(x)
'''
When checking multicollinearity for HP:
We run:
'''
vif_data=pd.DataFrame()
vif_data['Feature']=x_const.columns
vif_data['VIF']=[variance_inflation_factor(x_const.values, i)
                 for i in range(x_const.shape[1])]
print("\nvariance inflation factor:\n", vif_data)
'''
Inference
VIF>10-Severe multicollinearity
VIF 5-10-Moderate multicollinearity
Remove or combine variance if VIF high.
'''
########################################
#
#FIT MULTIPLE LINEAR REGRESSION MODEL
#
import statsmodels.api as sm
import scipy.stats as stats
import matplotlib.pyplot as plt
#Dependent Variable
y=df['speed']
#Independent Variables (remove MPG)
X=df.drop(columns=['speed'])
#Add constant (intercept)
X=sm.add_constant(X)
#Fit model
model=sm.OLS(y,X).fit()
print(model.summary())
#
#RESIDUAL ANALYSIS
#
residuals=model.resid
fitted_vals=model.fittedvalues
#Residual vs Fitted plot
plt.figure(figsize=(6,4))
plt.scatter(fitted_vals,residuals)
plt.axhline(0, color='red')
plt.xlabel("Fitted values")
plt.ylabel("Residuals")
plt.title('Fitted values vs Residuals')
plt.show()
'''
Inference
'''
#
#QQ PLOT (NORMALITY CHECK FOR RESIDUALS
plt.figure(figsize=(6,4))
stats.probplot(residuals, dist="norm", plot=plt)
plt.title("QQ PLOT - RESIDUALS")
plt.show()
'''
Inference
'''

#
#Step1: Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from scipy.stats import skew
from feature_engine.outliers import Winsorizer



#Step 2: Load Data
df=pd.read_csv("C:/Assignment/multi linear rregression/Computer_Data (1).csv")
df=df.drop(["cd","multi","premium"],axis=1)

print("Initial Shape",df.shape)
print(df.head())
#Step 3 Baic Cleaning
print("\nData Types:\n", df.dtypes)
print("\nMissing Values Before Treatment:\n", df.isnull().sum())
'''
Inference
Dataset contains only numerical values
No categorical encoding required
If missing values exist - must be handled
MPG is target variables
''' 
#Step 4: Missing values treatment (Median Imputation)
for col in df.columns:
    df[col].fillna(df[col].median(), inplace=True)
print("\nMissing Values After Treatment:\n", df.isnull().sum())
'''
Inference
Median used beacause
Robust to outlier
Suitable for skwed numerical data
Prevents distortion of coefficients.
'''
#Step 5: Duplicate Removals
df.drop_duplicates(inplace=True)
print("After removing duplicates:", df.shape)
'''
Removes repeated vehicle records 
Prevents model bias 
Improves generalization capability.
'''

#Step 6: Outlier Detection
plt.figure(figsize=(8,5))
sns.boxplot(data=df, orient='h')
plt.title("Boxplot Before Treatment")
plt.show()
'''
HP and SP show extreme values.
VOL and WT show strong correlation.
Outlier can distort regression coefficients.
'''
#Step 7: outlier treatment using winsorization
winsor = Winsorizer(
    capping_method='iqr',
    tail='both',
    fold=1.5,
    variables=list(df.columns)
)

cars=winsor.fit_transform(df)

plt.figure(figsize=(8,5))
sns.boxplot(data=df, orient='h')
plt.title("Boxplt After Outlier Treatment ")
plt.show()
'''
Inference
Extreme values capped using IQR method.
Reduces impact of abnormal vehicles.
Improves regression stability.
'''
#Step 8: SKEWNESS CHECK
print("\nSkewness:\n", df.skew())
'''
Inference
Skewness>1=Strong Skew (log transformation may help).
Mild skew=acceptable for regression
Helps decide transformation strategy.
'''
#Step 9: TRAIN_TEST_SPLIT
X=df.drop(columns=['speed'])
y=df['speed']
X_train,X_test,y_train,y_test=train_test_split(
    X,y, test_size=0.2, random_state=42
)
print("\nTraining Shape:", X_train.shape)
print("\nTesting Shape:", X_test.shape)
'''
Inference
80% data used for training.
20% data used for testing.
Ensures model generalization.
'''
#
#STEP 10: BUILD MULTIPLE LINEAR REGRESSION MODEL
#
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
#Combine training data into one dataframe for formula api
df_train=pd.concat([X_train, y_train], axis=1)    
df_test=pd.concat([X_test, y_test], axis=1)    
#Initial model with all predctors
ml1=smf.ols('price~speed+hd+ram+screen+ads', data=df_train).fit()
print(ml1.summary())
'''
Inference
1 Model Strength 
R-Squared = 0.831
Model explains 83.1% of variation in MPG
This is a strong model fit.
Indicates predictirs collectively explain fuel efficiency well.

Adjusted R-Squared=0.820
very close to R-Square
 
Dep. Variable:                    MPG   R-squared:                       0.774
Model:                            OLS   Adj. R-squared:                  0.759
Method:                 Least Squares   F-statistic:                     50.55
Date:                Thu, 04 Jun 2026   Prob (F-statistic):           2.08e-18
Time:                        17:29:54   Log-Likelihood:                -182.24
No. Observations:                  64   AIC:                             374.5
Df Residuals:                      59   BIC:                             385.3
Df Model:                           4                                         
Covariance Type:            nonrobust  

Omnibus:                        2.900   Durbin-Watson:                   1.715
Prob(Omnibus):                  0.235   Jarque-Bera (JB):                2.067
Skew:                           0.391   Prob(JB):                        0.356
Kurtosis:                       3.403   Cond. No.                     6.17e+03        

Indicates:
Strong multicollinearity present
'''
# 
#STEP 11:MULTICOLLINEARITY CHECK (VIF)
#
#Calculating VIF manually
rsq_hp=smf.ols('HP~VOL+SP+WT', data=cars_train).fit().rsquared
vif_hp=1/(1-rsq_hp)                              

rsq_vol=smf.ols('HP~VOL+SP+WT', data=cars_train).fit().rsquared
vif_vol=1/(1-rsq_vol)                              

rsq_sp=smf.ols('HP~VOL+SP+WT', data=cars_train).fit().rsquared
vif_sp=1/(1-rsq_sp)                              

rsq_wt=smf.ols('HP~VOL+SP+WT', data=cars_train).fit().rsquared
vif_wt=1/(1-rsq_wt)                              

vif_frame=pd.DataFrame({
    'Variable':['HP','VOL','SP','WT'],
    'VIF':[vif_hp, vif_vol, vif_sp, vif_wt]
})
print('VIF Frame:', vif_frame)
#
#STEP 12: DROP HIGH VIF VARIABLE (Example: WT)
#
final_ml=smf.ols('MPG~HP+VOL+SP', data=cars_train).fit()
r2 = final_ml.rsquared
print("Summary:", final_ml)
#
#STEP 13:ASSUMPTION CHECKING
#
#Predictions 
train_pred=final_ml.predict(cars_train)
test_pred=final_ml.predict(cars_test)
#Residuals
residuals=final_ml.resid
#---QQ Plot----
sm.qqplot(residuals)
plt.title("QQ Plot - Residuals")
plt.show()
'''
Interpretation:
Residuals are approximately narmally distributed.
Minor tail deviations indicate presence of few mild outliers
'''
#
#Residuals vs Fitted
sns.residplot(x=train_pred, y=y_train, lowess=True)
plt.xlabel("Fitted Values")
plt.ylabel("Residuals")
plt.title("Residuals vs Fitted")
plt.show()
#
#STEP 14: MODEL EVALUATION (RMSE)
#
train_rmse=np.sqrt(np.mean((train_pred-y_train)**2))
test_rmse=np.sqrt(np.mean((test_pred-y_test)**2))
print("Train RMSE:", round(train_rmse,4))
print("Test RMSE:", round(test_rmse,4))
'''
Train RMSE < Test RMSE - Normal case
Train RMSE = Test RMSE - Ideal
Train RMSE >> Test RMSE - Underfitting
Train RMSE << Test RMSE - Overfitting
'''
#########################################################

#dataset 3

#Step1: Import Required Libraries
#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import statsmodels.api as smf
from statsmodels.stats.outliers_influence import variance_inflation_factor 
from statsmodels.tools.tools import add_constant
#
#Step2: LOAD THE DATASET
cars=pd.read_csv("C:/Linear Regression/Cars.csv")
print("First 5 Rows:\n", cars.head())
print("\nData Types:\n", cars.dtypes)
print("\nSummary Statistics:\n", cars.describe())
print("\nmissing values:\n", cars.isnull().sum())
#
#Business Moment Decisions
#MEAN
print("\nMean:\n", cars.mean())
'''
Inference
Mean:
 HP     117.469136
MPG     34.422076
VOL     98.765432
SP     121.540272
WT      32.412577
'''
#Variance
print("\nVariance:\n", cars.var())
'''
Inference
High variance in price - multiple segments (economy+luxury)
High variance in engine or hoesrpower - diverse product range
'''
#Std Dev
print("\nStd Dev:\n", cars.std())
'''
Inference
Shows spread around mean.
Higher std - less stability in feature values.
'''
#Skewness
print("\nSkewness:\n", cars.skew())
'''
Inference
Positive skew in price - few very expensive cars
Skewed variables may required log transform.
'''
#Kurtosis
print("\nKurtosis:\n", cars.kurtosis())
'''
Inference
High kurtosis - presence of extreme values.
extreme values may in regression influence.
'''
#
#UNIVARIATE ANALYSIS
#
cars.hist(figsize=(12,8))
plt.suptitle("Histogram of Numerical Features")
plt.show()
'''
Inference
HP (Horsepower)
Distribution is positively skewed (right-skewed).
Most cars have moderate horsepower (80-120 HP).
Few cars have very high HP, creating a long right tail.
Indicates presence of some high-performance vehicles.

2 MPG (Mileage)
Distribution appears approximately normal with slight skewness.
Most vehicles fall in the 25-40 MPG range.
Very Low and very high mileage cars are Limited.
Suggests balanced fuel efficiency across vehicles.

3 VOL (Engine Volume)
Slight right skewness observed.
Majority of cars have medium engine volume (80-120 range).
Few Large-engine vehicles exist.
Indicates mix of standard and heavy engine cars.

SP (Speed)
Distribution shows mild right skewness.
Most cars have speeds around 110-130.
Few high-speed vehicles extend the right tail.
Reflects presence of performance segment.

WT (Weight)
Distribution is slightly right-skewed.
Most cars weigh between 28-38 units.
Few heavier cars create upper tail.
Suggests majority are mid-weight vehicles.
'''

#BOX PLOT (OUTLIER DETECTION)
plt.figure(figsize=(12,6))
sns.boxplot(data=cars)
plt.xticks(rotation=45)
plt.title("Boxplot for outlier detection")
plt.show()
'''
Inference
Outlier detects in the all of the features of car
And only MPG has not outlier
'''
#
#Correlation Heatmap
#

plt.figure(figsize=(8,6))
sns.heatmap(cars.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
'''
Inference
'''
#
#PAIRPLOT (BIVARIATE ANALYSIS)
#
sns.pairplot(cars)
plt.show()
'''
Inference
Check linear relationship visually.
Detect non-linear patterns or clusters.
'''
#
#MULTICOLLINEARITY CHECK (VIF)
#
#Assuming 'Milage' is dependent variable
x=cars
x_const=add_constant(x)
'''
When checking multicollinearity for HP:
We run:
'''
vif_data=pd.DataFrame()
vif_data['Feature']=x_const.columns
vif_data['VIF']=[variance_inflation_factor(x_const.values, i)
                 for i in range(x_const.shape[1])]
print("\nvariance inflation factor:\n", vif_data)
'''
Inference
VIF>10-Severe multicollinearity
VIF 5-10-Moderate multicollinearity
Remove or combine variance if VIF high.
'''
########################################
#
#FIT MULTIPLE LINEAR REGRESSION MODEL
#
import statsmodels.api as sm
import scipy.stats as stats
import matplotlib.pyplot as plt
#Dependent Variable
y=cars['MPG']
#Independent Variables (remove MPG)
X=cars.drop(columns=['MPG'])
#Add constant (intercept)
X=sm.add_constant(X)
#Fit model
model=sm.OLS(y,X).fit()
print(model.summary())
#
#RESIDUAL ANALYSIS
#
residuals=model.resid
fitted_vals=model.fittedvalues
#Residual vs Fitted plot
plt.figure(figsize=(6,4))
plt.scatter(fitted_vals,residuals)
plt.axhline(0, color='red')
plt.xlabel("Fitted values")
plt.ylabel("Residuals")
plt.title('Fitted values vs Residuals')
plt.show()
'''
Inference
'''
#
#QQ PLOT (NORMALITY CHECK FOR RESIDUALS
plt.figure(figsize=(6,4))
stats.probplot(residuals, dist="norm", plot=plt)
plt.title("QQ PLOT - RESIDUALS")
plt.show()
'''
Inference
'''

#
#Step1: Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from scipy.stats import skew
from feature_engine.outliers import Winsorizer
#Step 2: Load Data
cars=pd.read_csv("C:/15-Regression/Cars.csv")
print("Initial Shape",cars.shape)
print(cars.head())
#Step 3 Baic Cleaning
print("\nData Types:\n", cars.dtypes)
print("\nMissing Values Before Treatment:\n", cars.isnull().sum())
'''
Inference
Dataset contains only numerical values
No categorical encoding required
If missing values exist - must be handled
MPG is target variables
''' 
#Step 4: Missing values treatment (Median Imputation)
for col in cars.columns:
    cars[col].fillna(cars[col].median(), inplace=True)
print("\nMissing Values After Treatment:\n", cars.isnull().sum())
'''
Inference
Median used beacause
Robust to outlier
Suitable for skwed numerical data
Prevents distortion of coefficients.
'''
#Step 5: Duplicate Removals
cars.drop_duplicates(inplace=True)
print("After removing duplicates:", cars.shape)
'''
Removes repeated vehicle records 
Prevents model bias 
Improves generalization capability.
'''

#Step 6: Outlier Detection
plt.figure(figsize=(8,5))
sns.boxplot(data=cars, orient='h')
plt.title("Boxplot Before Treatment")
plt.show()
'''
HP and SP show extreme values.
VOL and WT show strong correlation.
Outlier can distort regression coefficients.
'''
#Step 7: outlier treatment using winsorization
winsor = Winsorizer(
    capping_method='iqr',
    tail='both',
    fold=1.5,
    variables=list(cars.columns)
)

cars=winsor.fit_transform(cars)

plt.figure(figsize=(8,5))
sns.boxplot(data=cars, orient='h')
plt.title("Boxplt After Outlier Treatment ")
plt.show()
'''
Inference
Extreme values capped using IQR method.
Reduces impact of abnormal vehicles.
Improves regression stability.
'''
#Step 8: SKEWNESS CHECK
print("\nSkewness:\n", cars.skew())
'''
Inference
Skewness>1=Strong Skew (log transformation may help).
Mild skew=acceptable for regression
Helps decide transformation strategy.
'''
#Step 9: TRAIN_TEST_SPLIT
X=cars.drop(columns=['MPG'])
y=cars['MPG']
X_train,X_test,y_train,y_test=train_test_split(
    X,y, test_size=0.2, random_state=42
)
print("\nTraining Shape:", X_train.shape)
print("\nTesting Shape:", X_test.shape)
'''
Inference
80% data used for training.
20% data used for testing.
Ensures model generalization.
'''
#
#STEP 10: BUILD MULTIPLE LINEAR REGRESSION MODEL
#
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
#Combine training data into one dataframe for formula api
cars_train=pd.concat([X_train, y_train], axis=1)    
cars_test=pd.concat([X_test, y_test], axis=1)    
#Initial model with all predctors
ml1=smf.ols('MPG~HP+VOL+SP+WT', data=cars_train).fit()
print(ml1.summary())
'''
Inference
1 Model Strength 
R-Squared = 0.831
Model explains 83.1% of variation in MPG
This is a strong model fit.
Indicates predictirs collectively explain fuel efficiency well.

Adjusted R-Squared=0.820
very close to R-Square
 
Dep. Variable:                    MPG   R-squared:                       0.774
Model:                            OLS   Adj. R-squared:                  0.759
Method:                 Least Squares   F-statistic:                     50.55
Date:                Thu, 04 Jun 2026   Prob (F-statistic):           2.08e-18
Time:                        17:29:54   Log-Likelihood:                -182.24
No. Observations:                  64   AIC:                             374.5
Df Residuals:                      59   BIC:                             385.3
Df Model:                           4                                         
Covariance Type:            nonrobust  

Omnibus:                        2.900   Durbin-Watson:                   1.715
Prob(Omnibus):                  0.235   Jarque-Bera (JB):                2.067
Skew:                           0.391   Prob(JB):                        0.356
Kurtosis:                       3.403   Cond. No.                     6.17e+03        

Indicates:
Strong multicollinearity present
'''
# 
#STEP 11:MULTICOLLINEARITY CHECK (VIF)
#
#Calculating VIF manually
rsq_hp=smf.ols('HP~VOL+SP+WT', data=cars_train).fit().rsquared
vif_hp=1/(1-rsq_hp)                              

rsq_vol=smf.ols('HP~VOL+SP+WT', data=cars_train).fit().rsquared
vif_vol=1/(1-rsq_vol)                              

rsq_sp=smf.ols('HP~VOL+SP+WT', data=cars_train).fit().rsquared
vif_sp=1/(1-rsq_sp)                              

rsq_wt=smf.ols('HP~VOL+SP+WT', data=cars_train).fit().rsquared
vif_wt=1/(1-rsq_wt)                              

vif_frame=pd.DataFrame({
    'Variable':['HP','VOL','SP','WT'],
    'VIF':[vif_hp, vif_vol, vif_sp, vif_wt]
})
print('VIF Frame:', vif_frame)
#
#STEP 12: DROP HIGH VIF VARIABLE (Example: WT)
#
final_ml=smf.ols('MPG~HP+VOL+SP', data=cars_train).fit()
r2 = final_ml.rsquared
print("Summary:", final_ml)
#
#STEP 13:ASSUMPTION CHECKING
#
#Predictions 
train_pred=final_ml.predict(cars_train)
test_pred=final_ml.predict(cars_test)
#Residuals
residuals=final_ml.resid
#---QQ Plot----
sm.qqplot(residuals)
plt.title("QQ Plot - Residuals")
plt.show()
'''
Interpretation:
Residuals are approximately narmally distributed.
Minor tail deviations indicate presence of few mild outliers
'''
#
#Residuals vs Fitted
sns.residplot(x=train_pred, y=y_train, lowess=True)
plt.xlabel("Fitted Values")
plt.ylabel("Residuals")
plt.title("Residuals vs Fitted")
plt.show()
#
#STEP 14: MODEL EVALUATION (RMSE)
#
train_rmse=np.sqrt(np.mean((train_pred-y_train)**2))
test_rmse=np.sqrt(np.mean((test_pred-y_test)**2))
print("Train RMSE:", round(train_rmse,4))
print("Test RMSE:", round(test_rmse,4))
'''
Train RMSE < Test RMSE - Normal case
Train RMSE = Test RMSE - Ideal
Train RMSE >> Test RMSE - Underfitting
Train RMSE << Test RMSE - Overfitting
'''
##################################################################


#dataset 4
#Step1: Import Required Libraries
#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import statsmodels.api as smf
from statsmodels.stats.outliers_influence import variance_inflation_factor 
from statsmodels.tools.tools import add_constant
#
#Step2: LOAD THE DATASET
cars=pd.read_csv("C:/Linear Regression/Cars.csv")
print("First 5 Rows:\n", cars.head())
print("\nData Types:\n", cars.dtypes)
print("\nSummary Statistics:\n", cars.describe())
print("\nmissing values:\n", cars.isnull().sum())
#
#Business Moment Decisions
#MEAN
print("\nMean:\n", cars.mean())
'''
Inference
Mean:
 HP     117.469136
MPG     34.422076
VOL     98.765432
SP     121.540272
WT      32.412577
'''
#Variance
print("\nVariance:\n", cars.var())
'''
Inference
High variance in price - multiple segments (economy+luxury)
High variance in engine or hoesrpower - diverse product range
'''
#Std Dev
print("\nStd Dev:\n", cars.std())
'''
Inference
Shows spread around mean.
Higher std - less stability in feature values.
'''
#Skewness
print("\nSkewness:\n", cars.skew())
'''
Inference
Positive skew in price - few very expensive cars
Skewed variables may required log transform.
'''
#Kurtosis
print("\nKurtosis:\n", cars.kurtosis())
'''
Inference
High kurtosis - presence of extreme values.
extreme values may in regression influence.
'''
#
#UNIVARIATE ANALYSIS
#
cars.hist(figsize=(12,8))
plt.suptitle("Histogram of Numerical Features")
plt.show()
'''
Inference
HP (Horsepower)
Distribution is positively skewed (right-skewed).
Most cars have moderate horsepower (80-120 HP).
Few cars have very high HP, creating a long right tail.
Indicates presence of some high-performance vehicles.

2 MPG (Mileage)
Distribution appears approximately normal with slight skewness.
Most vehicles fall in the 25-40 MPG range.
Very Low and very high mileage cars are Limited.
Suggests balanced fuel efficiency across vehicles.

3 VOL (Engine Volume)
Slight right skewness observed.
Majority of cars have medium engine volume (80-120 range).
Few Large-engine vehicles exist.
Indicates mix of standard and heavy engine cars.

SP (Speed)
Distribution shows mild right skewness.
Most cars have speeds around 110-130.
Few high-speed vehicles extend the right tail.
Reflects presence of performance segment.

WT (Weight)
Distribution is slightly right-skewed.
Most cars weigh between 28-38 units.
Few heavier cars create upper tail.
Suggests majority are mid-weight vehicles.
'''

#BOX PLOT (OUTLIER DETECTION)
plt.figure(figsize=(12,6))
sns.boxplot(data=cars)
plt.xticks(rotation=45)
plt.title("Boxplot for outlier detection")
plt.show()
'''
Inference
Outlier detects in the all of the features of car
And only MPG has not outlier
'''
#
#Correlation Heatmap
#

plt.figure(figsize=(8,6))
sns.heatmap(cars.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
'''
Inference
'''
#
#PAIRPLOT (BIVARIATE ANALYSIS)
#
sns.pairplot(cars)
plt.show()
'''
Inference
Check linear relationship visually.
Detect non-linear patterns or clusters.
'''
#
#MULTICOLLINEARITY CHECK (VIF)
#
#Assuming 'Milage' is dependent variable
x=cars
x_const=add_constant(x)
'''
When checking multicollinearity for HP:
We run:
'''
vif_data=pd.DataFrame()
vif_data['Feature']=x_const.columns
vif_data['VIF']=[variance_inflation_factor(x_const.values, i)
                 for i in range(x_const.shape[1])]
print("\nvariance inflation factor:\n", vif_data)
'''
Inference
VIF>10-Severe multicollinearity
VIF 5-10-Moderate multicollinearity
Remove or combine variance if VIF high.
'''
########################################
#
#FIT MULTIPLE LINEAR REGRESSION MODEL
#
import statsmodels.api as sm
import scipy.stats as stats
import matplotlib.pyplot as plt
#Dependent Variable
y=cars['MPG']
#Independent Variables (remove MPG)
X=cars.drop(columns=['MPG'])
#Add constant (intercept)
X=sm.add_constant(X)
#Fit model
model=sm.OLS(y,X).fit()
print(model.summary())
#
#RESIDUAL ANALYSIS
#
residuals=model.resid
fitted_vals=model.fittedvalues
#Residual vs Fitted plot
plt.figure(figsize=(6,4))
plt.scatter(fitted_vals,residuals)
plt.axhline(0, color='red')
plt.xlabel("Fitted values")
plt.ylabel("Residuals")
plt.title('Fitted values vs Residuals')
plt.show()
'''
Inference
'''
#
#QQ PLOT (NORMALITY CHECK FOR RESIDUALS
plt.figure(figsize=(6,4))
stats.probplot(residuals, dist="norm", plot=plt)
plt.title("QQ PLOT - RESIDUALS")
plt.show()
'''
Inference
'''

#
#Step1: Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from scipy.stats import skew
from feature_engine.outliers import Winsorizer
#Step 2: Load Data
cars=pd.read_csv("C:/15-Regression/Cars.csv")
print("Initial Shape",cars.shape)
print(cars.head())
#Step 3 Baic Cleaning
print("\nData Types:\n", cars.dtypes)
print("\nMissing Values Before Treatment:\n", cars.isnull().sum())
'''
Inference
Dataset contains only numerical values
No categorical encoding required
If missing values exist - must be handled
MPG is target variables
''' 
#Step 4: Missing values treatment (Median Imputation)
for col in cars.columns:
    cars[col].fillna(cars[col].median(), inplace=True)
print("\nMissing Values After Treatment:\n", cars.isnull().sum())
'''
Inference
Median used beacause
Robust to outlier
Suitable for skwed numerical data
Prevents distortion of coefficients.
'''
#Step 5: Duplicate Removals
cars.drop_duplicates(inplace=True)
print("After removing duplicates:", cars.shape)
'''
Removes repeated vehicle records 
Prevents model bias 
Improves generalization capability.
'''

#Step 6: Outlier Detection
plt.figure(figsize=(8,5))
sns.boxplot(data=cars, orient='h')
plt.title("Boxplot Before Treatment")
plt.show()
'''
HP and SP show extreme values.
VOL and WT show strong correlation.
Outlier can distort regression coefficients.
'''
#Step 7: outlier treatment using winsorization
winsor = Winsorizer(
    capping_method='iqr',
    tail='both',
    fold=1.5,
    variables=list(cars.columns)
)

cars=winsor.fit_transform(cars)

plt.figure(figsize=(8,5))
sns.boxplot(data=cars, orient='h')
plt.title("Boxplt After Outlier Treatment ")
plt.show()
'''
Inference
Extreme values capped using IQR method.
Reduces impact of abnormal vehicles.
Improves regression stability.
'''
#Step 8: SKEWNESS CHECK
print("\nSkewness:\n", cars.skew())
'''
Inference
Skewness>1=Strong Skew (log transformation may help).
Mild skew=acceptable for regression
Helps decide transformation strategy.
'''
#Step 9: TRAIN_TEST_SPLIT
X=cars.drop(columns=['MPG'])
y=cars['MPG']
X_train,X_test,y_train,y_test=train_test_split(
    X,y, test_size=0.2, random_state=42
)
print("\nTraining Shape:", X_train.shape)
print("\nTesting Shape:", X_test.shape)
'''
Inference
80% data used for training.
20% data used for testing.
Ensures model generalization.
'''
#
#STEP 10: BUILD MULTIPLE LINEAR REGRESSION MODEL
#
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
#Combine training data into one dataframe for formula api
cars_train=pd.concat([X_train, y_train], axis=1)    
cars_test=pd.concat([X_test, y_test], axis=1)    
#Initial model with all predctors
ml1=smf.ols('MPG~HP+VOL+SP+WT', data=cars_train).fit()
print(ml1.summary())
'''
Inference
1 Model Strength 
R-Squared = 0.831
Model explains 83.1% of variation in MPG
This is a strong model fit.
Indicates predictirs collectively explain fuel efficiency well.

Adjusted R-Squared=0.820
very close to R-Square
 
Dep. Variable:                    MPG   R-squared:                       0.774
Model:                            OLS   Adj. R-squared:                  0.759
Method:                 Least Squares   F-statistic:                     50.55
Date:                Thu, 04 Jun 2026   Prob (F-statistic):           2.08e-18
Time:                        17:29:54   Log-Likelihood:                -182.24
No. Observations:                  64   AIC:                             374.5
Df Residuals:                      59   BIC:                             385.3
Df Model:                           4                                         
Covariance Type:            nonrobust  

Omnibus:                        2.900   Durbin-Watson:                   1.715
Prob(Omnibus):                  0.235   Jarque-Bera (JB):                2.067
Skew:                           0.391   Prob(JB):                        0.356
Kurtosis:                       3.403   Cond. No.                     6.17e+03        

Indicates:
Strong multicollinearity present
'''
# 
#STEP 11:MULTICOLLINEARITY CHECK (VIF)
#
#Calculating VIF manually
rsq_hp=smf.ols('HP~VOL+SP+WT', data=cars_train).fit().rsquared
vif_hp=1/(1-rsq_hp)                              

rsq_vol=smf.ols('HP~VOL+SP+WT', data=cars_train).fit().rsquared
vif_vol=1/(1-rsq_vol)                              

rsq_sp=smf.ols('HP~VOL+SP+WT', data=cars_train).fit().rsquared
vif_sp=1/(1-rsq_sp)                              

rsq_wt=smf.ols('HP~VOL+SP+WT', data=cars_train).fit().rsquared
vif_wt=1/(1-rsq_wt)                              

vif_frame=pd.DataFrame({
    'Variable':['HP','VOL','SP','WT'],
    'VIF':[vif_hp, vif_vol, vif_sp, vif_wt]
})
print('VIF Frame:', vif_frame)
#
#STEP 12: DROP HIGH VIF VARIABLE (Example: WT)
#
final_ml=smf.ols('MPG~HP+VOL+SP', data=cars_train).fit()
r2 = final_ml.rsquared
print("Summary:", final_ml)
#
#STEP 13:ASSUMPTION CHECKING
#
#Predictions 
train_pred=final_ml.predict(cars_train)
test_pred=final_ml.predict(cars_test)
#Residuals
residuals=final_ml.resid
#---QQ Plot----
sm.qqplot(residuals)
plt.title("QQ Plot - Residuals")
plt.show()
'''
Interpretation:
Residuals are approximately narmally distributed.
Minor tail deviations indicate presence of few mild outliers
'''
#
#Residuals vs Fitted
sns.residplot(x=train_pred, y=y_train, lowess=True)
plt.xlabel("Fitted Values")
plt.ylabel("Residuals")
plt.title("Residuals vs Fitted")
plt.show()
#
#STEP 14: MODEL EVALUATION (RMSE)
#
train_rmse=np.sqrt(np.mean((train_pred-y_train)**2))
test_rmse=np.sqrt(np.mean((test_pred-y_test)**2))
print("Train RMSE:", round(train_rmse,4))
print("Test RMSE:", round(test_rmse,4))
'''
Train RMSE < Test RMSE - Normal case
Train RMSE = Test RMSE - Ideal
Train RMSE >> Test RMSE - Underfitting
Train RMSE << Test RMSE - Overfitting
'''

