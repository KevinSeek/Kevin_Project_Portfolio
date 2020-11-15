import numpy as np
import pandas as pd
import h5py as h5py
import random

def gen_sampling_titles():

    # Pull in datasets
    with pd.HDFStore('datasets/movie.hdf5') as store:
        rt = store['subset_title_ids']
        titles = store['titles_series']

    # Randomly genreate 5 titles for user to rate
    sampling_title_list = random.sample(rt.to_list(),5)

    # Filter dataframe
    st_df = titles.loc[sampling_title_list,:]

    # Rename index header name
    st_df.index.name = 'title_id'

    st_df.reset_index(inplace=True)
    
    return st_df


