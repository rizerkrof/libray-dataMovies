import requests

class ImdbRequests:
    """Class used to encapsulate request package
    """
    def __init__(self):
        self.req = requests

    def get(self, url):
        """Get the response from a url.
        Args:
            url: the targeted url as a string (e.g. 'https://imdb-api.com/API/BoxOffice/k_12345678')

        Returns:
            The response from the url as a python dictionary.
        """
        return self.req.get(url)
