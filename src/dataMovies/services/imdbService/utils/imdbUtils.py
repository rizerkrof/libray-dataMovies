def get_movie_id(movie):
    return movie['id']

def get_movies_first_result(response_content):
    return response_content['results'][0]
