# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 16:40:36 2026

@author: shrih
"""

import numpy as np
from numpy import array
from scipy.linalg import svd
A=array([[1,0,0,0,2],[0,0,3,0,0],[0,4,0,0,0]])
print(A)

#svd
u,d,Vt=svd(A)
print(u)
print(d)
print(Vt)
print(np.diag(d))
#svd apply to a dataset
import pandas as pd
data=pd.read_excel("C:/EDA/University_Clustering.xlsx")
data.head()
data=data.iloc[:,2:]
data
from sklearn.decomposition import TruncatedSVD
svd=TruncatedSVD(n_component=3)
svd.fit(data)
result=pd.DataFrame(svd.transform(data))
result.head()
result.columns="pc0","pc1","pc2"
result.head()
#scatter plot
import matplotlib.pylab as plt
plt.scatter(x=result.pc0,y=result.pc1)

import pandas as pd
import matplotlib.pylab as plt
from sklearn.decomposition import TruncatedSVD

# 1. Corrected 'n_components' (it must be plural)
svd = TruncatedSVD(n_components=3)

# Assuming 'data' is your pre-defined DataFrame or array
svd.fit(data)

# 2. Transform the data and create DataFrame
result = pd.DataFrame(svd.transform(data))

# 3. Corrected column assignment (needs to be a list or tuple)
result.columns = ["pc0", "pc1", "pc2"]

# 4. Scatter plot
plt.scatter(x=result.pc0, y=result.pc1)
plt.xlabel('PC0')
plt.ylabel('PC1')
plt.title('SVD Scatter Plot')
plt.show()
