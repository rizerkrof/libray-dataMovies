from ...errors.imdbServiceErrors import ImdbResponseContentError
from ...errors.imdbServiceErrors import ImdbResponseStatusCodeError

class Response:
    def __init__(self, status_code, content):
        if status_code != 200:
            raise ImdbResponseStatusCodeError(status_code, 'Imdb response FAILED.')
        if 'errorMessage' in content and content['errorMessage'] != '':
            raise ImdbResponseContentError(content, content['errorMessage'])

        self.status_code = status_code
        self.content = content
