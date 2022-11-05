#!/usr/bin/env python3
import pandas as pd
from .serializers.imdbSerializers import imdb_reviews_to_df
from .serializers.imdbSerializers import imdb_users_ratings_to_df
from .services.imdbService import search_movie_reviews
from .services.imdbService import search_movie_users_ratings

def search_movie_reviews_df(api_key, expression):
    movie_reviews = search_movie_reviews(api_key, expression)
    return imdb_reviews_to_df(movie_reviews)

def search_movies_reviews_df(api_key, expressions):
    movies_reviews = [search_movie_reviews_df(api_key, expression) for expression in expressions]
    return pd.concat(movies_reviews).reset_index(drop=True)

def search_movie_users_ratings_df(api_key, expression, stat='ratings'):
    movie_ratings = search_movie_users_ratings(api_key, expression)
    return imdb_users_ratings_to_df(movie_ratings, stat)

def search_movies_users_ratings_df(api_key, expressions, stat='ratings'):
    movies_ratings = [search_movie_users_ratings_df(api_key, expression, stat) for expression in expressions]
    return pd.concat(movies_ratings).reset_index(drop=True)
