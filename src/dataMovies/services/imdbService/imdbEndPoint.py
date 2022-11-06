#!/usr/bin/env python3

class ImdbEndPoint:
    """Class use to generalize ImDb API end points
    """
    def __init__(self, route, api_key, parameter=None):
        """Constructor
        Args:
            route: the ImDb API route path of your request as a string (e.g. 'SearchMovie')
            api_key: a valid ImDb API token string (e.g. 'k_12345678')
            paramter (optional): a string corresponding to the route parameters (e.g. 'tt0145487')
        """
        self.api_base_url = "https://imdb-api.com/API"
        self.api_key = api_key
        self.route = route
        self.parameter = parameter

    def value(self):
        """The full end point url.
        Returns:
            The full Imdb API url of your request as a string.
        """
        full_end_point = self.api_base_url+'/'+self.route+'/'+self.api_key
        if self.parameter:
            full_end_point+='/'+self.parameter
        return full_end_point
