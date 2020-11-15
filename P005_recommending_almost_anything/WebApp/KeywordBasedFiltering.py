import pandas as pd
import numpy as np
import h5py

#import user defined function
import scale_mean as sm

def find_similar(NN_file_loc, hdf5_file_loc, name, n = 10):
    """
    Find n most similar items (or least) to name based on embeddings. Option to also plot the results
    
    """
    
    
    # Retrieve pre-calculated title weights
    with h5py.File(NN_file_loc,'r') as hf:
        weights = hf['title_weights'][:]
        
    with pd.HDFStore(hdf5_file_loc) as store:
        idx_t_ids_dict = store['idx_title_series'].to_dict()
        index_title_dict = store['titles_series'].to_dict()['title']
    
    t_ids_idx_dict = {item : key for key,item in idx_t_ids_dict.items()}
    
    # Create a list container to hold calculated dictionary
    ls_of_dicts = []
    
    # Select index and reverse index
    index_name = 'title'
    index = t_ids_idx_dict
    rindex = idx_t_ids_dict

    # Check to make sure `name` is in index
    try:
        # Calculate dot product between book and all others
        dists = np.dot(weights, weights[index[name]])
    except KeyError:
        print(f'{name} Not Found.')
        return
    
    # Sort distance indexes from smallest to largest
    sorted_dists = np.argsort(dists)
    
    # Take the last n sorted distances; remove the title itself
    closest = sorted_dists[-(n+1):][:-1]
    
    ls_of_dicts = [{'title_id': rindex[c], 'composite_rating': dists[c]} for c in reversed(closest)]
    
    user_rec_df = pd.DataFrame(ls_of_dicts)
    
    # Map title name to title id
    user_rec_df['title'] = user_rec_df['title_id'].map(index_title_dict)
    
    return user_rec_df



def keyword_based_recommender(NN_file_loc, hdf5_file_loc, user_res, top_rec=10):
    '''
    Function to run rec algorithms 
    
    '''
    chunks = []
    for mv_id, rating in user_res.items():
        df = find_similar(NN_file_loc, hdf5_file_loc, mv_id, n = 10)
        
        # Apply weights based on user's rating
        df['composite_rating'] = df['composite_rating'] * rating/len(user_res)
        
        # Append dataframe
        chunks.append(df)

    # Concat dataframe together
    user_rec_df = pd.concat(chunks,ignore_index=True)
    
    # Apply standard scaling
    user_rec_df['composite_rating'] = user_rec_df['composite_rating'].apply(sm.common_scale, args=([1,5],user_rec_df['composite_rating']))
    
    user_rec_df.sort_values(by='composite_rating', ascending=False, inplace=True)
    user_rec_df.drop_duplicates(subset='title', keep='first', inplace=True)
    user_rec_df.reset_index(drop=True, inplace=True)
    user_rec_df = user_rec_df[['title_id', 'title', 'composite_rating']]
    
    
    return user_rec_df.head(top_rec)