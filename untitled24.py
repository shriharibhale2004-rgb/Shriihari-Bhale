# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 17:14:10 2026

@author: shrih
"""

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

#sample datset

transactions=[
    ['Milk','Bread','Butter'],
    ['Bread','Eggs'],
    ['Milk','Bread','Eggs','Butter'],
    ['Bread','Eggs','Butter'],
    ['Milk','Bread','Eggs']
]

#step1 convert the dataset into a format suitable for apriori
te= TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df=pd.DataFrame(te_ary,columns=te.columns_)
#

#step2 apply the apriori algo to find frequent elements

frequent_itemsets = apriori(df,min_support=0.5,use_colnames=True)

#step3 generate association rules from the frequent itemsets

rules = association_rules(frequent_itemsets, metric="lift",min_threshold=1)

#step4 output the results
print("Frequent Itemsets:")
print(rules[['antecedents','consequents','support','confidence','lift']])

##########################################################



#-------------------------------------------

