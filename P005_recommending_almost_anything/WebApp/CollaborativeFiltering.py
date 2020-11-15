import pandas as pd
import numpy as np
import h5py
import random
from sklearn.metrics.pairwise import cosine_similarity

# import user defined functions
import scale_mean as sm

def cf_rec(hdf5_loc, user_id, top_rec=5):
    '''
    Function will put the following stored dataframe/series from HDF5, series must be in the same name: 
    1. users         => dataframe containing the user/title utility Matrix
    2. user_sim      => dataframe containing the user cosine similiarity matrix
    3. titles_series => Series of title and movie_id
    
    Arguments
    arg1 (str) : HDF5 File location
    arg2 (int) : User_id
    arg3 (int) : Top nth number of recommendation
    
    retun:
    DataFrame with movie_id, title, composite score
    '''
    
    # Import user rating file
    with pd.HDFStore(hdf5_loc) as store:
        users_sim = store['users_sim']
        users = store['users']
        index_title_dict = store['titles_series'].to_dict()['title']
    
    # Find user's similarity scores against users have positive similarity
    users_sim = users_sim[user_id].drop(user_id)
    users_sim = users_sim[users_sim > 0]
    
    # Convert user's score to weight; A 1-D array of weights
    user_weight = users_sim.values/np.sum(users_sim.values)
    
    # Find title ratings of titles which user has not rate; A 2-D array of ratings bounded by user-unwatch titles & users that are similar
    titles_rating = users.T
    titles_rating = titles_rating[titles_rating[user_id].isnull()]
    titles_rating = titles_rating.drop(user_id, axis=1)
    titles_rating = titles_rating[users_sim.index]
    
    # Find the score of titles which user has not rate; A 1-D array of composite ratings
    user_rating = np.dot(titles_rating.fillna(0).values, user_weight)
    
    # convert to a dataframe
    user_rec_df = pd.DataFrame(user_rating, index=titles_rating.index,
                               columns=['composite_rating']).sort_values(by='composite_rating', ascending=False).head(top_rec)
    
    # reset index to get movie_id as 1 of the column
    user_rec_df.reset_index(inplace=True)
    user_rec_df.rename({'movie_id':'title_id'}, axis=1, inplace=True)
    
    # Map to find the title
    user_rec_df['title'] = user_rec_df['title_id'].map(index_title_dict)
    user_rec_df = user_rec_df[['title_id', 'title','composite_rating']]
    
    # Apply Standard Rating Scaling
    user_rec_df['composite_rating'] = user_rec_df['composite_rating'].apply(sm.common_scale, args=([1,5],user_rec_df['composite_rating']))
    
    # Return a dataframe of the titles recommendation
    return user_rec_df