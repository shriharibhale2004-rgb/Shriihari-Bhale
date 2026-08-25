# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 17:08:33 2026

@author: shrih
"""
##mean < median data left
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
import numpy as np
from scipy.stats import gaussian_kde

tips=sns.load_dataset('tips')

#
tips.describe()
#distribution of total bill amounts
sns.displot(tips.total_bill)
#distribution of total bill with  kde(Kernel Density Estiment)
sns.displot(tips.total_bill,kde=True)
##########
#interpretation
#the distribution is right skewed (positively skewed)
#most total bills are concentrated at lower values 10$ to 25$
#a few very large bills stretch the tail to the right
#this is comman in service /Restrarent data
#most customers spend moderately a few spend heavily

#distribution of tip amounts with kde
sns.displot(tips.tip,kde=True)

#joint plots
#scater plot with marginal histogram
sns.jointplot(x=tips.tip,y=tips.total_bill)
#scater plot with regression line
sns.jointplot(x=tips.tip,y=tips.total_bill,kind='reg')
#joint plot interpretation
#center 
#each point represent one customer  visit
#x axis tip amount 
#y axis total bill
#clear positive relationship as total bill increase tip generally increase

#regression line
#shows overall trend 
#relation ship is positive but not  perfectly linear
#variability increase for higher bills

#######################

#hexbin joint plot for density based visual
sns.jointplot(x=tips.tip,y=tips.total_bill,kind='hex')
#
sns.pairplot(tips,kind='reg')
##
#pairplot insights

#total bill vs tips:
#strong positive correlation 
#higher bills generally receive higher tips

#total bill vs size
#weak to modrate positive correlation
#larger groups tend to generate higher bills
#small groups can also have high bills
#tip vs size
#weak correlation
#larger groups donot always leave higher tips
#most tips still cluster around $2$5
###############
#pairplot with hue time
sns.pairplot(tips,hue='time')   
#
#insights by time of visit :
#dinner bills are generally higher than lunch bills 
#dinner bills are more concentrateed at lower values

#group size:
#dinner groups tend to be larger 
#lunch groups are mostly size 2
#relationship:
#positive total bill vs tip relationship exits for both
#dinner shows more extream high bill high tip cases 
####
sns.pairplot(tips,hue='day')   
##
#day size isights
# tital bill:
    # saturday shows highest spendingn and spread
    #friday has fewer observation and lower spending
#tips:
#higher tips are more frequent an saturday and sunday
#trusday and friday show fewer high tips 

#group size
#most groups are size 2-3 across all days
#larger groups 5-6 appear mostly on weekends
########################
#heatmap 
sns.heatmap(tips.corr(numeric_only=True),annot=True)    
#correlation interpretation
#correlation values range from -1to1
#total bill and tip(-0,68)
#strong positive correltion
#larger bills generally lead to higher tips

#total bill and size(-0,60)
#modrate positive correlation 
#larger groups tend to order more

#tipand size(-0.49)
#modrate correlation
#group size affects tips but not as strongly as bill amount
#############
#boxplot outlier detection
sns.boxplot(tips.total_bill)
#shoes several high value outliers very expensive meals
sns.boxplot(tips.tip)
#shows tip outlier unusally high  tips
####################
#count plot
sns.countplot(x=tips.day)
#most of customers are coming on sat aand sun there is considrable strength
#very few customer are coming in friday
sns.countplot(x=tips.sex)
#more male customers than female customers

#pie and bar chart

tips.sex.value_counts().plot(kind='pie',autopct='%1.1f%%')
tips.sex.value_counts().plot(kind='bar')

#########
#time wise day anlysis
sns.countplot(data=tips[tips.time=='Dinner'],x='day')
#dinner is most popular as saturday and sunday
sns.countplot(data=tips[tips.time=='Lunch'],x='day')
#lunch accours mostly on thrusday and friday

##########

fig=sns.FacetGrid(tips, row='smoker',col='time')
fig.map(sns.histplot,'total_bill')
##
#tips=dataset
#row=smoker seperate row for
#smoker=yes 
#smoker =no
#col=time seperate columns for
#lunch 
#dinner

#facetgrid intrepretation
#panels

###########

##matplotlib implementation

#histogram of total bill eith plt
plt.hist(tips['total_bill'],bins=20,edgecolor='black')
plt.title('Total Bill Disttibution')
plt.xlabel('Total Bill')
plt.ylabel('count')
plt.show()

###################
#kde using scipy

data=tips['total_bill']

density=gaussian_kde(data)
x=np.linspace(min(data),max(data),200)
y=density(x)

plt.hist(data,bins=20,density=True,alpha=0.6, edgecolar='black')
plt.plot(x,y,linewidth=2)
plt.title('Total Bill Disttibution eith density curve')
plt.xlabel('Total Bill')
plt.ylabel('Density')
plt.show()

#################
#tip distribution
plt.hist(tips['tip'],bins=20,edgecolo='black')
plt.title('Tip Distribution')
plt.xlabel('Tip')
plt.ylabel('Count')
plt.show()
###
#scatter plot
plt.scatter(tips['tip'],tips['total_bill'],alpha=0.6)
plt.title('Tip vs Total Bill')
plt.xlabel('Tip')
plt.ylabel('Total Bill')
plt.show()
######
#correlation matrix heat map
corr=tips.corr(numeric_only=True)
corr
plt.imshow(corr,interpolation='none')
plt.colorbar()
plt.xticks(range(len(corr)),corr.column,rotation=45)
plt.yticks(range(len(corr)),corr.column)
plt.title('Correlation matrix')
plt.show()
########
#boxplots
plt.boxplot(tips['total_bill'])
plt.title('Boxplot - Total Bill')
plt.show()

plt.boxplot(tips['tip'])
plt.title('Boxplot-Tip')
plt.show()

##############
#bar and pie chart

tips['day'].value_counts().plot(kind='bar')
plt.title('count by day')
plt.show()

tips['sex'].value_counts().plot(kind='bar')
plt.title('count by gender')
plt.show()

tips['sex'].value_counts().plot(kind='pie',autopct='%1.1f%%')
plt.title('Gender distrbution')
plt.ylabel('')
plt.show()