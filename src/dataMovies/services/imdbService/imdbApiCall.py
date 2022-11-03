#!/usr/bin/env python3

import os
from dotenv import load_dotenv
from .imdbResponse import Response
from .imdbRequests import ImdbRequests
from .imdbEndPoint import ImdbEndPoint
from .utils.imdbUtils import get_movies_first_result

class ImdbApiCall:
    # load_dotenv()
    # api_key=os.getenv('IMDB_API_KEY')
    api_key = 'k_12345678'
    requests = ImdbRequests()

    @classmethod
    def search_movies(cls, expression):
        endPointUrl = ImdbEndPoint('SearchMovie', cls.api_key, parameter=expression).value()
        print(endPointUrl)
        response = cls.requests.get(endPointUrl)
        return Response(status_code=response.status_code, content=response.json())

    @classmethod
    def get_users_ratings(cls, id_movie):
        endPointUrl = ImdbEndPoint('UserRatings', cls.api_key, parameter=id_movie).value()
        response = cls.requests.get(endPointUrl)
        return Response(status_code=response.status_code, content=response.json())

    @classmethod
    def get_reviews(cls, id_movie):
        endPointUrl = ImdbEndPoint('Reviews', cls.api_key, parameter=id_movie).value()
        response = cls.requests.get(endPointUrl)
        return Response(status_code=response.status_code, content=response.json())
