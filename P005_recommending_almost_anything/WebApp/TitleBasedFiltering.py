import pandas as pd
import numpy as np
import h5py

import scale_mean as sm

def title_weighter(users_df, title_sim, movies_sim, user_id, title_id):
    
    '''
    Function: Return the title name and its weights to other similar title
    
    '''
    title_sim = movies_sim[title_id].drop(title_id)
    title_sim = title_sim[title_sim > 0]
        
    # Find the weight of each title similarity
    title_weights = title_sim.values/np.sum(title_sim.values)

    # Filter by title similarity then but those that have user's rating
    user_ratings = users_df.T[user_id].loc[title_sim.index].fillna(0)

    # Find the composite rating of the single unwatch title
    return (title_id, np.dot(user_ratings.values, title_weights))





def title_based_recommender(hdf5_loc, user_res, user_id, top_rec=5):
    '''
    Function
    
    '''
    # Top_rec dataframe containers
    chunks = []
    
    # Import user rating file
    with pd.HDFStore(hdf5_loc) as store:
        movies_sim = store['movies_sim']
        users = store['users']
        index_title_dict = store['titles_series'].to_dict()['title']

    # Loop through user_response
    for mv_id, rating in user_res.items():
        
        # Find list of titles that are positively similar to the title
        title_sim = movies_sim[mv_id].drop(mv_id)
        title_sim = title_sim[title_sim > 0]
        
        # Find list of titles that are not watched by user
        #n_watch = list(users.T[user_id].loc[title_sim.index][users.T[user_id].isnull()].index)
        n_watch = list(title_sim.sort_values(ascending=False).head(20).index)

        # Return a list of recommendation for each title that user have not watch
        ls_rec = [title_weighter(users, title_sim, movies_sim, user_id, title) for title in n_watch]
                        
        # Create a dataframe of recommendations
        com_rec_df = pd.DataFrame(data=ls_rec, columns=['title_id', 'composite_rating']).sort_values(by='composite_rating', ascending=False).head(top_rec)

        # Apply User's rating weight
        com_rec_df['composite_rating'] = com_rec_df['composite_rating'] * rating/len(user_res)
        
        # Append to rec_df container
        chunks.append(com_rec_df)
    
    # Concat dataframe together
    user_rec_df = pd.concat(chunks,ignore_index=True)
    
    # Map to find the title
    user_rec_df['title'] = user_rec_df['title_id'].map(index_title_dict)
    user_rec_df = user_rec_df[['title_id', 'title','composite_rating']]
    
    # Apply standard scaling
    user_rec_df['composite_rating'] = user_rec_df['composite_rating'].apply(sm.common_scale, args=([1,5],user_rec_df['composite_rating']))
    
    # Sort & Remove Duplicates
    user_rec_df.sort_values(by='composite_rating', ascending=False, inplace=True)
    user_rec_df.drop_duplicates(subset='title', keep='first', inplace=True)
    
    # Return a dataframe of the titles recommendation
    return user_rec_df.head(top_rec)