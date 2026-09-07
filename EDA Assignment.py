# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 18:49:31 2026

@author: shrih
"""
'''
Dataset 1
'''
# Business understanding

# 1. Business Problem Statement:
# - Which factor is influence to user
# - The cost is spend for advertising is effective or wasted

# 2. Simplified Context of the Problem:
# - The advertising company shows ads to user based on 
# - age, income, internet usage, city, country, time spend online

# 3. Problem Identification:
# - The every not want to see ads
# - The ads are Low conversion rate

# 4. Business Objective:
# - predict the wheater ads are clicked by user mostly
# - Improve targeted advertising

# 5. Stakeholder Expectations:
# - Marketing Team: Better audience targeting
# - Business Managers: Increased revenue

# 6. Constraints & Limitations:
# - Few adertising are boring or take more time
# - The important data is missing in ads

#7.Feasibility Check:
# - The ML model can predict the users where ads are mostly clicked using historic and real-time data

# 8. Success Criteria
# Business Success Criteria:
# - Customer are increase after see ads

# ML Success Criteria:
# - High prediction accuracy

#Business Impact
# - Increase customer rate
# - Increase companise brand value
# - Improve customers efficiency

#EDA
#1 library required
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#2 dataset load
df=pd.read_csv("C:/Assignment/EDA/advertising (1).csv")

#3 basic understanding
df.shape
df.size
df.columns

df.describe()
#define min, max, mean, mode, median

#4 rename columns name
df.columns=('Time','Age','Area_icon','Internet','Topic','City','Male','Country','Timestamp','Clicked')

#5 Check data types
df.dtypes
#inference:
#(Float64) columns Time,Area_icon,Internet
#(int64) columns Age,Male,Clicked
#(object) Topic, city, country, Timestamp,
#target column type is integer (categorical encoded).


#shape and size print
print("Shape of Dataset:", df.shape)
print("Size of Dataset:",df.size)  

#6 First moment (Mean)
mean_values=df.mean(numeric_only=True)
print("\nMean (first moment):\n",mean_values)

#7 Second moment(Variance and Std)
var_values=df.var(numeric_only=True)
print("\nVariance:\n",var_values)

std_values=df.std(numeric_only=True)
print("\nStandard Deviation:\n",std_values)  

#8 Third Moment(Skewness)
skew_values=df.skew(numeric_only=True)
print("\nSkewness:\n",skew_values)

#inference:
#positive skew -> Three samples with high concentration 
#negative skew -> Three smaples with very low concentration

#9 Fourth Moment(Kurtosis)
kurt_values=df.kurtosis(numeric_only=True)
print("\nKurtosis:\n",kurt_values)

#inference:
#platkurtic (<0): flater distribution uniform composition 
#leptokurtosis (>0): sharp peak extreme composition present

#10 Univartate analysis
#Histogram
df.drop(columns=['Clicked']).hist(
    figsize=(12,10),
    edgecolor='Blue',
    )
plt.suptitle("Histograms of Advertiesment")
plt.tight_layout()
plt.show()

#inference 

#11Boxplot
plt.figure(figsize=(12,6))
sns.boxplot(data=df.drop(columns=['Clicked']),orient='h')
plt.title("Boxplot of Advertiesment")
plt.show()

#inference
#outiler detect
#

#12 Jointplo
sns.jointplot(data=df, x="Area_icon", y="Internet", kind="scatter")
plt.suptitle("Joint Plot: Area_icon vs Internet", y=1.02)
plt.show()

#inference

#13 Pairplot
sns.pairplot(df.drop(columns='Clicked'),)
plt.suptitle("Pair Plot of All Features", y=1.02)
plt.show()

#14 Heatmap
plt.figure(figsize=(10,8))
sns.heatmap(
    df.drop(columns=['Clicked']),
    annot=True,
    cmap='coolwarm'
    )
plt.title("Correlation Heatmap - Advertiesment Dataset")
plt.show()

#15 PDF & CDF  
num_cols=df.select_dtypes(include=np.number).columns.drop(['Clicked'])

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
    plt.plot(sorted_vals,y_vals,marker='.',linestyle='None')
    plt.title(f"CDF of {col}")
    
    plt.tight_layout()
    plt.show()

#inference


#class distribution (target analusis)

sns.countplot(x=df['Clicked'])
plt.title("Distribution of Advertiesment Types")
plt.show()    

#inference 
#data is balanced in last column Clicked
#all advertiesment data set is balanced


##################################################################


'''
Dataset 2
'''
# Business understanding
# 1. Business Problem Statement:
# - Some customer are rejected offers
# - And cost for term deposite and time consuming

# 2. Simplified Context of the Problem:
# - A bank contact customers using phone calls, emails, history.


# 3. Problem Identification:
# - Custumers balance and loan status faces the bank


# 4. Business Objective:
# - Predict wheater customers are open term deposite
# - Improve campaign efficeincy

# 5. Stakeholder Expectations:
# - Marketing Team: Better customer targeting
# - Business Managers: Increased revenue from deposites
# - Data team: Accurate prediction model

# 6. Constraints & Limitations:
# - Customer behavior may change over time

#7.Feasibility Check:
# - The ML model can predict the users wheather customers are not open term deposite using historic and real-time data

# 8. Success Criteria
# Business Success Criteria:
# - The term deposite increases the revenue of bank

# ML Success Criteria:
# - High prediction accuracy

#Business Impact
# - Increase customer deposite
# - Increase  revenue of bank
# - Improve loan and interest due to deposite


#1 library required
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#2 Dataset load
bank=pd.read_csv("C:/Assignment/EDA/bank_data (1).csv")

#3 Basic understanding
bank.columns
bank.size
bank.shape
bank.dtypes
bank.describe()

#inference
#define a column name 
#dataset szie is 1446752
#dataset shape is 45211 rows and 32 columns
#data type is all int64
#find a min max mean mode and median for basic understanding

#4 First Moment(Mean)
mean_values=bank.mean(numeric_only=True)
print("\nMean of Bank daaset:\n",mean_values)


#5 Second Moment (variance and std)
var_values=bank.var(numeric_only=True)
print("\nVariance of bank dataset:\n",var_values)

std_values=bank.std(numeric_only=True)
print("\nStandard Deviation:\n",std_values)  

#inference

#6 Third moment (Skewness)
skew_values=bank.skew(numeric_only=True)
print("\nSkewness of bank dataset:\n",skew_values)

#inference

#7 fourth moment (kurtosis)
kurt_values=bank.kurtosis(numeric_only=True)
print("\nKurtosis of bank dataset:\n",kurt_values)

#inference

#8 Univartate analysis
#Histogram
bank.drop(columns=['y']).hist(
    figsize=(12,10),
    edgecolor='Blue',
    )
plt.suptitle("Histograms of Bamk")
plt.tight_layout()
plt.show()

#inference 

#11Boxplot
plt.figure(figsize=(12,6))
sns.boxplot(data=bank.drop(columns=['y']),orient='h')
plt.title("Boxplot of Bank")
plt.show()

#inference

#12 Jointplo
sns.jointplot(data=bank, x="balance", y="duration", kind="scatter")
plt.suptitle("Joint Plot: Balance vs Duration", y=1.02)
plt.show()

#inference

#13 Pairplot
sns.pairplot(bank.drop(columns='y'),)
plt.suptitle("Pair Plot of All Features", y=1.02)
plt.show()

#14 Heatmap
plt.figure(figsize=(10,8))
sns.heatmap(
    bank.drop(columns=['y']),
    annot=True,
    cmap='coolwarm'
    )
plt.title("Correlation Heatmap - Bank Dataset")
plt.show()

#15 PDF & CDF  
num_cols=bank.select_dtypes(include=np.number).columns.drop(['y'])

for col in num_cols:
    plt.figure(figsize=(12,5))
    
    
    #pdf
    plt.subplot(1,2,1)
    sns.kdeplot(bank[col],fill=True)
    plt.title(f"PDF Of {col}")
    
    
    #CDF
    plt.subplot(1,2,2)
    sorted_vals=np.sort(bank[col])
    y_vals=np.arange(len(sorted_vals)) / float(len(sorted_vals))
    plt.plot(sorted_vals,y_vals,marker='.',linestyle='None')
    plt.title(f"CDF of {col}")
    
    plt.tight_layout()
    plt.show()

#inference


#class distribution (target analusis)

sns.countplot(x=bank['y'])
plt.title("Distribution of Bnak Types")
plt.show()    

#inference 
#data is inbalanced 
#all advertiesment data set is balanced

##################################################################

'''
dataset 3
'''
#Business understanding
# 1. Business Problem Statement:
# - Sales performance varies widely

# 2. Simplified Context of the Problem:
# - The company sales collect data from different markets
# - price of product
# - advertising budget
# - Store location (urban, rural) 


# 3. Problem Identification:
# - Uncertainity in sales performance


# 4. Business Objective:
# - Predict whether sales will be High or Low

# 5. Stakeholder Expectations:
# - Management Team: Increase revenue and profitability
# - Sales Team: Focus on high performing regions

# 6. Constraints & Limitations:
# - Data quality isuues like missing values

#7.Feasibility Check:
# - The ML model can predict the wheather sales are more than other region historic and real-time data
# - Can be integrated into business decision systems

# 8. Success Criteria
# Business Success Criteria:
# - The sales are increace other regions where sales is low

# ML Success Criteria:
# - High precision or recall for high sales prediction

#Business Impact
# - Increase customer rate
# - Increase  revenue of the company
# - Improve dicision making using data


#1 library required
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#2 Dataset load
data=pd.read_csv("C:/Assignment/EDA/Company_Data (1).csv")

#3 Basic understanding
data.columns
data.size
data.shape
data.dtypes
data.describe()

#inference
#define a column name 
#dataset szie is 4400
#dataset shape is 400 rows and 11 columns
#data type is all int64 and object
#find a min max mean mode and median for basic understanding

#4 First Moment(Mean)
mean_values=data.mean(numeric_only=True)
print("\nMean of company daaset:\n",mean_values)


#5 Second Moment (variance and std)
var_values=data.var(numeric_only=True)
print("\nVariance of company dataset:\n",var_values)

std_values=data.std(numeric_only=True)
print("\nStandard Deviation:\n",std_values)  
#inference

#6 Third moment (Skewness)
skew_values=data.skew(numeric_only=True)
print("\nSkewness of company dataset:\n",skew_values)

#inference

#7 fourth moment (kurtosis)
kurt_values=data.kurtosis(numeric_only=True)
print("\nKurtosis of comapny dataset:\n",kurt_values)

#inference

#8 Univartate analysis
#Histogram
data.drop(columns=['US']).hist(
    figsize=(12,10),
    edgecolor='Blue',
    )
plt.suptitle("Histograms of Company")
plt.tight_layout()
plt.show()

#inference 

#11Boxplot
plt.figure(figsize=(12,6))
sns.boxplot(data=data.drop(columns=['US']),orient='h')
plt.title("Boxplot of Company")
plt.show()

#inference

#12 Jointplo
sns.jointplot(data=data, x="Sales", y="Income", kind="scatter")
plt.suptitle("Joint Plot: Sales vs Income", y=1.02)
plt.show()

#inference

#13 Pairplot
sns.pairplot(data.drop(columns='US'),)
plt.suptitle("Pair Plot of All Features", y=1.02)
plt.show()

#14 Heatmap
plt.figure(figsize=(10,8))
sns.heatmap(
    data.drop(columns=['ShelveLoc']),
    annot=True,
    cmap='coolwarm',
    )
plt.title("Correlation Heatmap - company Dataset")
plt.show()

#15 PDF & CDF  
num_cols=data.select_dtypes(include=np.number).columns.drop(['Price'])

for col in num_cols:
    plt.figure(figsize=(12,5))
    
    
    #pdf
    plt.subplot(1,2,1)
    sns.kdeplot(data[col],fill=True)
    plt.title(f"PDF Of {col}")
    
    
    #CDF
    plt.subplot(1,2,2)
    sorted_vals=np.sort(data[col])
    y_vals=np.arange(len(sorted_vals)) / float(len(sorted_vals))
    plt.plot(sorted_vals,y_vals,marker='.',linestyle='None')
    plt.title(f"CDF of {col}")
    
    plt.tight_layout()
    plt.show()

#inference


#class distribution (target analusis)

sns.countplot(x=data['US'])
plt.title("Distribution of company data Types")
plt.show()    

#inference 


##################################################################


'''
dataset 4
'''
#Business understanding
# 1. Business Problem Statement:
# - The crime rate is high
# - different type of crime are happened

# 2. Simplified Context of the Problem:
# - Reduced the crime rare
# - And give dangerous punishment to crimenal


# 3. Problem Identification:
# - The law and order is loose so crimerate is high


# 4. Business Objective:
# - Predict crime rate or category
# - Improve public safety

# 5. Stakeholder Expectations:
# - Police Departments: Better patrol planning
# - Government Authorities: Reduced crime rates
# - Public: Need safety

# 6. Constraints & Limitations:
# - Crime is influenced by unpredictable human behavior

#7.Feasibility Check:
# - The ML model can predict the crimerate and criminal historic and real-time data
# - Can be integrated into policing systems

# 8. Success Criteria
# Business Success Criteria:
# - Reduced in crime rate

# ML Success Criteria:
# - High recall for high crime area

#Business Impact
# - Smarter policing strategies
# - Identification of crime hotspots
# - Faster emergency response
# - Improved public safety and trust

#1 library required
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#2 Dataset load
crime=pd.read_csv("C:/Assignment/EDA/crime_data (1).csv")

#3 Basic understanding
crime.columns
crime.size
crime.shape
crime.dtypes
crime.describe()

#inference
#define a column name 
#dataset szie is 250
#dataset shape is 50 rows and 5 columns
#data type is all int64 and float
#find a min max mean mode and median for basic understanding

#4 First Moment(Mean)
mean_values=crime.mean(numeric_only=True)
print("\nMean of Crime daaset:\n",mean_values)


#5 Second Moment (variance and std)
var_values=crime.var(numeric_only=True)
print("\nVariance of Crime dataset:\n",var_values)

std_values=crime.std(numeric_only=True)
print("\nStandard deviation of Crimr dataset:\n",std_values)

#inference

#6 Third moment (Skewness)
skew_values=crime.skew(numeric_only=True)
print("\nSkewness of Crime dataset:\n",skew_values)

#inference

#7 fourth moment (kurtosis)
kurt_values=crime.kurtosis(numeric_only=True)
print("\nKurtosis of Crime dataset:\n",kurt_values)

#inference

#8 Univartate analysis
#Histogram
crime.drop(columns=['Unnamed: 0']).hist(
    figsize=(12,10),
    edgecolor='Blue',
    )
plt.suptitle("Histograms of crime")
plt.tight_layout()
plt.show()

#inference 

#11Boxplot
plt.figure(figsize=(12,6))
sns.boxplot(data=crime.drop(columns=['Unnamed: 0']),orient='h')
plt.title("Boxplot of Crime")
plt.show()

#inference
#no outlier

#12 Jointplo
sns.jointplot(data=crime, x="Murder", y="Rape", kind="scatter")
plt.suptitle("Joint Plot: murder vs rape", y=1.02)
plt.show()

#inference

#13 Pairplot
sns.pairplot(crime.drop(columns='Unnamed: 0'),)
plt.suptitle("Pair Plot of All Features", y=1.02)
plt.show()

#14 Heatmap
plt.figure(figsize=(10,8))
sns.heatmap(
    crime.drop(columns=['Unnamed: 0']),
    annot=True,
    cmap='coolwarm'
    )
plt.title("Correlation Heatmap - Crime Dataset")
plt.show()

#15 PDF & CDF  
num_cols=crime.select_dtypes(include=np.number).columns.drop(['Rape'])

for col in num_cols:
    plt.figure(figsize=(12,5))
    
    
    #pdf
    plt.subplot(1,2,1)
    sns.kdeplot(crime[col],fill=True)
    plt.title(f"PDF Of {col}")
    
    
    #CDF
    plt.subplot(1,2,2)
    sorted_vals=np.sort(crime[col])
    y_vals=np.arange(len(sorted_vals)) / float(len(sorted_vals))
    plt.plot(sorted_vals,y_vals,marker='.',linestyle='None')
    plt.title(f"CDF of {col}")
    
    plt.tight_layout()
    plt.show()

#inference


#class distribution (target analusis)

sns.countplot(x=crime['Unnamed: 0'])
plt.title("Distribution of Crime Types")
plt.show()    

#inference 


############################################################

'''
Dataset 5
'''
#Business understanding
# 1. Business Problem Statement:
# - Detect heart disease early
# - Reduce death rate

# 2. Simplified Context of the Problem:
# - The contains of the patient health such as:
# - Age, sex, BP, Heart rate, chol, etc.


# 3. Problem Identification:
# - Due heart disease the patients are death
# - Delay diagnosis, and human error


# 4. Business Objective:
# - Build a model to predict heart disease presence

# 5. Stakeholder Expectations:
# - Doctors & Medical Staff: Faster and more accurate diagnosis
# - Hospitals: Efficient resource utilization
# - Patients: Early detection and better care

# 6. Constraints & Limitations:
# - Medical data may have missing values

#7.Feasibility Check:
# - The ML model can predict the heart disease on real-time data
# - Can be integrated into hospital decision support systems

# 8. Success Criteria
# Business Success Criteria:
# - Improve treatment efficiency

# ML Success Criteria:
# - High accuracy to detect heart disease

#Business Impact
# - Reduce patient death due to heart disease
# - Faster diagnosis
# - Reduce health cara cost


#1 library required
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#2 Dataset load
heart=pd.read_csv("C:/Assignment/EDA/heart disease (1).csv")

#3 Basic understanding
heart.columns
heart.size
heart.shape
heart.dtypes
heart.describe()

#inference
#define a column name 
#dataset szie is 4242
#dataset shape is 303 rows and 14 columns
#data type is all numeric
#find a min max mean mode and median for basic understanding

#4 First Moment(Mean)
mean_values=heart.mean(numeric_only=True)
print("\nMean of Disease daaset:\n",mean_values)


#5 Second Moment (variance and std)
var_values=heart.var(numeric_only=True)
print("\nVariance of Disease dataset:\n",var_values)

std_values=heart.std(numeric_only=True)
print("\nStandard deviation of Disease dataset:\n",std_values)

#inference

#6 Third moment (Skewness)
skew_values=heart.skew(numeric_only=True)
print("\nSkewness of Disease dataset:\n",skew_values)

#inference

#7 fourth moment (kurtosis)
kurt_values=crime.kurtosis(numeric_only=True)
print("\nKurtosis of heart disease dataset:\n",kurt_values)

#inference

#8 Univartate analysis
#Histogram
heart.drop(columns=['target']).hist(
    figsize=(12,10),
    edgecolor='Blue',
    )
plt.suptitle("Histograms of heart disease")
plt.tight_layout()
plt.show()

#inference 

#11Boxplot
plt.figure(figsize=(12,6))
sns.boxplot(data=heart.drop(columns=['target']),orient='h')
plt.title("Boxplot of heart disease")
plt.show()

#inference

#12 Jointplo
sns.jointplot(data=heart, x="trestbps", y="chol", kind="scatter")
plt.suptitle("Joint Plot: trestbps vs chol", y=1.02)
plt.show()

#inference

#13 Pairplot
sns.pairplot(heart.drop(columns='target'),)
plt.suptitle("Pair Plot of All Features", y=1.02)
plt.show()

#14 Heatmap
plt.figure(figsize=(10,8))
sns.heatmap(
    heart.drop(columns=['target']),
    annot=True,
    cmap='coolwarm',
    )
plt.title("Correlation Heatmap - heart disease Dataset")
plt.show()

#15 PDF & CDF  
num_cols=heart.select_dtypes(include=np.number).columns.drop(['target'])

for col in num_cols:
    plt.figure(figsize=(12,5))
    
    
    #pdf
    plt.subplot(1,2,1)
    sns.kdeplot(heart[col],fill=True)
    plt.title(f"PDF Of {col}")
    
    
    #CDF
    plt.subplot(1,2,2)
    sorted_vals=np.sort(heart[col])
    y_vals=np.arange(len(sorted_vals)) / float(len(sorted_vals))
    plt.plot(sorted_vals,y_vals,marker='.',linestyle='None')
    plt.title(f"CDF of {col}")
    
    plt.tight_layout()
    plt.show()

#inference


#class distribution (target analusis)

sns.countplot(x=heart['target'])
plt.title("Distribution of heart disease Types")
plt.show()    

#inference 



#####################################################################

'''
Document 6
'''
#Business understanding
# 1. Business Problem Statement:
# - Increase the fuel cost and mileage of vehicle is less

# 2. Simplified Context of the Problem:
# - The goal is to increase the mileage of vehicle

# 3. Problem Identification:
# - Low fuel efficiency in certain vehicles

# 4. Business Objective:
# - Identify the better vehicle design
# - Keep work on mileage to increase

# 5. Stakeholder Expectations:
# - Automobile Manufacturers: Design fuel-efficient cars
# - Customers: Choose cost-effective vehicles 

# 6. Constraints & Limitations:
# - To change the design and make it fuel efficient is most costly for Manufacturers

#7.Feasibility Check:
# - The ML model can helps to take decision about fuel and design historic and real-time data
# - Can be used in automotive R&D and decision-making systems

# 8. Success Criteria
# Business Success Criteria:
# - Increase customer trust on vehicle company
# - And increase sells of the vehicle

# ML Success Criteria:
# - Good prediction accuracy

#Business Impact
# - Smarter vehicle design
# -  Reduced fuel consumption
# - Lower environmental impact
# - Cost savings for customers

#EDA
#1 library required
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#2 Dataset load
car=pd.read_csv("C:/Assignment/EDA/mtcars (1).csv")

#3 Basic understanding
car.columns
car.size
car.shape
car.dtypes
car.describe()

#inference
#define a column name 
#dataset szie is 352
#dataset shape is 32 rows and 11 columns
#data type is al float and int
#find a min max mean mode and median for basic understanding

#4 First Moment(Mean)
mean_values=car.mean(numeric_only=True)
print("\nMean of cars daaset:\n",mean_values)


#5 Second Moment (variance and std)
var_values=car.var(numeric_only=True)
print("\nVariance of cars dataset:\n",var_values)

std_values=car.std(numeric_only=True)
print("\nStandard deviation of cars dataset:\n",std_values)

#inference

#6 Third moment (Skewness)
skew_values=car.skew(numeric_only=True)
print("\nSkewness of cars dataset:\n",skew_values)

#inference

#7 fourth moment (kurtosis)
kurt_values=car.kurtosis(numeric_only=True)
print("\nKurtosis of cars dataset:\n",kurt_values)

#inference

#8 Univartate analysis
#Histogram
car.drop(columns=['carb']).hist(
    figsize=(12,10),
    edgecolor='Blue',
    )
plt.suptitle("Histograms of cars")
plt.tight_layout()
plt.show()

#inference 

#11Boxplot
plt.figure(figsize=(12,6))
sns.boxplot(data=car.drop(columns=['carb']),orient='h')
plt.title("Boxplot of Cars")
plt.show()

#inference

#12 Jointplo
sns.jointplot(data=car, x="mpg", y="cyl", kind="scatter")
plt.suptitle("Joint Plot: mpg vs cyl", y=1.02)
plt.show()

#inference

#13 Pairplot
sns.pairplot(car.drop(columns='carb'),)
plt.suptitle("Pair Plot of All Features", y=1.02)
plt.show()

#14 Heatmap
plt.figure(figsize=(10,8))
sns.heatmap(
    car.drop(columns=['carb']),
    annot=True,
    cmap='coolwarm',
    numeric_only=True
    )
plt.title("Correlation Heatmap - Cars Dataset")
plt.show()

#15 PDF & CDF  
num_cols=car.select_dtypes(include=np.number).columns.drop(['carb'])

for col in num_cols:
    plt.figure(figsize=(12,5))
    
    
    #pdf
    plt.subplot(1,2,1)
    sns.kdeplot(car[col],fill=True)
    plt.title(f"PDF Of {col}")
    
    
    #CDF
    plt.subplot(1,2,2)
    sorted_vals=np.sort(car[col])
    y_vals=np.arange(len(sorted_vals)) / float(len(sorted_vals))
    plt.plot(sorted_vals,y_vals,marker='.',linestyle='None')
    plt.title(f"CDF of {col}")
    
    plt.tight_layout()
    plt.show()

#inference


#class distribution (target analusis)

sns.countplot(x=car['carb'])
plt.title("Distribution of cars Types")
plt.show()    

#inference 

################################################################

'''
Document 7
'''
#1 library required
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#2 Dataset load
air=pd.read_excel("C:/Assignment/EDA/EastWestAirlines (1).xlsx")

#3 Basic understanding
air.columns
air.size
air.shape
air.dtypes
air.describe()

#inference
#define a column name 
#dataset szie is 47988
#dataset shape is 3999 rows and 12 columns
#all data type are data  int64 
#find a min max mean mode and median values for basic understanding

#4 First Moment(Mean)
mean_values=air.mean(numeric_only=True)
print("\nMean of Airlines daaset:\n",mean_values)


#5 Second Moment (variance and std)
var_values=air.var(numeric_only=True)
print("\nVariance of Airlines dataset:\n",var_values)

std_values=air.std(numeric_only=True)
print("\nStandard deviation of Airlines dataset:\n",std_values)

#inference

#6 Third moment (Skewness)
skew_values=air.skew(numeric_only=True)
print("\nSkewness of Airlines dataset:\n",skew_values)

#inference
#only Id is negative skew
#and all columns are positive skew

#7 fourth moment (kurtosis)
kurt_values=air.kurtosis(numeric_only=True)
print("\nKurtosis of heart sisease dataset:\n",kurt_values)

#inference
#id ,cc1_miles,days_since_enroll,award is less than zero 
#and another columns is greater than zero

#8 Univartate analysis
#Histogram
air.drop(columns=['Award?']).hist(
    figsize=(12,10),
    edgecolor='Blue',
    )
plt.suptitle("Histograms of Airlines")
plt.tight_layout()
plt.show()

#inference 

#11Boxplot
plt.figure(figsize=(12,6))
sns.boxplot(data=air.drop(columns=['Award?']),orient='h')
plt.title("Boxplot of Airlines")
plt.show()

#inference
#balance columns are so many outliers
#bouns_miles are outlier
#some columns single outlier an another columns are zero

#12 Jointplo
sns.jointplot(data=air, x="Balance", y="Days_since_enroll", kind="scatter")
plt.suptitle("Joint Plot: Balance vs Days_since_enroll", y=1.02)
plt.show()

#inference

#13 Pairplot
sns.pairplot(air.drop(columns='Award?'),)
plt.suptitle("Pair Plot of All Features", y=1.02)
plt.show()

#14 Heatmap
plt.figure(figsize=(10,8))
sns.heatmap(
    air.drop(columns=['Award?']),
    annot=True,
    cmap='coolwarm',
    )
plt.title("Correlation Heatmap - Airlines Dataset")
plt.show()

#15 PDF & CDF  
num_cols=air.select_dtypes(include=np.number).columns.drop(['Award?'])

for col in num_cols:
    plt.figure(figsize=(12,5))
    
    
    #pdf
    plt.subplot(1,2,1)
    sns.kdeplot(air[col],fill=True)
    plt.title(f"PDF Of {col}")
    
    
    #CDF
    plt.subplot(1,2,2)
    sorted_vals=np.sort(air[col])
    y_vals=np.arange(len(sorted_vals)) / float(len(sorted_vals))
    plt.plot(sorted_vals,y_vals,marker='.',linestyle='None')
    plt.title(f"CDF of {col}")
    
    plt.tight_layout()
    plt.show()

#inference


#class distribution (target analusis)

sns.countplot(x=air['Award?'])
plt.title("Distribution of Crime Types")
plt.show()    

#inference 


