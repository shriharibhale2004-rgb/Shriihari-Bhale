# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 17:09:06 2026

@author: shrih
"""

import numpy as np
#sample dataset
data=[10,12,23,23,16,23,21,16]
print("Original Data", data)
#step 1: mean of data
mean=np.mean(data)
print("\nMean (Average):",mean)
#step2: maen absolute deviation from the mean
mad= np.mean([abs(x-mean)for x in data])
print("Mean Absolute deviation (mad)",mad)
#step3: varience
#it is the average of squared diff the mean
variance=np.var(data)
print("variance",variance)
#step4: standard deviation
#its the square root of the variance
std_dev=np.std(data)
print("standard deviation",std_dev)

################
# history and math test score from the image
history_scores=[75,72,68,65,67,73]
math_scores=[93,96,43,47,51,90]

def calculate_mad(scores):
    mean=sum(scores)/ len(scores)
    mad= sum(abs(x-mean)for x in scores) /len(scores)
    return mad

history_mad=calculate_mad(history_scores)
math_mad =calculate_mad(math_scores)

print("mean absolute deviation (MAD):")
print(f"history test:{history_mad:2f}")
print(f"math test:{math_mad:2f}")

'''Although both the History Test and the Math Test 
have the same average score of 70, 
their Mean Absolute Deviations (MAD) 
tell a different story.
The MAD of the History Test is lower, 
which means the scores are closer to the mean. 
The students performed more consistently, 
with less variation in their scores.
The MAD of the Math Test is much higher,
 indicating that the scores are more spread out.
 This shows greater inconsistency,
 with some students scoring very high and 
 others much lower.'''
 
 #############
import math 
#dataset 1: from left table
scores_1=[75,72,68,65,67,73]
#dataset 2
scores_2=[83,70,70,63,70,70]
def calculate_standard_deviation(scores):
    mean=sum(scores)/len(scores)
    squared_diffs=[(x-mean)** 2 for x in scores]
    varience=sum(squared_diffs)/len(scores)
    std_dev=math.sqrt(varience)
    return std_dev

std_dev_1=calculate_standard_deviation(scores_1)
std_dev_2=calculate_standard_deviation(scores_2)

print("standard deviation (population):")
print(f"dataset1:{std_dev_1:2f}")
print(f"dataset2:{std_dev_2:2f}")
'''Even though both datasets have the same MAD value, 
their standard deviations are significantly different, 
which tells us how scores are spread around the mean.'''
##############

import numpy as np
original_weights=[105,156,145,172,100]
adjusted_weights=[weight + 5 for weight in original_weights]
mean_original=np.mean(original_weights)
std_original=np.std(original_weights,ddof=1)
mean_adjusted=np.mean(adjusted_weights)
std_adjusted=np.std(adjusted_weights,ddof=1)
#ddof stands for delta degrees of freedom

print(f"Original mean:{mean_original:2f},Original std dev :{std_original:2f}")
print(f"Adjusted mean:{mean_original:2f},Adjusted std dev :{std_adjusted:2f}")

'''Addition of a Constant Affects the Mean 
but Not the Standard Deviation:
When each person wears 5 extra pounds of clothing,
 every data point increases by 5.
This increases the mean by 5 units.
Standard deviation remains unchanged 
because the spread or dispersion of data points
 does not change—only their position shifts.
Numerical Verification (from image and code):
Original Mean = 135.6
Adjusted Mean = 135.6 + 5 = 140.6
Original Standard Deviation = 31.75
Adjusted Standard Deviation = 31.75 (unchanged)''' 

###
import numpy as np 
import pylab
import scipy.stats as stats

mesurements= np.random.normal(loc=20,scale=5,size=10)
stats.probplot(mesurements,dist="norm",plot=pylab)
pylab.show()
##############
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data={'person_name':['rob','tom','xi','mohan','pooja','sofia'],
      'credit_score':[750,310,475,600,820,780],
      'income':[80000,32000,77000,65000,550000,75000],
      'age':[32,45,33,51,35,31],
      'loan_aproveed':['Y','N','Y','Y','N','N']
        }
df=pd.DataFrame(data)
df['log_income']=np.log(df['income'])

plt.figure(figsize=(10,6))

plt.bar(df['person_name'],df['income'],color='skyblue',label='original income')

plt.bar(df['person_name'],df['log_income'] * 10000,color='orange', alpha=0.7,label='log(income) x 10000')

plt.xlabel('Person_name')
plt.ylabel('Income')
plt.title('original vs log transformed income')
plt.legend()
plt.grid(True,linestyle='--',alpha=0.5)
plt.tight_layout()
plt.show()
############
'''use case; salries 
mean salary (u) = 40,000
standard deviation =10,000
we want to know:
    what percentage of data lies between 10,000and 70,000
that range is u+-    
   
    '''
#chebyshevs algorithm
def chebyshev_inequality(mu, sigma, lower_bound, upper_bound):
    k= min(abs(lower_bound-mu),abs(upper_bound-mu))/sigma
    '''Start Lower_bound = 10 upper bound = 70 Know your average
with your range (e.g., from 10k to 70k salaries):
mu= 40 (mean)
and standard deviation:
sigma = 10 (standard deviation) Find how far each bound is from the mean: distance_from_lower = |Lower_bound - mu| = |10 - 40| = 30 distance_from_upper = Jupper_bound - mu| = |70 - 40| = 30 Take the smaller of these two distances: This heeps the interval symmetric around the mean (Ltke a safe zone). min_distance = min(distance_from_lower, distance_from_upper) = 30 Convert that distance into number of standard deviations k- min_distance / sigmg m 30 / 10m 3'''

#apply cheshev inequality    
    probability=1 -(1/k**2)
    
#format the result 
    return round(probability*100,2),k 

    
mean_salary =40000
std_dev_salary=10000
lower= 10000
upper= 70000

percent,k_val=chebyshev_inequality(mean_salary,std_dev_salary,lower,upper)

print(f"According to chebyshev inequlity:")
print(f"At least {percent}% of salaries lie between ${lower}and${upper}")
print(f" this range is a{int(k_val)} standard deviation  from the mean)")