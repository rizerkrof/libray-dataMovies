#!/usr/bin/env python3

import unittest
from src.dataMovies.services.imdbService.imdbEndPoint import ImdbEndPoint

class TestImdbEndPoint(unittest.TestCase):

    def test_value(self):
        errors = []
        testing_samples = [
            (
                'test with parameter',
                {
                    'route': 'Reviews',
                    'api_key': 'k_12345678',
                    'parameter': 'tt1375666'
                },
                'https://imdb-api.com/API/Reviews/k_12345678/tt1375666'
            ),(
                'test without parameter',
                {
                    'route': 'BoxOffice',
                    'api_key': 'k_12345678'
                },
                'https://imdb-api.com/API/BoxOffice/k_12345678'
            )
        ]
        for sample in testing_samples:
            sampleName, arguments, targetedOutput = sample
            initialOutput = ImdbEndPoint(**arguments).value()
            if not ( initialOutput == targetedOutput ):
                print(initialOutput)
                print(targetedOutput)
                errors.append(sampleName+' FAILED')

        self.assertTrue(not errors, "\nerrors occured in "+self.__class__.__name__+":\n{}".format("\n".join(errors)))
