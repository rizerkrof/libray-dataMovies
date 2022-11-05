#!/usr/bin/env python3
import unittest
from src.dataMovies.services.imdbService.utils.imdbUtils import get_movie_id
from src.dataMovies.services.imdbService.utils.imdbUtils import get_movies_first_result

class TestImdbUtils(unittest.TestCase):

    def test_get_movie_id(self):
        errors = []
        testing_samples = [
            (
                'integration test',
                {
                    'movie':  {
                        "id":"tt1375666",
                        "resultType":"Movie",
                        "image":"https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_Ratio0.6757_AL_.jpg",
                        "title":"Inception",
                        "description":"2010 Leonardo DiCaprio, Joseph Gordon-Levitt"
                    }
                },
                'tt1375666'
            ),(
                'empty test',
                {
                    'movie': {}
                },
                ''
            )
        ]
        for sample in testing_samples:
            sampleName, arguments, targetedOutput = sample
            initialOutput = get_movie_id(**arguments)
            if not ( initialOutput == targetedOutput ):
                print(initialOutput)
                print(targetedOutput)
                errors.append(sampleName+' FAILED')

        self.assertTrue(not errors, "\nerrors occured in "+self.__class__.__name__+":\n{}".format("\n".join(errors)))

    def test_get_movies_first_result(self):
        errors = []
        testing_samples = [
            (
                'integration test',
                {
                    'response_content': {
                        "searchType":"Movie",
                        "expression":"inception",
                        "results":[
                            {
                                "id":"tt1375666",
                                "resultType":"Movie",
                                "image":"https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_Ratio0.6757_AL_.jpg",
                                "title":"Inception",
                                "description":"2010 Leonardo DiCaprio, Joseph Gordon-Levitt"
                            },
                            {
                                "id":"tt1790736",
                                "resultType":"Movie",
                                "image":"https://m.media-amazon.com/images/M/MV5BMjE0NGIwM2EtZjQxZi00ZTE5LWExN2MtNDBlMjY1ZmZkYjU3XkEyXkFqcGdeQXVyNjMwNzk3Mjk@._V1_Ratio0.6757_AL_.jpg",
                                "title":"Inception: The Cobol Job",
                                "description":"2010 Video Leonardo DiCaprio, Joseph Gordon-Levitt"
                            },
                            {
                                "id":"tt2762020",
                                "resultType":"Movie",
                                "image":"",
                                "title":"Inception of Chaos",
                                "description":"2012 Short Peter Benjamin, Matthew Bradley"
                            },
                        ],
                        "errorMessage": ""
                    }
                },
                {
                    "id":"tt1375666",
                    "resultType":"Movie",
                    "image":"https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_Ratio0.6757_AL_.jpg",
                    "title":"Inception",
                    "description":"2010 Leonardo DiCaprio, Joseph Gordon-Levitt"
                }
            ),
            (
                'empty test',
                {
                    'response_content': {}
                },
                {}
            )
        ]
        for sample in testing_samples:
            sampleName, arguments, targetedOutput = sample
            initialOutput = get_movies_first_result(**arguments)
            if not ( initialOutput == targetedOutput ):
                print(initialOutput)
                print(targetedOutput)
                errors.append(sampleName+' FAILED')

        self.assertTrue(not errors, "\nerrors occured in "+self.__class__.__name__+":\n{}".format("\n".join(errors)))
