def get_movie_id(movie):
    if not 'id' in movie:
        return ''
    return movie['id']

def get_movies_first_result(response_content):
    if not 'results' in response_content:
        return {}
    return response_content['results'][0]
