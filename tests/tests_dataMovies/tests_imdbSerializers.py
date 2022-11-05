#!/usr/bin/env python3
import unittest
import pandas as pd
from src.dataMovies.serializers.imdbSerializers import imdb_reviews_to_df
from src.dataMovies.serializers.imdbSerializers import imdb_users_ratings_to_df
import logging

class TestsImdbSerializers(unittest.TestCase):
    def test_imdb_reviews_to_df(self):
        errors = []
        testing_samples = [
            (
                'Simple sample test no filter',
                {
                    'reviews': {
                        "imDbId":"tt1375666",
                        "title":"Inception",
                        "fullTitle":"Inception (2010)",
                        "type":"Movie",
                        "year":"2010",
                        "items":[
                            {
                                "username":"adrien",
                                "userUrl":"https://www.imdb.com/user/ur36885175",
                                "reviewLink":"https://www.imdb.com/review/rw4692192",
                                "warningSpoilers":True,
                                "date":"1 March 2019",
                                "rate":"10",
                                "helpful":"380 out of 437 found this helpful.",
                                "title":"A one-of-a-kind mind-blowing masterpiece!",
                                "content":"My 3rd time watching this movie!"
                            },
                            {
                                "username":"srcooper",
                                "userUrl":"https://www.imdb.com/user/ur23351007",
                                "reviewLink":"https://www.imdb.com/review/rw6388098",
                                "warningSpoilers":False,
                                "date":"22 December 2020",
                                "rate":"10",
                                "helpful":"172 out of 202 found this helpful.",
                                "title":"Is it possible the makers understand how incredible this film is?",
                                "content":"You only get to watch this for the first time once."
                            },
                        ],
                        "errorMessage":""
                    }
                },
                pd.DataFrame([
                    ("adrien", "https://www.imdb.com/user/ur36885175", "https://www.imdb.com/review/rw4692192", True, "1 March 2019", "10", "380 out of 437 found this helpful.", "A one-of-a-kind mind-blowing masterpiece!","My 3rd time watching this movie!", "tt1375666", "Inception", "Inception (2010)", "Movie", "2010"),
                    ("srcooper", "https://www.imdb.com/user/ur23351007", "https://www.imdb.com/review/rw6388098", False, "22 December 2020", "10", "172 out of 202 found this helpful.", "Is it possible the makers understand how incredible this film is?", "You only get to watch this for the first time once.", "tt1375666", "Inception", "Inception (2010)", "Movie", "2010"),
                ], columns=["review_username", "review_userUrl", "review_reviewLink", "review_warningSpoilers", "review_date", "review_rate", "review_helpful", "review_title", "review_content", "imDbId", "title", "fullTitle", "type", "year"])
            )
        ]
        for sample in testing_samples:
            sampleName, arguments, targetedOutput = sample
            initialOutput = imdb_reviews_to_df(**arguments)
            if not ( initialOutput.equals(targetedOutput) or (initialOutput.empty and targetedOutput.empty) ):
                print(initialOutput)
                print(targetedOutput)
                errors.append(sampleName+' FAILED')

        assert not errors, "\nerrors occured in "+self.__class__.__name__+":\n{}".format("\n".join(errors))
