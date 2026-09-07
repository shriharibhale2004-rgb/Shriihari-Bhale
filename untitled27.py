# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 17:25:12 2026

@author: shrih
"""

import pandas as pd 
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
file_path="C:/recommendation system/game.csv"
data=pd.read_csv(file_path)

# user item matirx

user_item_matrix =data.pivot_table(index='userId',columns='game',values='rating')

#fill nan value with 0
user_item_matrix_filled = user_item_matrix.fillna(0)

#compute cosine similarity between users

user_similarity =cosine_similarity(user_item_matrix_filled)
user_similarity_df =pd.DataFrame(user_similarity,index=user_item_matrix.index,columns=user_item_matrix.index)

#recommendation function

def get_collaborative_recommendation_for_user(user_id,num_recommendations=5):
    #similarity scores
    similar_users=user_similarity_df[user_id].sort_values(ascending=False)
    similar_users=similar_users.drop(user_id)
    
    #top 50 most similar users
    top_similar_users=similar_users.head(50)
    
    #weighted ratings(dot product of similarity scores with rating matrix
    weighted_ratings = top_similar_users.values @ user_item_matrix_filled.loc[top_similar_users.index]
    
    #normalize by sum of similarity 
    sum_of_similarities = top_similar_users.sum()
    if sum_of_similarities > 0:
        weighted_ratings =weighted_ratings/sum_of_similarities
     #find games user has not rated
    user_ratings=user_item_matrix_filled.loc[user_id]
    unrated_games=user_ratings[user_ratings ==0]
    #select recommendations only from unrated games
    game_recommendations =pd.Series(weighted_ratings,index=user_item_matrix_filled.columns).loc[unrated_games.index]
    
    return game_recommendations.sort_values(ascending=False).head(num_recommendations)

#example usages
recommended_games=get_collaborative_recommendation_for_user(511)
print("Recommended games for user 511:")
print(recommended_games)

    