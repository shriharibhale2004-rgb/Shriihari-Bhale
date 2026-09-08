# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 16:37:32 2026

@author: shrih
"""

import pandas as pd 
import numpy as np

uni1 =pd.read_excel("C:/EDA/University_Clustering.xlsx")
uni1.describe()

uni1.info()
uni = uni1.drop(["State"], axis =1)

from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale

#considering only numerical data
uni.data = uni.iloc[:,1:]
#normalization the numerical data
uni_normal=scale(uni.data)
uni_normal

pca = PCA(n_components=6)
pca_values =pca.fit_transform(uni_normal)

# the amount of variance that such pca explains is
var =pca.explained_variance_ratio_
var

#PCA weights
#pca.components_
#pca.components_[0]

#complative variance

var1 =np.cumsum(np.round(var,decimals=4)*100)
var1
#plot comulative variance
#variance plot for pca component obtained

plt.plot(var1,color="red")
#Visualizes how much variance is captured by the first few components.
##Helps to choose the optimal number of components (e.g.,
#if first 3 explain 90% variance, use 3).

pca_values
#create PCA dataframe
pca_data =pd.DataFrame(pca_values)
pca_data.columns="comp0","comp1","comp2","comp3","comp4","comp5"
#Concatenate with University Names
final=pd.concat([uni.Univ,pca_data.iloc[:,0:3]], axis =1)
#This is 'Univ' column of uni data frame
# Scatter diagram
import matplotlib.pylab as plt
ax=final.plot(x='comp0', y='comp1', kind='scatter', figsize=(12,8))
#lambda x: ax,text(*x) is equivalent to ax.text(x['compe'], x['comp1'], x['Un
              
final[['comp0','comp1','Univ']].apply(lambda x: ax.text(*x),axis=1)
# where each point text labels (university names) on a scatter plot is based on PCA components,                