# Basic pythonic library
import numpy as np
import pandas as pd
import h5py
import pickle

# Web app library
from flask import Flask, request, render_template

# User Defined files
#from .webappfuncs import genSampleTitles as gst, findNextClosestUser as ncu
import genSampleTitles as gst, findNextClosestUser as ncu, CollaborativeFiltering as cf, TitleBasedFiltering as tbf, KeywordBasedFiltering as kbf

# Current file represent my web application and create an instance of the Flask class called app
app = Flask(__name__)

# Represent default page
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/testing", methods=['GET', 'POST'])
def testing():

# Generate Sample Titles
    # define an empty variable
    sample_name = None

    if request.method == "POST":

        # Invoke function when gen_title button is clicked
        if request.form.get('gen_title') == 'title_gened':
            # call function and assign dataframe to output
            sample_df = gst.gen_sampling_titles()
            sample_name = sample_df[['title', 'genre']]

            # Save output to pickle file
            with open('datasets/nur.pickle', 'wb') as f:
                pickle.dump(sample_df,f)
            return render_template("home.html", output22 = sample_name.to_html())
        
        
# Invoke Recommendation Functions        
        # Recall random generated title for user to rate from pickle
        with open('datasets/nur.pickle','rb') as f:
            sample_df = pickle.load(f)
            sample_name = sample_df[['title','genre']]

        # Return user-ranking from text box when Submit Ranking is clicked
        if (request.form.get('rank_title') == 'title_ranked') & (not request.form['ranked_result']):
            return render_template('home.html', output22 = sample_name.to_html(), rError = 'Please rank the titles')

        else:
            # save user rating to variable
            user_input = request.form['ranked_result']
            
            # Processing of output & user_input and create a dictionary
            user_in = user_input
            user_in = [int(x) for x in user_in.split(",")]
            sample_id = sample_df['title_id'].to_list()
            user_res = dict(zip(sample_id,user_in))
            
            # Save data to pickle
            with open('datasets/user_res.pickle', 'wb') as f:
                pickle.dump(user_res,f)
            
            # Find user in database that is most similar to new user
            nearest_user = ncu.find_next_closest_user('datasets/user_res.pickle','users','datasets/movie.hdf5')
            
            # Find top five recommendation from collaborative filtering
            colab_rec = cf.cf_rec('datasets/movie.hdf5',nearest_user,5)
            colab_rec['rec_type'] = 'colab_filter'

            # Find top five recommendation from Title based filtering
            tb_rec = tbf.title_based_recommender('datasets/movie.hdf5',user_res, nearest_user,5)
            tb_rec['rec_type'] = 'tb_filter'


            # Find top five recommendation from NN-Keyword based filtering
            kbf_rec = kbf.keyword_based_recommender('datasets/movie_NN.hdf5','datasets/movie.hdf5',user_res, 5)
            kbf_rec['rec_type'] = 'kbf_filter'

            # Ensemble model Based Filter
            ensemble = colab_rec.append(tb_rec, ignore_index=True)
            ensemble = ensemble.append(kbf_rec,ignore_index=True)
            ensemble = ensemble.sort_values(by='composite_rating', ascending=False)
            ensemble.drop_duplicates(subset='title', keep='first', inplace=True)
            

            return render_template('home.html', output22=sample_name.to_html(), co_rec = colab_rec.to_html(), tb_rec = tb_rec.to_html(), kbf_rec = kbf_rec.to_html(), en_rec = ensemble.head().to_html())

# If file is run and not imported, run app; debug=True: allows possible Python errors to appear on the web page.
if __name__ == "__main__":
    app.run(debug=True)
