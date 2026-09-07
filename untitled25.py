# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 17:38:01 2026

@author: shrih
"""

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

healthcare_data=[
    ['Fever','Cough','Covid-19'],
    ['Cough','Sore Throat','Flu'],
    ['Fever','Cough','Shoetness of Breath','Covid-19'],
    ['Cough','Sore Throat','Flu','Headache'],
    ['Fever','Body Ache','Flu'],
    ['Fever','Cough','Covid-19','Shortness of Breath'],
    ['Sore Throat','Headache','Cough'],
    ['Body Ache','Fatigue','Flu'],
   ]
#
te=TransactionEncoder()
te_ary=te.fit(healthcare_data).transform(healthcare_data)
df=pd.DataFrame(te_ary,columns=te.columns_)

#apply apriori algorithm
#
frequent_itemsets=apriori(df , min_support=0.3,use_colnames=True)
#apriori used for find frequent item sets 
#
rules =association_rules(frequent_itemsets, metric="confidence",min_threshold=0.7)

print("Frequent Itemsets")
print(frequent_itemsets)

print("\nAssociation Rules:")
print(rules[['antecedents','consequents','support','confidence','lift']])


#####################################



