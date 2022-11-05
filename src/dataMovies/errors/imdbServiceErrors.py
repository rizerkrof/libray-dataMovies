#!/usr/bin/env python3
from .error import Error

class ImdbResponseStatusCodeError(Error):
    def __init__(self, status_code, message):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

    def __str__(self):
        return self.message+' Response status code: '+self.status_code

class ImdbResponseContentError(Error):
    def __init__(self, content, message):
        self.message = message
        self.content = content
        super().__init__(self.message)

    def __str__(self):
        return self.message+' Response content: ', self.content
