#!/usr/bin/env python3

class ImdbEndPoint:
    def __init__(self, route, api_key, parameter=None):
        self.api_base_url = "https://imdb-api.com/API"
        self.api_key = api_key
        self.route = route
        self.parameter = parameter

    def value(self):
        full_end_point = self.api_base_url+'/'+self.route+'/'+self.api_key
        if self.parameter:
            full_end_point+='/'+self.parameter
        return full_end_point
