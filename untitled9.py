# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 16:59:19 2026

@author: shrih
"""
import pandas as pd
pd.__version__
#
import pandas as pd
songs2 = pd.Series([145,142,38,13],name='counts')
#it is easy to inspect the index of a series 
songs2.index
##

songs3 = pd.Series([145,142,38,13],name='counts', index=["poul","Jhon","Gearage","ringo"])
songs3.index
songs3  
###

import pandas as pd
f1=pd.read_csv('age.csv')
f1=pd.read_csv('c:/3-python_DS/age.csv')
f1
##
df=pd.read_excel('c:/3-python_DS/Bahaman.xlsx')

##
import numpy as np
numpy_ser = np.array([145,142,38,13])


songs3[1]
#
numpy_ser[1]
#
songs3.mean()
numpy_ser.mean()
##############
#create
import pandas as pd
george= pd.Series([10,7,1,22], 
index=["1968","1969","1970","1970"], 
name='George_Songs')
george
#############
#reading the series
george["1968"]
george["1970"]

for item in george:
    print(item)
###################
#update
george["1969"]= 68
george["1969"]
george    
george["1969"]= 68
george["1969"]
george    
###############
#Delete
s=pd.Series([2,3,4],index=[1,2,3])
del s[1]
s
#############
#converting type
#
import pandas as pd
songs_66 = pd.Series([3,None,11,9],
index=['George','ringo','jhon','paul'],
name='Counts')
songs_66
songs_66.dtypes
###########
#if you want then as integer with missing values
songs_66 = pd.Series([3,None,11,9],
index=['George','ringo','jhon','paul'],
name='Counts',
dtype='Int64')

print(songs_66)
print(songs_66.dtype)
##########
#
pd.to_numeric(songs_66.apply(str))
#only numeric vale converted there is none
#error
#specialized function hust for numeric conversition

pd.to_numeric(songs_66.astype(str),errors='coerce')
#
songs_66.dtype
##
songs_66 = pd.Series([3,None,11,9],
index=['George','ringo','jhon','paul'],
name='Counts')
print(songs_66.dtype)
songs_66=songs_66.fillna(-1)
songs_66
songs_66=pd.to_numeric(songs_66.apply(str))
print(songs_66.dtype)
##
songs_66=songs_66.fillna(-1)
songs_66=songs_66.apply(str)
songs_66.dtype
#
songs_66=songs_66.fillna(-1).astype(str)
songs_66.dtype
print(songs_66.dtype)
##drop value
songs_66 = pd.Series([3,None,11,9],
index=['George','ringo','jhon','paul'],
name='Counts')
songs_66=songs_66.dropna()
songs_66
#############
songs_69=pd.Series([7,16,27,45],
index=['ram','shyam','ghanshyam','krishna'],                   
name='counts')

songs=pd.concat([songs_66,songs_69])
songs
###################
#plotting series
import matplotlib.pyplot as plt
fig=plt.figure()
songs_69.plot()
plt.legend()
###
fig=plt.figure()
songs_69.plot(kind="bar")
songs_66.plot(kind="bar",color='r')
plt.legend()
#########
import numpy as np
data= pd.Series(np.random.randn(500),name='500_random')
fig=plt.figure()
ax=fig.add_subplot(111)
data.hist()
#########
