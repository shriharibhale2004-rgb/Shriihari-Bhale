# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:38:36 2026

@author: shrih
"""

import pandas as pd
import numpy as np

#user item matrix (0=not rated ,1.5=rating) 
user_item_matrix =pd.DataFrame({
    "Game1":[5,4,0,1],
    "Game2":[3,0,4,1],
    "Game3":[0,2,5,4],
    "Game4":[1,0,4,0],
    "Game5":[0,3,0,5]
    },index=['User1','User2','User3','User4'])

print("User-Item Matrix:")
print(user_item_matrix)
#compute user similarity (cosine similarity)
from sklearn.metrics.pairwise import cosine_similarity

#compute cosine similarity between users

user_similarity =cosine_similarity(user_item_matrix)
similarity_df =pd.DataFrame(user_similarity,index=user_item_matrix.index,columns=user_item_matrix.index)
print("\nUser similarity matrix:")
print(similarity_df.round(2))

#step3 recommendation function

def recommend(user):
    #step1 find similarity user with all
    sim_users =similarity_df[user]
    #remove the user itsself (similarity with self =1 notuseful)
    sim_users=sim_users.drop(user)
    #step2 sort users by similarity high
    sim_users=sim_users.sort_values(ascending=False)
    #take top2 most similar users close
    top_users=sim_users.head(2)
    
    #step3: get ratings of thease similar users
    #we pick only those rows users from the original matrix
    top_user_ratings=user_item_matrix.loc[top_users.index]
    
    #step 4compute weighted scorre 
    #multiply ratings with similarity - more similar users influence more
    scores =np.dot(top_users.values,top_user_ratings)
    #normalize(divide by total similarity to balance scores)
    scores=scores/top_users.sum()
    
    #step5:convaert score into a labeledformat (game -score)
    scores_series=pd.Series(scores,index=user_item_matrix.columns)
    
    #step6 find games not yet rated by the user
    
    unseen = user_item_matrix.loc[user]==0
    
    #keep only those unseen games
    unseen_scores=scores_series[unseen]
    
    #step7: sort recommendation (high score best recommendation)
    
    sorted_scores=unseen_scores.sort_values(ascending=False)
    #step8 return final recommendation 
    
    return sorted_scores
#test
print(recommend('User2'))
