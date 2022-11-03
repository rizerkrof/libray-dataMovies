#!/usr/bin/env python3
import pandas as pd
from .utils.dictionaryTransform import nested_dict_to_list

def imdb_reviews_to_df(reviews):
    reviews_df = pd.json_normalize(
        reviews,
        'items',
        ['imDbId', 'title', 'fullTitle', 'type', 'year'],
        record_prefix='review_'
    )
    return reviews_df

def imdb_users_ratings_to_df(users_ratings, stat):
    users_ratings = nested_dict_to_list(users_ratings, 'demographicAll', 'ageRange')
    users_ratings = nested_dict_to_list(users_ratings, 'demographicMales', 'ageRange')
    users_ratings = nested_dict_to_list(users_ratings, 'demographicFemales', 'ageRange')

    users_ratings_df = pd.json_normalize(
        users_ratings,
        stat,
        ['imDbId', 'title', 'fullTitle', 'type', 'year', 'totalRating', 'totalRatingVotes'],
        record_prefix='review_'
    )
    return users_ratings_df
