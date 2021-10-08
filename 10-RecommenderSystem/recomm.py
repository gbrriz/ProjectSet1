import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import NMF
from sklearn.impute import KNNImputer
import random


def user_movie_ratings(html_form_data):

    movies = pd.read_csv("./data/ml-latest-small/movies.csv")
    ratings = pd.read_csv("./data/ml-latest-small/ratings.csv")
    movie_ratings = pd.merge(ratings, movies, on=['movieId'])
    user_movie_df = pd.pivot_table(movie_ratings, index='userId', columns='movieId', values='rating')

    imputer = KNNImputer(n_neighbors=5)
    imputed = imputer.fit_transform(user_movie_df)
    imputed_w_titles = pd.DataFrame(imputed, index=user_movie_df.index, columns=user_movie_df.columns)

    nmf = NMF(n_components=1, max_iter=5)
    nmf.fit(imputed_w_titles)

    Q = pd.DataFrame(nmf.components_, columns=imputed_w_titles.columns)
    P = pd.DataFrame(nmf.transform(imputed_w_titles), index=imputed_w_titles.index)

    Recommendations_in = pd.DataFrame(np.dot(P, Q), index=imputed_w_titles.index, columns=imputed_w_titles.columns)

    genre = input('Choose your genre:')
    mov = list(movies[movies['genres'].str.contains(f"{genre}")]['title'])
    movie_selection = random.sample(mov, 5)

    return movie_selection;
