# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 11:26:53 2026

@author: shrih
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import (
    silhouette_score,
    davies_bouldin_score,
    calinski_harabasz_score
    )

#step2 load the dataset
Univ1=pd.read_excel("C:/x-clustering/University_Clustering.xlsx")

#preview Dataset
print(Univ1.head())

#step3 basic EDA - structure check
print("\nData Types:\n", Univ1.dtypes)
print("\nShape:",Univ1.shape)
print("Size:", Univ1.size)

#step4 summary statistics

a=Univ1.describe()
print("\nSummary Statistics:\n",a)

#business moment decisions

#first moment - mean
print("\nMean:\n",Univ1.mean(numeric_only =True))

#std & variance
print("\nVariance:\n",Univ1.var(numeric_only=True) )
print("\nStd Dev:\n",Univ1.std(numeric_only=True) )

#skewness
print("\nSkewness:\n",Univ1.skew(numeric_only=True))
#kurtosis
print("\Kurtosis:\n",Univ1.kurtosis(numeric_only=True))

#step5: univariate analysis (histogram)

Univ1.select_dtypes(include="number").hist(
    figsize=(12,10),
    edgecolor="black"
    )
plt.suptitle("Histogram of University Preformance metrics")
plt.tight_layout()
plt.show() 


'''
1. SAT Scores
Most universities fall in the 1200–1400 range.
A few values around 1000–1100 → indicates some lower-tier institutions.
Distribution is slightly left-skewed (more high scores than low).

2. Top10 (% of students from top 10% of class)
Majority between 70%–100%.
Few outliers in 30%–50%.
Distribution is right-skewed toward higher values.

3. Acceptance Rate (Accept)
Spread across 15% to 90%.
Many clustered around 20%–40%.
Some very high acceptance (>70%) → less selective institutions.

4. Student-Faculty Ratio (SFRatio)
Concentrated around 10–15.
Few extreme values (up to ~25).
Fairly normal distribution with slight right tail.

5. Expenses
Wide range from ~4000 to 20000+.
Slight clustering in mid-range (~8000–15000).
Presence of high-cost outliers.

6. Graduation Rate (GradRate)
Mostly between 70%–100%.
Few lower values (~50–60%).
Slight left skew (more high values).

'''
#step 6 outlier analysis(boxplot)

plt.figure(figsize=(12,6))
Univ1.select_dtypes(include="number").boxplot(vert=False)
plt.title("Boxplot - University Performance Indicators")
plt.show() 

'''
1. SAT
Narrow box → low variability.
Few mild outliers.
2. Top10
Compact distribution.
Slight presence of lower-value outliers.
3. Acceptance Rate (Accept)
Wider spread compared to Top10.
Some outliers on higher side.
4. Student-Faculty Ratio (SFRatio)
Moderate spread.
A few high-value outliers.

5. Expenses
Largest spread among all variables.
Long whiskers + extreme values.
Median around mid-range.
Inference:
Huge variation in cost → from affordable to very expensive institutions
Presence of premium/high-cost outliers

6. Graduation Rate (GradRate)
Compact distribution toward higher values.
Few low outliers.

'''
#step 7 : data preprocessing
#Drop categorical column "state
Univ=Univ1.drop(['State'], axis=1)

#seperate identifiers 
Univ_names = Univ.iloc[:,0]

#keep only numerical data
Univ_num=Univ.iloc[:,1:]

#step8 normalization (min max)

#distance based algorithm require normalization
def norm_func(i):
    return (i - i.min())/ (i.max()-i.min())
df_norm = norm_func(Univ_num)

#verify normalization
print("\nNormalized Data Summary:\n", df_norm.describe())

#step9 dendogram(cluster tendency)

z=linkage(
    df_norm,
    method="complete",
    metric="euclidean"
)
plt.figure(figsize=(15,8))
plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("University Index")
plt.ylabel("Distance")
dendrogram(z, leaf_rotation=40, leaf_font_size=10)
plt.show()
#step10 :Agglomerative clustering model

h_complete =AgglomerativeClustering(
    n_clusters=3,
    linkage="complete",
    metric="euclidean"
    )
cluster_labels =h_complete.fit_predict(df_norm)

#attach cluster labels
Univ["clust"] =cluster_labels

#step11 cluster profiling

Univ_clustered =Univ.iloc[:,[7,1,2,3,4,5,6]]

cluster_summary = Univ_clustered.iloc[:,1:].groupby(Univ_clustered.clust).mean()

print("\nCluster-wise mean profile:\n",cluster_summary)
#
#step 12 cluster validation metrics

silhouette =silhouette_score(df_norm, cluster_labels)
db_index=davies_bouldin_score(df_norm, cluster_labels)
ch_index=calinski_harabasz_score(df_norm,cluster_labels)

print("\n---Clustering performance metrics--")
print(f"Silhouette Score   :{silhouette:.4f}")

'''
Silhouette Score = 0.2930
Range: -1 to +1

Meaning: Measures how similar points are to their own cluster vs. other clusters.

Interpretation:

0.7 – 1.0: Strong, well-separated clusters

0.5 – 0.7: Reasonable separation

0.25 – 0.5: Weak to moderate separation

< 0.25: Poor clustering

In this case (0.2930):

Moderate quality — clusters are somewhat distinct but still have overlap.

This is acceptable, but not very strong — maybe some cluster boundaries aren’t crisp.

'''

print(f"Davies-Bouldin Index  : {db_index:.4f}")

'''
Davies–Bouldin Index = 1.0286
Range: 0 → ∞

Meaning: Lower means better separation and compactness.

Interpretation:

< 1.0: Good separation

1.0 – 2.0: Acceptable

> 2.0: Poor separation

In this case 1.0286:

Acceptable — clusters are reasonably compact and well-separated.
'''
print(f"Calinski-Harabasz Index :{ch_index:.4f}")

'''
Calinski–Harabasz Index = 24.6202
Range: No fixed max, higher is better.

Meaning: Ratio of between-cluster dispersion to within-cluster dispersion.

Interpretation:

Higher values indicate better-defined clusters.

Best used comparatively — check which k gives the highest value.

In this case (24.6202):

On its own, not high or low without a baseline — compare
 with other k values to be sure.

Still indicates a fair degree of separation.

'''
#step 13 : export results

Univ_clustered.to_csv("University.csv",encoding="utf-8",index=False) 
import os
print("\nWorking Directiory")

'''
Cluster 0 – Upper-Mid Tier Universities
• Strong academics
• Moderate selectivity
• Balanced cost and outcomes

Cluster 1 – Developing / Mass Universities
• High acceptance
• Lower expenses
• Moderate graduation rates

Cluster 2 – Elite Universities
• Highly selective
• Low student–faculty ratio
• High expenses and outcomes

Business Value:
• Enables benchmarking
• Supports funding & accreditation decisions
• Identifies peer institutions
'''