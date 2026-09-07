# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 11:37:40 2026

@author: shrih
"""


#Dataset 1

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

#load university dataset

Univ1=pd.read_excel("C:/x-clustering/University_Clustering.xlsx")

#drop non numeric column

Univ= Univ1.drop(["State"],axis=1)

#apply standardization
scaler =StandardScaler()
df_std= pd.DataFrame(scaler.fit_transform(Univ.iloc[:,1:]),
                     columns=Univ.columns[1:])
#finding optimal K using elbow ethod (with standardized data)
TWSS=[]
k_range =list(range(2,8))

for k in k_range:
    kmeans =KMeans(n_clusters=k,random_state=42)
    kmeans.fit(df_std)
    TWSS.append(kmeans.inertia_)
    
# Plot elboe curve
plt.plot(k_range,TWSS,'ro-')
plt.xlabel("Number of clusters")
plt.ylabel("Total within sum of square (TWSS)")
plt.title("Elbow curve to determine Optimal K")
plt.show()
#apply Kmeans with optimal clusters(e.g,k=3)

model =KMeans(n_clusters=3,random_state=42)
model.fit(df_std)

#add cluster labels to the original dataset
Univ['Cluster']= model.labels_   
#rearranging columns to bring cluster first

Univ=Univ[['Cluster']+list(Univ.columns[:-1])]
#now check the Univ1 DataFrame

Univ.iloc[:,2:].groupby(Univ.Cluster).mean()

'''
Cluster 0
Feature	Value	Interpretation
SAT	1360	High SAT scores — academically strong students.
Top10	87.5%	Most students are top performers in high school.
Accept	34.5%	Selective college (low acceptance rate).
SFRatio	6.5	Very low student-faculty ratio — more personalized attention.
Expenses	$61,133	Very high expenses — likely elite, private colleges.
GradRate	84%	High graduation rate.

 Summary: This cluster represents elite, expensive, and selective institutions, likely private universities with strong academics and small class sizes.
Cluster 1
Feature	Value	Interpretation
SAT	1114	Lower SAT scores.
Top10	47%	Fewer top-performing high school students.
Accept	67.8%	High acceptance rate — less selective.
SFRatio	17.0	High student-faculty ratio — large class sizes.
Expenses	$13,385	Low cost — probably public or community colleges.
GradRate	74%	Moderate graduation rate.

Summary: This cluster likely includes public/state colleges or regional universities with lower costs, open admissions, and larger class sizes.
Cluster 2
Feature	Value	Interpretation
SAT	1309	High SAT scores — strong academics.
Top10	85.6%	High percentage of top-performing students.
Accept	29.6%	Very selective.
SFRatio	11.94	Moderate class sizes.
Expenses	$28,360	Mid-range cost.
GradRate	91.5%	Very high graduation rate.

Summary: This cluster represents prestigious but more affordable schools — possibly top public universities or scholarships-driven institutions with high performance.
'''

# Clustering Performance metrics
from sklearn.metrics import silhouette_score,davies_bouldin_score,calinski_harabasz_score

labels=model.labels_
silhouette = silhouette_score(df_std,labels)
silhouette
'''
Silhouette Score = 0.42
Range: -1 to +1

Meaning: Measures how similar points are to their own cluster vs. other clusters.

Interpretation:

0.7 – 1.0: Strong, well-separated clusters

0.5 – 0.7: Reasonable separation

0.25 – 0.5: Weak to moderate separation

< 0.25: Poor clustering

Your case (0.42):

Moderate quality — clusters are somewhat distinct but still have overlap.

This is acceptable, but not very strong — maybe some cluster boundaries aren’t crisp.

'''
db_index=davies_bouldin_score(df_std,labels)
db_index
#0.73

'''
Davies–Bouldin Index = 0.73
Range: 0 → ∞

Meaning: Lower means better separation and compactness.

Interpretation:

< 1.0: Good separation

1.0 – 2.0: Acceptable

> 2.0: Poor separation

Your case (0.73):

Very good — clusters are reasonably compact and well-separated.
'''
ch_index=calinski_harabasz_score(df_std,labels)
ch_index

'''
Calinski–Harabasz Index = 22.20
Range: No fixed max, higher is better.

Meaning: Ratio of between-cluster dispersion to within-cluster dispersion.

Interpretation:

Higher values indicate better-defined clusters.

Best used comparatively — check which k gives the highest value.

Your case (22.20):

On its own, not high or low without a baseline — compare
 with other k values to be sure.

Still indicates a fair degree of separation.
'''
################################################



#Dataset 2

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

#load university dataset

Air=pd.read_excel("C:/Assignment/K means/EastWestAirlines (2).xlsx")

#drop non numeric column

#df= Air.drop(["State"],axis=1)

#apply standardization
scaler =StandardScaler()
Air_std= pd.DataFrame(scaler.fit_transform(Air.iloc[:,1:]),columns=Air.columns[1:])
#finding optimal K using elbow ethod (with standardized data)
TWSS=[]
k_range =list(range(2,8))

for k in k_range:
    kmeans =KMeans(n_clusters=k,random_state=42)
    kmeans.fit(Air_std)
    TWSS.append(kmeans.inertia_)
    
# Plot elboe curve
plt.plot(k_range,TWSS,'ro-')
plt.xlabel("Number of clusters")
plt.ylabel("Total within sum of square (TWSS)")
plt.title("Elbow curve to determine Optimal K")
plt.show()
#apply Kmeans with optimal clusters(e.g,k=3)

model =KMeans(n_clusters=25,random_state=42)
model.fit(Air_std)

#add cluster labels to the original dataset
Air['Cluster']= model.labels_   
#rearranging columns to bring cluster first

#Air=[['Cluster']+list(Univ.columns[:-1])]
#now check the Univ1 DataFrame

Air.iloc[:,2:].groupby(Air.Cluster).mean()

'''
Cluster 0
Feature	Value	Interpretation
SAT	1360	High SAT scores — academically strong students.
Top10	87.5%	Most students are top performers in high school.
Accept	34.5%	Selective college (low acceptance rate).
SFRatio	6.5	Very low student-faculty ratio — more personalized attention.
Expenses	$61,133	Very high expenses — likely elite, private colleges.
GradRate	84%	High graduation rate.

 Summary: This cluster represents elite, expensive, and selective institutions, likely private universities with strong academics and small class sizes.
Cluster 1
Feature	Value	Interpretation
SAT	1114	Lower SAT scores.
Top10	47%	Fewer top-performing high school students.
Accept	67.8%	High acceptance rate — less selective.
SFRatio	17.0	High student-faculty ratio — large class sizes.
Expenses	$13,385	Low cost — probably public or community colleges.
GradRate	74%	Moderate graduation rate.

Summary: This cluster likely includes public/state colleges or regional universities with lower costs, open admissions, and larger class sizes.
Cluster 2
Feature	Value	Interpretation
SAT	1309	High SAT scores — strong academics.
Top10	85.6%	High percentage of top-performing students.
Accept	29.6%	Very selective.
SFRatio	11.94	Moderate class sizes.
Expenses	$28,360	Mid-range cost.
GradRate	91.5%	Very high graduation rate.

Summary: This cluster represents prestigious but more affordable schools — possibly top public universities or scholarships-driven institutions with high performance.
'''

# Clustering Performance metrics
from sklearn.metrics import silhouette_score,davies_bouldin_score,calinski_harabasz_score

labels=model.labels_
silhouette = silhouette_score(Air_std,labels)
silhouette
'''
Silhouette Score = 0.24
Range: -1 to +1

Meaning: Measures how similar points are to their own cluster vs. other clusters.

Interpretation:

0.7 – 1.0: Strong, well-separated clusters

0.5 – 0.7: Reasonable separation

0.25 – 0.5: Weak to moderate separation

< 0.25: Poor clustering

Your case (0.24):

Moderate quality — clusters are somewhat distinct but still have overlap.

This is acceptable, but not very strong — maybe some cluster boundaries aren’t crisp.

'''
db_index=davies_bouldin_score(Air_std,labels)
db_index
#1.21

'''
Davies–Bouldin Index = 1.21
Range: 0 → ∞

Meaning: Lower means better separation and compactness.

Interpretation:

< 1.0: Good separation

1.0 – 2.0: Acceptable

> 2.0: Poor separation

Your case (1.21):

Very good — clusters are reasonably compact and well-separated.
'''
ch_index=calinski_harabasz_score(Air_std,labels)
ch_index

'''
Calinski–Harabasz Index = 656.93
Range: No fixed max, higher is better.

Meaning: Ratio of between-cluster dispersion to within-cluster dispersion.

Interpretation:

Higher values indicate better-defined clusters.

Best used comparatively — check which k gives the highest value.

Your case (656.93):

On its own, not high or low without a baseline — compare
 with other k values to be sure.

Still indicates a fair degree of separation.
'''

#############################################################################################


#Dataset 3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

#load university dataset

crime=pd.read_csv("C:/Assignment/K means/crime_data (1).csv")

#drop non numeric column

crime1= crime.drop(["Unnamed: 0"],axis=1)

#apply standardization
scaler =StandardScaler()
crime_std= pd.DataFrame(scaler.fit_transform(crime1.iloc[:,1:]),columns=crime.columns[1:])
#finding optimal K using elbow ethod (with standardized data)
TWSS=[]
k_range =list(range(2,8))

for k in k_range:
    kmeans =KMeans(n_clusters=k,random_state=42)
    kmeans.fit(crime_std)
    TWSS.append(kmeans.inertia_)
    
# Plot elboe curve
plt.plot(k_range,TWSS,'ro-')
plt.xlabel("Number of clusters")
plt.ylabel("Total within sum of square (TWSS)")
plt.title("Elbow curve to determine Optimal s")
plt.show()
#apply Kmeans with optimal clusters(e.g,k=3)

model =KMeans(n_clusters=25,random_state=42)
model.fit(crime_std)

#add cluster labels to the original dataset
crime1['Cluster']= model.labels_   
#rearranging columns to bring cluster first

crime1=crime1[['Cluster']+list(crime1.columns[:-1])]
#now check the Univ1 DataFrame

crime.iloc[:,2:].groupby(crime.Cluster).mean()

'''
Cluster 0
Feature	Value	Interpretation
SAT	1360	High SAT scores — academically strong students.
Top10	87.5%	Most students are top performers in high school.
Accept	34.5%	Selective college (low acceptance rate).
SFRatio	6.5	Very low student-faculty ratio — more personalized attention.
Expenses	$61,133	Very high expenses — likely elite, private colleges.
GradRate	84%	High graduation rate.

 Summary: This cluster represents elite, expensive, and selective institutions, likely private universities with strong academics and small class sizes.
Cluster 1
Feature	Value	Interpretation
SAT	1114	Lower SAT scores.
Top10	47%	Fewer top-performing high school students.
Accept	67.8%	High acceptance rate — less selective.
SFRatio	17.0	High student-faculty ratio — large class sizes.
Expenses	$13,385	Low cost — probably public or community colleges.
GradRate	74%	Moderate graduation rate.

Summary: This cluster likely includes public/state colleges or regional universities with lower costs, open admissions, and larger class sizes.
Cluster 2
Feature	Value	Interpretation
SAT	1309	High SAT scores — strong academics.
Top10	85.6%	High percentage of top-performing students.
Accept	29.6%	Very selective.
SFRatio	11.94	Moderate class sizes.
Expenses	$28,360	Mid-range cost.
GradRate	91.5%	Very high graduation rate.

Summary: This cluster represents prestigious but more affordable schools — possibly top public universities or scholarships-driven institutions with high performance.
'''

# Clustering Performance metrics
from sklearn.metrics import silhouette_score,davies_bouldin_score,calinski_harabasz_score

labels=model.labels_
silhouette = silhouette_score(crime_std,labels)
silhouette
'''
Silhouette Score = 0.16
Range: -1 to +1

Meaning: Measures how similar points are to their own cluster vs. other clusters.

Interpretation:

0.7 – 1.0: Strong, well-separated clusters

0.5 – 0.7: Reasonable separation

0.25 – 0.5: Weak to moderate separation

< 0.25: Poor clustering

Your case (0.16):

Moderate quality — clusters are somewhat distinct but still have overlap.

This is acceptable, but not very strong — maybe some cluster boundaries aren’t crisp.

'''
db_index=davies_bouldin_score(crime_std,labels)
db_index
#0.73

'''
Davies–Bouldin Index = 0.59
Range: 0 → ∞

Meaning: Lower means better separation and compactness.

Interpretation:

< 1.0: Good separation

1.0 – 2.0: Acceptable

> 2.0: Poor separation

Your case (0.59):

Very good — clusters are reasonably compact and well-separated.
'''
ch_index=calinski_harabasz_score(crime_std,labels)
ch_index

'''
Calinski–Harabasz Index = 21.10
Range: No fixed max, higher is better.

Meaning: Ratio of between-cluster dispersion to within-cluster dispersion.

Interpretation:

Higher values indicate better-defined clusters.

Best used comparatively — check which k gives the highest value.

Your case (21.10):

On its own, not high or low without a baseline — compare
 with other k values to be sure.

Still indicates a fair degree of separation.
'''

