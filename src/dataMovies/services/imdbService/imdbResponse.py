from ...errors.imdbServiceErrors import ImdbResponseContentError
from ...errors.imdbServiceErrors import ImdbResponseStatusCodeError

class Response:
    """Response class used to encapsulate ImDb API response
    """
    def __init__(self, status_code, content):
        """Constructor
        Args:
            status_code: the ImDb API response status code as int (e.g. 200)
            content: the ImDb API response content as a python dictionary

        Raises:
            ImdbResponseStatusCodeError: if status code not 200
            ImdbResponseContentError: if there is an error message in response content
        """
        if status_code != 200:
            raise ImdbResponseStatusCodeError(status_code, 'Imdb response FAILED.')
        if 'errorMessage' in content and content['errorMessage'] != '':
            raise ImdbResponseContentError(content, content['errorMessage'])

        self.status_code = status_code
        self.content = content
