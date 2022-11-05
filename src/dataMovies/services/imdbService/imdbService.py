#!/usr/bin/env python3
from .imdbApiCall import ImdbApiCall
from .utils.imdbUtils import get_movie_id
from .utils.imdbUtils import get_movies_first_result

def search_movie(api_key, expression):
    movies_response = ImdbApiCall.search_movies(api_key, expression)
    movies = movies_response.content
    movie = get_movies_first_result(movies)
    return movie

def get_movie_reviews(api_key, movie):
    movie_id = get_movie_id(movie)
    reviews_reponse = ImdbApiCall.get_reviews(api_key, movie_id)
    return reviews_reponse.content

def get_movie_users_ratings(api_key, movie):
    movie_id = get_movie_id(movie)
    users_ratings_response = ImdbApiCall.get_users_ratings(api_key, movie_id)
    return users_ratings_response.content

def search_movie_reviews(api_key, expression):
    movie = search_movie(api_key, expression)
    movie_reviews = get_movie_reviews(api_key, movie)
    return movie_reviews

def search_movie_users_ratings(api_key, expression):
    movie = search_movie(api_key, expression)
    movie_users_ratings = get_movie_users_ratings(api_key, movie)
    return movie_users_ratings
