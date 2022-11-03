#!/usr/bin/env python3
from .imdbApiCall import ImdbApiCall
from .utils.imdbUtils import get_movie_id
from .utils.imdbUtils import get_movies_first_result

def search_movie(expression):
    movies_response = ImdbApiCall.search_movies(expression)
    movies = movies_response.content
    movie = get_movies_first_result(movies)
    return movie

def get_movie_reviews(movie):
    movie_id = get_movie_id(movie)
    reviews_reponse = ImdbApiCall.get_reviews(movie_id)
    return reviews_reponse.content

def get_movie_users_ratings(movie):
    movie_id = get_movie_id(movie)
    users_ratings_response = ImdbApiCall.get_users_ratings(movie_id)
    return users_ratings_response.content

def search_movie_reviews(expression):
    movie = search_movie(expression)
    movie_reviews = get_movie_reviews(movie)
    return movie_reviews

def search_movie_users_ratings(expression):
    movie = search_movie(expression)
    movie_users_ratings = get_movie_users_ratings(movie)
    return movie_users_ratings
