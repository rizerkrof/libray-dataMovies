#!/usr/bin/env python3

from .imdbResponse import Response
from .imdbRequests import ImdbRequests
from .imdbEndPoint import ImdbEndPoint
from .utils.imdbUtils import get_movies_first_result

class ImdbApiCall:
    requests = ImdbRequests()

    @classmethod
    def search_movies(cls, api_key, expression):
        try:
            endPointUrl = ImdbEndPoint('SearchMovie', api_key, parameter=expression).value()
            print(endPointUrl)
            response = cls.requests.get(endPointUrl)
            return Response(status_code=response.status_code, content=response.json())
        except Exception as e:
            print(e.__class__.__name__, 'as occured')
            print(e.__str__())
            return Response(status_code=response.status_code, content={})

    @classmethod
    def get_users_ratings(cls, api_key, id_movie):
        try:
            endPointUrl = ImdbEndPoint('UserRatings', api_key, parameter=id_movie).value()
            response = cls.requests.get(endPointUrl)
            return Response(status_code=response.status_code, content=response.json())
        except Exception as e:
            print(e.__class__.__name__, 'as occured')
            print(e.__str__())
            return Response(status_code=response.status_code, content={})

    @classmethod
    def get_reviews(cls, api_key, id_movie):
        try:
            endPointUrl = ImdbEndPoint('Reviews', api_key, parameter=id_movie).value()
            response = cls.requests.get(endPointUrl)
            return Response(status_code=response.status_code, content=response.json())
        except Exception as e:
            print(e.__class__.__name__, 'as occured')
            print(e.__str__())
            return Response(status_code=response.status_code, content={})
