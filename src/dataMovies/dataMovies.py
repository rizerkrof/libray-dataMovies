#!/usr/bin/env python3
import pandas as pd
from .serializers.imdbSerializers import imdb_reviews_to_df
from .serializers.imdbSerializers import imdb_users_ratings_to_df
from .services.imdbService import search_movie_reviews
from .services.imdbService import search_movie_users_ratings

def search_movie_reviews_df(api_key, expression):
    """Fetch movie reviews in pandas.DataFrame() format from ImDb API.
    Args:
        api_key: a valid ImDb API token string (e.g. 'k_12345678')
        expression: search expression corresponding to your targeted movie (e.g. 'spider-man')

    Returns:
        Movie reviews in pandas.DataFrame() corresponding to searching expression.
    """
    movie_reviews = search_movie_reviews(api_key, expression)
    return imdb_reviews_to_df(movie_reviews)

def search_movies_reviews_df(api_key, expressions):
    """Fetch movies reviews in pandas.DataFrame() format from ImDb API.
    Args:
        api_key: a valid ImDb API token string (e.g. 'k_12345678')
        expressions: a list of search expressions corresponding to your targeted movies (e.g. ['inception', 'spider-man'])

    Returns:
        Movie reviews in pandas.DataFrame() corresponding to all searching expressions.
    """
    movies_reviews = [search_movie_reviews_df(api_key, expression) for expression in expressions]
    return pd.concat(movies_reviews).reset_index(drop=True)

def search_movie_users_ratings_df(api_key, expression, stat='ratings'):
    """Fetch movie users ratings in pandas.DataFrame() format from ImDb API.
    Args:
        api_key: a valid ImDb API token string (e.g. 'k_12345678')
        expression: search expression corresponding to your targeted movie (e.g. 'spider-man')
        stat (optional): string from {'ratings', 'demographicMales', 'demographicFemales', 'demographicAll'} (e.g. demographicAll)
            - 'ratings' (default): shows the rating notes distribution among all voters
            - 'demographicMales': shows ratings per age range for males
            - 'demographicFemales': shows ratings per age range for females
            - 'demographicAll': shows ratings per age range for males and females

    Returns:
        Movie users ratings in pandas.DataFrame() corresponding to searching expression regardings the stat you chose.
    """
    movie_ratings = search_movie_users_ratings(api_key, expression)
    return imdb_users_ratings_to_df(movie_ratings, stat)

def search_movies_users_ratings_df(api_key, expressions, stat='ratings'):
    """Fetch movies users ratings in pandas.DataFrame() format from ImDb API.
    Args:
        api_key: a valid ImDb API token string (e.g. 'k_12345678')
        expressions: a list of search expressions corresponding to your targeted movies (e.g. ['inception', 'spider-man'])
        stat (optional): string from {'ratings', 'demographicMales', 'demographicFemales', 'demographicAll'} (e.g. demographicAll)
            'ratings' (default): shows the rating notes distribution among all voters
            'demographicMales': shows ratings per age range for males
            'demographicFemales': shows ratings per age range for females
            'demographicAll': shows ratings per age range for males and females

    Returns:
        Movie users ratings in pandas.DataFrame() corresponding to all searching expressions regardings the stat you chose.
    """
    movies_ratings = [search_movie_users_ratings_df(api_key, expression, stat) for expression in expressions]
    return pd.concat(movies_ratings).reset_index(drop=True)
