#!/usr/bin/env python3
from .serializers.imdbSerializers import imdb_reviews_to_df
from .serializers.imdbSerializers import imdb_users_ratings_to_df
from .services.imdbService import search_movie_reviews
from .services.imdbService import search_movie_users_ratings

def search_movie_reviews_df(expression):
    movie_reviews = search_movie_reviews(expression)
    return imdb_reviews_to_df(movie_reviews)

def search_movie_users_ratings_df(expression, stat='ratings'):
    movie_ratings = search_movie_users_ratings(expression)
    return imdb_users_ratings_to_df(movie_ratings, stat)
