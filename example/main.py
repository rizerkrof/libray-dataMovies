#!/usr/bin/env python3

import dataMovies
import os
from dotenv import load_dotenv


load_dotenv()
api_key=os.getenv('IMDB_API_KEY')
movieSearchExpression = 'spider-man'

print(dataMovies.search_movie_users_ratings_df(api_key, movieSearchExpression))
