import pandas as pd
import numpy as np

# Adjust to Common Scale
def common_scale(val, new_range, pd_series):
    '''
    Function will scale element of pandas series to new range
    
    arg1 (int)    : value
    arg2 (list)  : [Min, Max]
    arg3 (series) : Pandas series to apply function to
    
    Return: the new scaled valued
    '''
    s_range = [pd_series.min(),pd_series.max()]
    return round(np.diff(new_range)[0] * ((val - s_range[0])/(np.diff(s_range)[0])) + 1,2)


# Mean Centering
def mean_center_rows(df):
    '''
    Function to normalize dataset to its mean
    
    arg1 (df): Dataframe

    return Normalized dataframe
    '''
    return (df.T - df.mean(axis=1)).T