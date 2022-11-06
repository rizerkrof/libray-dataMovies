#!/usr/bin/env python3
import pandas as pd
from .utils.dictionaryTransform import nested_dict_to_list

def imdb_reviews_to_df(reviews):
    """Transform reviews to pandas.DataFrame() format.
    Args:
        reviews: a python dictionary corresponding to reviews

    Returns:
        A pandas.DataFrame() of the reviews.
    """
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
    """Transform reviews to pandas.DataFrame() format.
    Args:
        users_ratings: a python dictionary corresponding to users_ratings
        stat (optional): string from {'ratings', 'demographicMales', 'demographicFemales', 'demographicAll'} (e.g. demographicAll).
            'ratings' (default): shows the rating notes distribution among all voters.
            'demographicMales': shows ratings per age range for males.
            'demographicFemales': shows ratings per age range for females.
            'demographicAll': shows ratings per age range for males and females.

    Returns:
        A pandas.DataFrame() of the users_ratings.
    """
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
