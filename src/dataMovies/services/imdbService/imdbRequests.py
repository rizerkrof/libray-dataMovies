import requests

class ImdbRequests:
    def __init__(self):
        self.req = requests

    def get(self, url):
        return self.req.get(url)
