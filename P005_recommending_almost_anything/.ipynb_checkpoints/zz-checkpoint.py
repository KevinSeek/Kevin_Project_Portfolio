

def tb_rec(movie_dim_df, users_df, user_id, title_name):
    
    
    # Find list of titles that are positively similar to the title
    title_sim = movie_dim_df[title_name].drop(title_name)
    title_sim = title_sim[title_sim > 0]
    
    # Find the weight of each title similarity
    title_weights = title_sim.values/np.sum(title_sim.values)

    # Filter by title similarity then but those that have user's rating
    user_ratings = users_df.T[user_id][title_sim.index].fillna(0)

    # Find the composite rating of the single unwatch title
    return (title_name, np.dot(user_ratings.values, title_weights)) 