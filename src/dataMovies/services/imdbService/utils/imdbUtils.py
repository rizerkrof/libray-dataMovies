def get_movie_id(movie):
    """Get the id from a movie.
    Args:
        movie: a python dictionary corresponding to your targeted movie (e.g. the return of the search_movie() function)

    Returns:
        The movie id as a string.
    """
    if not 'id' in movie:
        return ''
    return movie['id']

def get_movies_first_result(response_content):
    """Get the first result from movie results list.
    Args:
        response_content: a python dictionary corresponding to the ImDb API response content

    Returns:
        The first/best movie in the results list as a python dictionary.
    """
    if not 'results' in response_content:
        return {}
    return response_content['results'][0]
