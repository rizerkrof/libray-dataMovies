#!/usr/bin/env python3
from .error import Error

class ImdbResponseStatusCodeError(Error):
    def __init__(self, status_code, message):
        """Constructor
        Args:
            status_code: the ImDb API response status code as int (e.g. 200)
            message: the error message as a string
        """
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

    def __str__(self):
        return self.message+' Response status code: '+self.status_code

class ImdbResponseContentError(Error):
    def __init__(self, content, message):
        """Constructor
        Args:
            content: the ImDb API response content as a python dictionary
            message: the error message as a string
        """
        self.message = message
        self.content = content
        super().__init__(self.message)

    def __str__(self):
        return self.message+' Response content: ', self.content
