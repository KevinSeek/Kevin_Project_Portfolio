# Import Library
import numpy as np
import pandas as pd
import h5py as h5py
import pickle
from sklearn.metrics.pairwise import cosine_similarity

# import user defined functions
#from webappfuncs import scale_mean as sm
import scale_mean as sm

def find_next_closest_user(user_res_loc, users_df_name, users_loc):

    '''
    Function to find next closest user in database similar to new user
    '''
    
    with open(user_res_loc,'rb') as f:
        user_res = pickle.load(f)
    
    with pd.HDFStore(users_loc) as store:
        users = store[users_df_name]

    # Create a user series with index as -1 and append to user-title matrix
    to_append = pd.Series(data=user_res, index=user_res,name=-1)

    # Make a copy so as not to contiminate original dataframe; append to user-title matrix
    user1 = users.copy()

    # Filter titles to only those that are in user_res
    user1 = user1[list(user_res.keys())]

    # append new user-ratings into matrix
    user1 = user1.append(to_append)

    # Drop users that have no ratings for ALL titles in user_res
    user1 = user1[list(user_res.keys())].dropna(axis=0, how='all')

    # Mean Centering the ratings
    user1_mc = sm.mean_center_rows(user1)
    user1_mc = user1_mc.fillna(0)

    # Create User sim matrix
    user1_sim = cosine_similarity(user1_mc)
    user1_sim = pd.DataFrame(user1_sim, columns=user1_mc.index, index = user1_mc.index)

    # Find the next most similar user to user other than user
    next_sim = user1_sim[[-1]].sort_values(by=-1, ascending=False).iloc[1].name

    return next_sim