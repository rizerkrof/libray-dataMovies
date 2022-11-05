#!/usr/bin/env python3
import pandas as pd
from .utils.dictionaryTransform import nested_dict_to_list

def imdb_reviews_to_df(reviews):
    features = ['items', 'imDbId', 'title', 'fullTitle', 'type', 'year']
    if not all(feature in reviews for feature in features):
        return pd.DataFrame()

    reviews_df = pd.json_normalize(
        reviews,
        features[0],
        features[1:],
        record_prefix='review_'
    )
    return reviews_df

def imdb_users_ratings_to_df(users_ratings, stat):
    features = ['imDbId', 'title', 'fullTitle', 'type', 'year', 'totalRating', 'totalRatingVotes', 'ratings', 'demographicAll', 'demographicMales', 'demographicFemales', stat]
    if not all(feature in users_ratings for feature in features):
        return pd.DataFrame()

    users_ratings = nested_dict_to_list(users_ratings, 'demographicAll', 'ageRange')
    users_ratings = nested_dict_to_list(users_ratings, 'demographicMales', 'ageRange')
    users_ratings = nested_dict_to_list(users_ratings, 'demographicFemales', 'ageRange')

    users_ratings_df = pd.json_normalize(
        users_ratings,
        stat,
        features[:7],
        record_prefix='review_'
    )
    return users_ratings_df
