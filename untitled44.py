# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 16:27:58 2026

@author: shrih
"""

'''
# 
1 Busines Problem Statement
Insurance companies want to understand
which claim-related and demographic factors influence
whether a claimant hires an attorney.
Legal involvement significantly increases:
Claim settlement cost
Processing time
Litigation expenses
Operational risk
Being able to predict attorney involvement early
helps insurers manage risk proactively.

2 Business Objective:
Identify key factors influencing attorney hiring
Quantify the impact of claim amount and demographics
Build a predictive model to estimate probability of attorney involment
Help insurance companies reduce Litigation cost exposure 
Enable early intervention strategies for high-risk claims

3 Motivation:
Understanding attorney involvement Dredirt hiah-cort claim involment helps:
Predict high-cost claims early Allocate Legal resources efficiently Improve claim settlement strategies Reduce unnecessary Litigation expenses Improve profitability and operational planning Support risk-based pricing strategies

4 Constraints:
Some predictors may have weak statistical significance
Class imbalance risk (if present in other datasets) 
Claim behavior may depend on external Legal or regional factors 
Logistic regression assumes Linearity in Log-odds 
Extreme claim amounts may distort probability estimates 
Dataset may not include behavioral or policy-Level variables

5 Success Criteria:
Business Success Criteria:
Accurately identify high-risk claims Likely to involve attorneys 
Provide actionable insights for Litigation prevention 
Improve cost forecasting accuracy
Support data-driven claim management decisions 

Machine learning success criteria:   
Statistically significant model (LLR p-value <0.05)
meaningful paseduR2 (modrate exploratory power)
balanced precision & recall (-70%+)
stable performance on test data
ROC - AUC Significant greater than 0.5
no severe multcolinearity    
'''

# DATA Preprocessing
'''
Feature name       Description                         Type             Business Relex
ATTORNEY           whether claimant hired attorney     Binary           target variable
CLMAGE             Age of claimant                     numeric          demographic
Loss               claim amount                        numeric          financial
CLMINSUR           Insurance coverage indicator        binary           policy relate
CLMSEX             gender of claimant                  binary           demographic
SEATBELT           seatbelt usage indicator            binary           injury severi
'''


# step 1 Import libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import statsmodels.tools.tools import add_constant


#step 2 Load data

claimants= pd.read_csv("C:/Linear Regression/claimants (1).csv")

#drop unnecessary column
c1=claimants.drop('CASENUM',axis=1)

print("First 5 Rows:\n,",c1.head)
print("Data types:\n",c1.dtypes)
print("\nSummary Statistics:\n", c1.describe()) 
print("\nMissing Values:\n", c1.isnull().sum())

'''
Inference:

Check variable types (numeric / categorical), 
Ensure ATTORNEY is binary (0/1),
Identify missing values for imputation, 
There are several missing val - 
LOSS Likely has high vartance strong predictor candidate.

What Are Four Moment Business Decisions?

Mean

Variance

Skewness

Kurtosis

They describe distribution shape of numerical variables.
They are very important in Linear Regression, but their role changes in Logistic Regression.
In Linear Regression
They are critical because:
Normality assumption required (for residuals)
Homoscedasticity matters
Outliers affect coefficients strongly
So 4 moments directly influence:
Model validity
Hypothesis testing
Confidence intervals

 In Logistic Regression
Logistic regression does NOT require normality.
It assumes:
log (𝑝/1−𝑝)=𝛽0+ 𝛽1+....
So what matters more?
 Linearity in log-odds
 Multicollinearity
 Class balance
 Separation issues

'''

#step3 target variable analysis ()
print("\nTarget distribution:\n",c1['ATTORNEY'].value_counts())

sns.countplot(x='ATTORNEY', data=c1)
plt.title("Class Distribution of ATTORNEY")
plt.show()
'''
Inference:

1. The target variable ATTORNEY is nearly balanced.
2. CLass 0 (No Attorney) and Class 1 (Attorney) have
3. No significant class imbalance problem is observed.
4. Logistic regression can be applied directly without resampling techniques.
5. Accuracy will be a reliable metric since baseline accuracy is ~50%.
6. Model will not be biased toward any, dominant class.""

'''

#step 4 Univarate analysis (numerical feature)
c1[['CLMAGE','LOSS']].hist(figsize=(10,6))
plt.subplot("Histogram of numerical Variables")
plt.show()

'''
Inference:

1 CLMAGE

Distribution appears slightly right-skewed.
Majority of claimants are in the 20-50 age group.
Few older claimants (above 70-80) create a tail:
No extreme abnormal pattern observed.
Implication for Logistic Regression:
CLMAGE Looks reasonably distributed.
No immediate transformation required.
Can be used directly in the model.

2 LOSS
Distribution is highly positively skewed (strong right skew). Most claim amounts are small.
Few very Large claims create a Long right tail.
Presencė of extreme values.
Implication for Logistic Regression:
Strong skewness may distort Log-odds relationship.
Consider applying Log transformation:
'''
#step 5 outlier  detection (boxplot)
plt.figure(figsize=(8,5))
sns.boxplot(data=c1[['CLMAGE','LOSS']])
plt.title("Boxplot for Outlier Detection")
plt.show()

'''
Inference:

1 CLMAGE
Moderate spread observed.
Few upper outliers (very high ages).
Majority of ages Lie within reasonable range.
No extreme abnormal variation.
Model Impact:
CLMAGE does not show severe outLier problem.
Can be safely used in Logistic regression,
Outlier's are minimal and manageable.

2 LOSS

Very high number of upper outliers.
Strong right skewness confirmed.
Few extremely Large claim amounts (up to ~170+).
Most values clustered near Lower range.
Model Impact:
LOSS has significant extreme values
These may strongly influence Log-odds.
Recommended to apply winsorizor
'''

#step 6 bivariate analysis (target vs numerical)

sns.boxplot(x='ATTORNEY',y='LOSS',data=c1)
plt.title('Loss vs Attorney')
plt.show()

sns.boxplot(x='ATTORNEY',y='CLMAGE',data=c1)
plt.title('Clmage vs Attorney')
plt.show()

'''
inference:
age does  not show a very stong
Since distributions overlap heavily, CLMAGE alone may not be a strong predictor.
It may still contribute when combined with other variables (like LOSS)
'''

# ------------------------------------------------------------
# STEP 7: CATEGORICAL vs TARGET ANALYSIS
# ------------------------------------------------------------
print("\nCLMSEX vs ATTORNEY:\n", pd.crosstab(c1.CLMSEX, c1.ATTORNEY, normalize='index'))

"""
Inference:
    
For CLMSEX = 0
55.46% → Did NOT hire attorney
44.53% → Hired attorney
For CLMSEX = 1
47.43% → Did NOT hire attorney
52.56% → Hired attorney
Claimants with CLMSEX = 1 have a higher probability of hiring an attorney (~52.6%).
Claimants with CLMSEX = 0 are slightly less likely to hire (~44.5%).
Difference is moderate, not extreme.
"""


print("\nCLMINSUR vs ATTORNEY:\n", pd.crosstab(c1.CLMINSUR, c1.ATTORNEY, normalize='index'))
'''
For CLMINSUR = 0
63.33% → Did NOT hire attorney
36.67% → Hired attorney
For CLMINSUR = 1
49.62% → Did NOT hire attorney
50.38% → Hired attorney

 Interpretation
Claimants with CLMINSUR = 1 have a higher probability (~50.4%) of hiring an attorney.
Claimants with CLMINSUR = 0 are much less likely (~36.7%) to hire an attorney.
The difference (~14%) is noticeable.

'''
print("\nSEATBELT vs ATTORNEY:\n", pd.crosstab(c1.SEATBELT, c1.ATTORNEY, normalize='index'))

"""
Categorical (SEATBELT) vs Target (ATTORNEY)
 Observed Proportions
For SEATBELT = 0
50.63% → Did NOT hire attorney
49.37% → Hired attorney
For SEATBELT = 1
72.73% → Did NOT hire attorney
27.27% → Hired attorney

 Interpretation
Claimants not wearing seatbelt (0) show almost equal probability of hiring attorney (~49%).
Claimants wearing seatbelt (1) are much less likely (~27%) to hire attorney.
Difference is substantial (~22%).
This suggests:
SEATBELT is a strong discriminator for attorney hiring."""

# ------------------------------------------------------------
# STEP 8: CORRELATION MATRIX
# ------------------------------------------------------------
plt.figure(figsize=(6,4))
sns.heatmap(c1.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

"""
Inference:
1️ Correlation with Target (ATTORNEY)

| Variable | Correlation with ATTORNEY | Interpretation         |
| -------- | ------------------------- | ---------------------- |
| CLMSEX   | +0.08                     | Very weak positive     |
| CLMINSUR | +0.079                    | Very weak positive     |
| SEATBELT | -0.057                    | Weak negative          |
| CLMAGE   | +0.011                    | Almost no relationship |
| LOSS     | -0.22                     | Moderate negative      |



Key Observations:
LOSS (-0.22) shows the strongest relationship with ATTORNEY (moderate).
SEATBELT has weak negative correlation.
CLMSEX and CLMINSUR have weak positive relationships.
CLMAGE has almost no linear correlation.

Important:
Correlation only measures linear relationship.
Logistic regression models log-odds, so even weak correlations can
 become significant predictors.

2️ Multicollinearity Check (Among Predictors)
Look at predictor-to-predictor correlations:
All correlations are very low (close to 0).
No strong correlations (> 0.7 or < -0.7).
Highest among predictors is very small (~0.11).
Inference:
No multicollinearity problem.
 VIF values are expected to be low.
 Model coefficients will be stable."""

# ------------------------------------------------------------
# STEP 9: MULTICOLLINEARITY CHECK (VIF)
# ------------------------------------------------------------
X = c1.drop(columns=['ATTORNEY'])

# Replace infinite values
X = X.replace([np.inf, -np.inf], np.nan)

# Drop rows with missing values
X = X.dropna()

# Add constant
X_const = add_constant(X)

# Compute VIF
vif_data = pd.DataFrame()
vif_data["Feature"] = X_const.columns
vif_data["VIF"] = [variance_inflation_factor(X_const.values, i)
                   for i in range(X_const.shape[1])]

print("\nVariance Inflation Factor:\n", vif_data)
"""
Inference:
- VIF > 10 → severe multicollinearity.
- Remove variable if VIF high.
- Multicollinearity affects coefficient stability.
| Feature  | VIF   | Interpretation                     |
| -------- | ----- | ---------------------------------- |
| const    | 13.06 | Ignore (intercept not interpreted) |
| CLMSEX   | 1.00  | No multicollinearity               |
| CLMINSUR | 1.00  | No multicollinearity               |
| SEATBELT | 1.02  | No multicollinearity               |
| CLMAGE   | 1.00  | No multicollinearity               |
| LOSS     | 1.02  | No multicollinearity               |
Key Observations
All predictor variables have VIF ≈ 1.
VIF < 5 indicates no multicollinearity problem.
Predictors are almost independent of each other.
Coefficient estimates in logistic regression will be stable.

"""

# ------------------------------------------------------------
# STEP 10: SKEWNESS CHECK
# ------------------------------------------------------------
print("\nSkewness:\n", c1.skew())

"""

Skewness Inference:

ATTORNEY (0.04):
Target variable is nearly symmetric → confirms balanced class distribution.

CLMSEX (-0.23):
Slight negative skew → almost balanced categorical variable → no issue.

CLMINSUR (-2.81):
Highly negatively skewed → one category dominates → moderate imbalance.

SEATBELT (7.47):
Extremely positively skewed → strong dominance of one category.

CLMAGE (0.41):
Mild positive skew → acceptable distribution → no transformation required.

LOSS (7.72):
Extremely positively skewed → many small claims and few very large claims.
Recommended to apply log transformation to stabilize effect in logistic regression.

Overall:
Logistic regression does not require normality,
but extreme skewness (especially LOSS) may influence log-odds strongly.
 If skewness > 1 → apply log transformation.
"""


"""
Log transformation reduces skewness and stabilizes variance.
"""

# ------------------------------------------------------------
# STEP 11: CHECK LINEARITY IN LOGIT
# ------------------------------------------------------------
# Logistic regression assumes linearity in log-odds

# Create transformed variable safely
c1['LOSS_log'] = np.log1p(c1['LOSS'])

y = c1['ATTORNEY']
X = c1[['CLMAGE', 'LOSS_log']]

# Replace infinite values
X = X.replace([np.inf, -np.inf], np.nan)

# Drop rows with NaN in either X or y
data = pd.concat([X, y], axis=1).dropna()

X_clean = sm.add_constant(data[['CLMAGE', 'LOSS_log']])
y_clean = data['ATTORNEY']

# Fit model
model_temp = sm.Logit(y_clean, X_clean).fit()

print(model_temp.summary())


"""
What to Observe:
(A) Converged
Must be True
If False → model unreliable
Meaning:
MLE optimization successfully found solution.

(B) LLR p-value (Likelihood Ratio Test)

If:
LLR p-value < 0.05 → Model is significant
LLR p-value > 0.05 → Model not useful
Meaning:
At least one predictor affects probability.

This is the overall model significance test.

(C) Pseudo R²
Not same as linear regression R².
Interpretation guideline:
0.02 → weak
0.10 → moderate
0.20+ → strong (for logistic)

Meaning:
How much improvement over null model.

# Never interpret it like linear regression R².

(D) Log-Likelihood

LL-Null → model without predictors

Log-Likelihood → with predictors

If Log-Likelihood improves (less negative) → model better.


Inference:

Logistic Regression Inference:

Model Summary:
- Model converged successfully → estimation is reliable.
- LLR p-value = 2.62e-56 (< 0.05) → Model is statistically significant.
- Pseudo R² = 0.1608 → Model explains ~16% variation in log-odds.
  (Moderate explanatory power for logistic regression.)

Intercept (const = 0.9892, p < 0.001):
- Baseline log-odds of hiring an attorney when predictors = 0.
- Statistically significant.

CLMAGE (coef = 0.0089, p = 0.007):
- Positive and statistically significant.
- As age increases, probability of hiring attorney slightly increases.
- Odds ratio ≈ exp(0.0089) ≈ 1.009
  → Each 1-year increase in age increases odds by ~0.9%.

LOSS_log (coef = -1.4231, p < 0.001):
- Strong negative and highly significant predictor.
- As log(LOSS) increases, probability of hiring attorney decreases.
- Odds ratio ≈ exp(-1.4231) ≈ 0.24
  → Higher loss reduces odds of hiring attorney by ~76%.

Overall Interpretation:
- Both CLMAGE and LOSS_log significantly influence attorney hiring.
- LOSS_log is the strongest predictor (large magnitude and very small p-value).
- Model is statistically strong but with moderate predictive power.
"""

# ------------------------------------------------------------
# FINAL EDA SUMMARY
# ------------------------------------------------------------

"""
FINAL EDA SUMMARY FOR LOGISTIC REGRESSION:

1. Target variable checked for class balance.
2. LOSS appears strong predictor (higher loss → higher attorney probability).
3. CLMAGE impact assessed.
4. Categorical variables analyzed using cross-tab.
5. Multicollinearity checked using VIF.
6. Skewness checked; log transformation applied.
7. Linearity in log-odds assumption verified.


"""


# ============================================================
# DATA PREPROCESSING FOR LOGISTIC REGRESSION
# ============================================================

# ------------------------------------------------------------
# STEP 1: IMPORT REQUIRED LIBRARIES
# ------------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from feature_engine.outliers import Winsorizer

# ------------------------------------------------------------
# STEP 2: LOAD DATASET
# ------------------------------------------------------------
claimants = pd.read_csv("c:/360DG/Datasets/claimants.csv")

print("Initial Shape:", claimants.shape)
print(claimants.head())

# ------------------------------------------------------------
# STEP 3: BASIC CLEANING
# ------------------------------------------------------------
# Drop unnecessary column
c1 = claimants.drop(columns=["CASENUM"])

# Convert special symbols to NaN if present
c1 = c1.replace(['?', 'NA', 'N/A', 'null', 'NULL', ' '], np.nan)

print("\nData Types:\n")
print(c1.dtypes)

print("\nMissing Values Before Treatment:\n")
print(c1.isnull().sum())

# ------------------------------------------------------------
# STEP 4: MISSING VALUE TREATMENT
# ------------------------------------------------------------

# Numerical variable - Median Imputation
c1["CLMAGE"] = c1["CLMAGE"].fillna(c1["CLMAGE"].median())

# Categorical variables - Mode Imputation
c1["CLMSEX"] = c1["CLMSEX"].fillna(c1["CLMSEX"].mode()[0])

c1["CLMINSUR"] = c1["CLMINSUR"].fillna( c1["CLMINSUR"].mode()[0])

c1["SEATBELT"] = c1["SEATBELT"].fillna( c1["SEATBELT"].mode()[0])

print("\nMissing Values After Treatment:\n")
print(c1.isnull().sum())

print("\nTotal Missing Values Remaining:", c1.isnull().sum().sum())
'''
Inference:
• Median used for CLMAGE → robust to outliers.
• Mode used for categorical variables → preserves class distribution.
• Dataset now free from missing values.
'''


# ------------------------------------------------------------
# STEP 5: DUPLICATE REMOVAL
# ------------------------------------------------------------
c1.drop_duplicates(inplace=True)
print("\nShape After Removing Duplicates:", c1.shape)

'''
Inference:
• Removes repeated claimant records.
• Prevents bias in probability estimation.
• Improves model generalization.
'''


# ------------------------------------------------------------
# STEP 6: OUTLIER DETECTION
# ------------------------------------------------------------
plt.figure(figsize=(8,5))
sns.boxplot(data=c1[["CLMAGE","LOSS"]])
plt.title("Boxplot Before Treatment")
plt.show()

'''
Inference:
• CLMAGE shows mild outliers.
• LOSS shows strong right-skew and extreme values.
• Extreme values may distort log-odds.
'''


# ------------------------------------------------------------
# STEP 7: OUTLIER TREATMENT (OPTIONAL FOR LOGISTIC)
# ------------------------------------------------------------
winsor = Winsorizer(
    capping_method='iqr',
    tail='both',
    fold=1.5,
    variables=["CLMAGE","LOSS"]
)

c1 = winsor.fit_transform(c1)

plt.figure(figsize=(8,5))
sns.boxplot(data=c1[["CLMAGE","LOSS"]])
plt.title("Boxplot After Winsorization")
plt.show()

'''
Inference:
• Extreme claim values capped.
• Reduces influence of abnormal cases.
• Improves stability of logistic coefficients.
'''


# ------------------------------------------------------------
# STEP 8: SKEWNESS CHECK
# ------------------------------------------------------------
print("\nSkewness:\n", c1.skew())

'''
Inference:
• LOSS typically shows high positive skew.
• Log transformation recommended for LOSS.
• Logistic regression does not require normality,
  but extreme skewness affects log-odds relationship.
'''


# ------------------------------------------------------------
# STEP 9: LOG TRANSFORMATION (FOR SKEWED VARIABLE)
# ------------------------------------------------------------
c1["LOSS_log"] = np.log1p(c1["LOSS"])

'''
Inference:
• log1p() prevents log(0) issues.
• Reduces skewness.
• Stabilizes effect in logistic regression.
'''


# ------------------------------------------------------------
# STEP 10: DEFINE FEATURES AND TARGET
# ------------------------------------------------------------
X = c1.drop(columns=["ATTORNEY","LOSS"])   # Use transformed LOSS_log
y = c1["ATTORNEY"]

print("\nFeature Columns:", X.columns)


# ------------------------------------------------------------
# STEP 11: TRAIN-TEST SPLIT
# ------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print("\nTraining Shape:", X_train.shape)
print("Testing Shape:", X_test.shape)

'''
Inference:
• 70% used for training.
• 30% used for testing.
• Ensures generalization capability.
'''


# ------------------------------------------------------------
# NOTE ON SCALING
# ------------------------------------------------------------
'''
Standardization is NOT mandatory for logistic regression
unless:
• Regularization is used (L1/L2 penalty)
• Variables have extremely different scales

Since most variables are binary or moderate scale,
scaling is optional here.
'''


# ------------------------------------------------------------
# FINAL PREPROCESSING SUMMARY
# ------------------------------------------------------------
"""
FINAL DATA PREPROCESSING SUMMARY:

• Dropped unnecessary column (CASENUM).
• Handled missing values (median & mode).
• Removed duplicates.
• Treated outliers using IQR-based winsorization.
• Applied log transformation on LOSS.
• Split dataset into training and testing sets.

Dataset is now ready for Logistic Regression modeling.
"""
# ============================================================
# LOGISTIC REGRESSION – MODEL BUILDING
# ============================================================

# ------------------------------------------------------------
# STEP 12: IMPORT REQUIRED MODELING LIBRARIES
# ------------------------------------------------------------
import statsmodels.formula.api as sm
from sklearn.metrics import roc_curve, auc, classification_report
from sklearn.model_selection import train_test_split
from sklearn import metrics


# ------------------------------------------------------------
# STEP 13: BUILD LOGISTIC REGRESSION MODEL (FULL DATA)
# ------------------------------------------------------------
logit_model = sm.logit(
    'ATTORNEY ~ CLMAGE + LOSS_log + CLMINSUR + CLMSEX + SEATBELT',
    data=c1
).fit()

print(logit_model.summary())

# Detailed Summary (Tabular Format)
print(logit_model.summary2())

"""
Inference:

• summary() gives statistical overview:
    converged:  True   model is successfully conversed
    - LLR p-value → Overall model significance
    - Pseudo R² → Model explanatory strength
    - coef → Direction of impact
    - P>|z| → Variable significance

• summary2() gives:
    - Clean tabular format
    - Confidence intervals clearly displayed
    - Easier for reporting and documentation

• Compare coefficients and p-values:
    - Significant predictors → p < 0.05
    - Positive coef → Increases probability
    - Negative coef → Decreases probability

• AIC used for model comparison:
    Lower AIC → Better model fit.
"""


"""
Inference summary :

Logistic Regression Inference:

Model Fit:
• Model converged successfully → estimation is reliable.
• LLR p-value = 2.769e-62 (< 0.05) → Overall model is highly significant.
• Pseudo R² = 0.1642 → Model explains ~16% variation in log-odds
  (moderate strength for logistic regression).
• Log-Likelihood improved significantly from null model.

Variable Interpretation:

CLMAGE (coef = 0.0086, p = 0.011):
• Statistically significant.
• Positive effect → As age increases, probability of hiring attorney 
increases slightly.
• Small but meaningful impact.

LOSS_log (coef = -1.4670, p < 0.001):
• Highly significant and strongest predictor.
• Negative coefficient → Higher claim amount (log scale)
 reduces odds of hiring attorney.
• Major driver in the model.

CLMINSUR (coef = 0.4744, p = 0.030):
• Statistically significant.
• Insured claimants have higher probability of hiring attorney.

CLMSEX (coef = 0.3733, p = 0.003):
• Statistically significant.
• Gender has meaningful influence on attorney hiring probability.

SEATBELT (coef = -0.6311, p = 0.230):
• Not statistically significant (p > 0.05).
• Does not show strong independent effect in presence of other variables.

Intercept (p = 0.079):
• Not statistically significant at 5% level.

Overall Conclusion:
• Model is statistically strong.
• LOSS_log is the most influential predictor.
• CLMAGE, CLMINSUR, and CLMSEX are significant contributors.
• SEATBELT may be considered for removal if model simplification is required.


 Inference from summary2():

MODEL FIT:
• Converged = 1.0000 → Model estimation successful.
• LLR p-value = 2.7695e-62 (< 0.05) → Overall model is statistically significant.
• Pseudo R-squared = 0.164 → Moderate explanatory strength.
• Log-Likelihood improved from -907.28 (null) to -758.31 → Model improves over baseline.

AIC (Akaike Information Criterion) = 1528.62:
• AIC measures model quality by balancing:
      - Model fit (Log-Likelihood)
      - Model complexity (number of predictors)
• Lower AIC indicates a better model.
• AIC is used for comparing multiple logistic models.
• AIC alone has no meaning unless compared with another model.
• If removing a non-significant variable lowers AIC → simplified model preferred.

BIC = 1559.69:
• Similar to AIC but penalizes complexity more strongly.
• Useful when comparing models.

SIGNIFICANT VARIABLES (p < 0.05):
• CLMAGE
• LOSS_log (strongest predictor)
• CLMINSUR
• CLMSEX

NOT SIGNIFICANT:
• SEATBELT (p = 0.2301)
• Intercept (p = 0.0786)

FINAL OBSERVATION:
Model is statistically strong, and AIC can be used to compare this model
with alternative models (e.g., removing SEATBELT).

"""


# ------------------------------------------------------------
# STEP 14: PREDICTION (PROBABILITY)
# ------------------------------------------------------------
pred = logit_model.predict(c1)


# ------------------------------------------------------------
# STEP 15: ROC CURVE & OPTIMAL THRESHOLD
# ------------------------------------------------------------
fpr, tpr, thresholds = roc_curve(c1.ATTORNEY, pred)

# Youden’s J Statistic
optimal_idx = np.argmax(tpr - fpr)
optimal_threshold = thresholds[optimal_idx]

print("Optimal Threshold:", optimal_threshold)

# Plot ROC Curve
plt.plot(fpr, tpr, label="ROC Curve")
plt.plot([0,1], [0,1], 'k--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve – Full Data")
plt.legend()
plt.show()

roc_auc = auc(fpr, tpr)
print("Area Under Curve (AUC):", roc_auc)

"""
Inference:
• AUC closer to 1 → strong discrimination.
• AUC ≈ 0.5 → random model.
• Optimal threshold balances sensitivity & specificity.
"""


# ------------------------------------------------------------
# STEP 16: CLASSIFICATION BASED ON OPTIMAL THRESHOLD
# ------------------------------------------------------------
c1["pred"] = np.where(pred > optimal_threshold, 1, 0)

print("\nClassification Report (Full Data):")
print(classification_report(c1["ATTORNEY"], c1["pred"]))

"""
Inference:
• Precision → Correctness of positive predictions.
• Recall → Ability to detect actual positives.
• F1-score → Balance between precision & recall.
• Accuracy alone should not be the only metric.

1️ Accuracy = 0.72
The model correctly classifies 72% of total cases.
Since your classes are balanced (~50-50),
72% is a meaningful improvement over random guessing (50%).

2️ Class 0 (No Attorney)
Precision = 0.74
When model predicts "No Attorney", it is correct 74% of the time.
Recall = 0.71
It correctly identifies 71% of actual No-Attorney cases.

F1-score = 0.73
Balanced performance between precision & recall.
Interpretation:
Model is slightly better at correctly identifying non-attorney cases.

3️ Class 1 (Attorney Hired)
Precision = 0.70
When model predicts "Attorney", it is correct 70% of the time.
Recall = 0.73
It correctly captures 73% of actual attorney cases.
F1-score = 0.72
Balanced detection performance.
Interpretation:
Model is slightly better at detecting attorney cases (recall higher 
                                                      than precision).
4️ Macro Average = 0.72
Simple average of both classes.
Since dataset is balanced, macro and weighted averages are almost 
equal.

5️ Weighted Average = 0.72
Weighted by class frequency.
Confirms balanced performance.

 What Is Most Important Here?
Since this is litigation prediction:
If business goal is:
Detect attorney hiring cases early → Recall for Class 1 is important 
(0.73 is decent).
Avoid false legal alerts → Precision for Class 1 matters 
(0.70 acceptable).

 Overall Model Interpretation

 Balanced performance
 No major bias toward any class
 Similar precision & recall → stable model
 F1 around 0.72 → moderate predictive strength


"""

# ------------------------------------------------------------
# STEP 17: TRAIN-TEST SPLIT
# ------------------------------------------------------------
train_data, test_data = train_test_split(c1, test_size=0.3, random_state=42)

# ------------------------------------------------------------
# STEP 18: MODEL BUILDING ON TRAIN DATA
# ------------------------------------------------------------
model = sm.logit(
    'ATTORNEY ~ CLMAGE + LOSS_log + CLMINSUR + CLMSEX + SEATBELT',
    data=train_data
).fit()

# Standard Summary
print(model.summary())

"""
Inference:

Model Fit:
• Model converged successfully → estimation is reliable.
• LLR p-value = 3.005e-45 (< 0.05) → Overall model is highly significant.
• Pseudo R² = 0.172 → Moderate explanatory strength (~17% improvement over null model).
• Log-Likelihood improved from -635.28 (null) to -525.99 → Predictors improve model fit.

Significant Variables (p < 0.05):
• Intercept (p = 0.022) → Significant baseline log-odds.
• CLMAGE (p = 0.047) → Small but significant positive effect.
• LOSS_log (p < 0.001) → Highly significant and strongest predictor (negative effect).

Marginal / Not Significant:
• CLMINSUR (p = 0.131) → Not significant at 5% level.
• CLMSEX (p = 0.098) → Marginally significant at 10% level.
• SEATBELT (p = 0.432) → Not significant.

Key Takeaway:
• LOSS_log is the dominant predictor.
• CLMAGE has a mild positive impact.
• Other variables show weaker or no independent significance in this model.
• Overall model is statistically strong with moderate predictive power.
"""
# Detailed Summary (Tabular Format)
print(model.summary2())

"""
Inference from summary2():

Model Fit:
• Converged = 1.0000 → Model estimation successful.
• LLR p-value = 3.0046e-45 (< 0.05) → Overall model is highly significant.
• Pseudo R-squared = 0.172 → Moderate explanatory strength (~17% improvement over null model).
• Log-Likelihood improved from -635.28 (null) to -525.99 → Model performs better than baseline.

AIC = 1063.98:
• AIC (Akaike Information Criterion) measures model quality 
  by balancing goodness-of-fit and model complexity.
• Lower AIC indicates a better model (when comparing multiple models).
• AIC has no standalone meaning — it must be compared with another model.
• If removing non-significant variables lowers AIC → simpler model preferred.

BIC = 1092.90:
• Similar to AIC but penalizes model complexity more strongly.
• Useful for model comparison.

Significant Predictors (p < 0.05):
• Intercept
• CLMAGE
• LOSS_log (strongest predictor)

Marginal / Not Significant:
• CLMINSUR (p = 0.1309) → Not significant at 5%.
• CLMSEX (p = 0.0983) → Marginally significant at 10%.
• SEATBELT (p = 0.4321) → Not significant.

Final Observation:
• Model is statistically strong.
• LOSS_log is dominant predictor.
• AIC can be used to compare this model with reduced models
  (e.g., removing SEATBELT).
"""




"""
Inference:

• summary() gives statistical overview:
    - LLR p-value → Overall model significance
    - Pseudo R² → Model explanatory strength
    - coef → Direction of impact
    - P>|z| → Variable significance

• summary2() gives:
    - Clean tabular format
    - Confidence intervals clearly displayed
    - Easier for reporting and documentation

• Compare coefficients and p-values:
    - Significant predictors → p < 0.05
    - Positive coef → Increases probability
    - Negative coef → Decreases probability

• AIC used for model comparison:
    Lower AIC → Better model fit.
"""
"""
Inference:
• Compare coefficients with full model.
• AIC used for comparison.
• Lower AIC → better model fit.
• Significant predictors should remain consistent.
"""


# ------------------------------------------------------------
# STEP 19: PREDICTION ON TEST DATA
# ------------------------------------------------------------
test_pred_prob = model.predict(test_data)

test_data["test_pred"] = np.where(
    test_pred_prob > optimal_threshold, 1, 0
)

# Confusion Matrix
confusion_matrix_test = pd.crosstab(
    test_data["test_pred"],
    test_data["ATTORNEY"]
)

print("\nConfusion Matrix (Test Data):")
print(confusion_matrix_test)

# Accuracy
accuracy_test = metrics.accuracy_score(
    test_data["ATTORNEY"],
    test_data["test_pred"]
)

print("Test Accuracy:", accuracy_test)
#0.6895674300254453
print("\nClassification Report (Test Data):")
print(classification_report(
    test_data["ATTORNEY"],
    test_data["test_pred"]
))

# ROC Curve (Test Data)
fpr_test, tpr_test, threshold_test = roc_curve(
    test_data["ATTORNEY"],
    test_pred_prob
)

roc_auc_test = auc(fpr_test, tpr_test)

plt.plot(fpr_test, tpr_test)
plt.plot([0,1],[0,1],'k--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve – Test Data")
plt.show()

print("Test AUC:", roc_auc_test)

"""
Inference:
• Test performance measures generalization ability.
• If Test AUC close to Train AUC → model stable.
• Large gap → overfitting.
"""


# ------------------------------------------------------------
# STEP 20: TRAIN PERFORMANCE CHECK
# ------------------------------------------------------------
train_pred_prob = model.predict(train_data)

train_data["train_pred"] = np.where(
    train_pred_prob > optimal_threshold, 1, 0
)

accuracy_train = metrics.accuracy_score(
    train_data["ATTORNEY"],
    train_data["train_pred"]
)

print("Train Accuracy:", accuracy_train)
#0.73173391
print("\nClassification Report (Train Data):")
print(classification_report(
    train_data["ATTORNEY"],
    train_data["train_pred"]
))

"""
Inference:
• If Train Accuracy >> Test Accuracy → Overfitting.
• If similar → Good generalization.
• Balanced precision & recall indicates stable model.
"""

------------------------------------------------------------
BUSINESS IMPACT
------------------------------------------------------------
1️ Financial Impact

Early identification of claims likely to involve attorneys
Helps estimate potential litigation costs in advance
Reduces unexpected claim settlement expenses
Supports better reserve allocation for high-risk cases
Improves overall claim cost forecasting accuracy
Impact:
Lower litigation cost and improved profitability.

2️ Operational Impact
Enables prioritization of high-risk claims
Faster intervention by legal and claims teams
Reduces claim processing delays
Optimizes workload distribution among claim managers
Impact:
Improved operational efficiency and faster decision-making.

3️ Risk Management Impact
Provides probability-based risk scoring for each claim
Identifies demographic and financial risk factors
Helps build proactive legal mitigation strategies
Supports data-driven underwriting improvements

Impact:

Better risk profiling and reduced legal exposure.

4️ Strategic Impact
Enables predictive analytics in claim management
Supports long-term policy pricing optimization
Improves competitive positioning in insurance market
Builds foundation for AI-driven claims automation

Impact:
Strengthens data-driven strategic planning.

5️ Customer Experience Impact
Faster settlement for low-risk claims
Early support for high-risk claimants
Transparent and efficient claim handling

Impact:

Improved customer satisfaction and brand trust.

