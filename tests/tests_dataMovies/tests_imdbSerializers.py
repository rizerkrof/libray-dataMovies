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
                'integration test',
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
            ),(
                'empty test',
                {
                    'reviews': {}
                },
                pd.DataFrame()
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

    def test_imdb_users_ratings_to_df(self):
        errors = []
        integration_sample = {"imDbId":"tt1375666","title":"Inception","fullTitle":"Inception (2010)","type":"Movie","year":"2010","totalRating":"8.8","totalRatingVotes":"0","ratings":[{"rating":"10","percent":"34.6%","votes":"805366"},{"rating":"9","percent":"30.4%","votes":"708335"},{"rating":"8","percent":"20.0%","votes":"466013"},{"rating":"7","percent":"8.5%","votes":"196995"},{"rating":"6","percent":"2.9%","votes":"67896"},{"rating":"5","percent":"1.3%","votes":"29694"},{"rating":"4","percent":"0.6%","votes":"14805"},{"rating":"3","percent":"0.4%","votes":"9517"},{"rating":"2","percent":"0.3%","votes":"7712"},{"rating":"1","percent":"0.9%","votes":"20766"}],"demographicAll":{"allAges":{"rating":"8.8","votes":"2327099"},"agesUnder18":{"rating":"9.0","votes":"1050"},"ages18To29":{"rating":"9.0","votes":"363089"},"ages30To44":{"rating":"8.8","votes":"914737"},"agesOver45":{"rating":"8.2","votes":"182612"}},"demographicMales":{"allAges":{"rating":"8.8","votes":"1271038"},"agesUnder18":{"rating":"9.1","votes":"761"},"ages18To29":{"rating":"9.0","votes":"273167"},"ages30To44":{"rating":"8.8","votes":"733408"},"agesOver45":{"rating":"8.2","votes":"149988"}},"demographicFemales":{"allAges":{"rating":"8.7","votes":"295650"},"agesUnder18":{"rating":"8.9","votes":"194"},"ages18To29":{"rating":"8.8","votes":"77053"},"ages30To44":{"rating":"8.7","votes":"165313"},"agesOver45":{"rating":"8.2","votes":"28247"}},"top1000Voters":{"rating":"8.3","votes":"911"},"usUsers":{"rating":"8.7","votes":"468075"},"nonUSUsers":{"rating":"8.8","votes":"1533308"},"errorMessage":""}
        testing_samples = [
            (
                'integration test for ratings stat',
                {
                    'users_ratings': integration_sample,
                    'stat': 'ratings'
                },
                pd.DataFrame([
                    ('10', '34.6%', '805366', 'tt1375666', 'Inception', 'Inception (2010)', 'Movie', '2010', '8.8', '0'),
                    ('9', '30.4%', '708335', 'tt1375666', 'Inception', 'Inception (2010)', 'Movie', '2010', '8.8', '0'),
                    ('8', '20.0%', '466013', 'tt1375666', 'Inception', 'Inception (2010)', 'Movie', '2010', '8.8', '0'),
                    ('7', '8.5%', '196995', 'tt1375666', 'Inception', 'Inception (2010)', 'Movie', '2010', '8.8', '0'),
                    ('6', '2.9%', '67896', 'tt1375666', 'Inception', 'Inception (2010)', 'Movie', '2010', '8.8', '0'),
                    ('5', '1.3%', '29694', 'tt1375666', 'Inception', 'Inception (2010)', 'Movie', '2010', '8.8', '0'),
                    ('4', '0.6%', '14805', 'tt1375666', 'Inception', 'Inception (2010)', 'Movie', '2010', '8.8', '0'),
                    ('3', '0.4%', '9517', 'tt1375666', 'Inception', 'Inception (2010)', 'Movie', '2010', '8.8', '0'),
                    ('2', '0.3%', '7712', 'tt1375666', 'Inception', 'Inception (2010)', 'Movie', '2010', '8.8', '0'),
                    ('1', '0.9%', '20766', 'tt1375666', 'Inception', 'Inception (2010)', 'Movie', '2010', '8.8', '0')
                ], columns=['review_rating', 'review_percent', 'review_votes', 'imDbId', 'title', 'fullTitle', 'type', 'year', 'totalRating', 'totalRatingVotes'])
            ),(
                'integration test for demographicMales stat',
                {
                    'users_ratings': integration_sample,
                    'stat': 'demographicMales'
                },
                pd.DataFrame([
                    ('allAges', '8.8', '1271038', 'tt1375666', 'Inception', 'Inception (2010)', 'Movie', '2010', '8.8', '0'),
                    ('agesUnder18', '9.1', '761', 'tt1375666', 'Inception', 'Inception (2010)', 'Movie', '2010', '8.8', '0'),
                    ('ages18To29', '9.0', '273167', 'tt1375666', 'Inception', 'Inception (2010)', 'Movie', '2010', '8.8', '0'),
                    ('ages30To44', '8.8', '733408', 'tt1375666', 'Inception', 'Inception (2010)', 'Movie', '2010', '8.8', '0'),
                    ('agesOver45', '8.2', '149988', 'tt1375666', 'Inception', 'Inception (2010)', 'Movie', '2010', '8.8', '0'),
                ], columns=['review_ageRange', 'review_rating', 'review_votes', 'imDbId', 'title', 'fullTitle', 'type', 'year', 'totalRating', 'totalRatingVotes'])
            ),(
                'integration test for demographicFemales stat',
                {
                    'users_ratings': integration_sample,
                    'stat': 'demographicFemales'
                },
                pd.DataFrame([
                    ('allAges', '8.7', '295650', 'tt1375666', 'Inception', 'Inception (2010)', 'Movie', '2010', '8.8', '0'),
                    ('agesUnder18', '8.9', '194', 'tt1375666', 'Inception', 'Inception (2010)', 'Movie', '2010', '8.8', '0'),
                    ('ages18To29', '8.8', '77053', 'tt1375666', 'Inception', 'Inception (2010)', 'Movie', '2010', '8.8', '0'),
                    ('ages30To44', '8.7', '165313', 'tt1375666', 'Inception', 'Inception (2010)', 'Movie', '2010', '8.8', '0'),
                    ('agesOver45', '8.2', '28247', 'tt1375666', 'Inception', 'Inception (2010)', 'Movie', '2010', '8.8', '0'),
                ], columns=['review_ageRange', 'review_rating', 'review_votes', 'imDbId', 'title', 'fullTitle', 'type', 'year', 'totalRating', 'totalRatingVotes'])
            ),(
                'integration test for demographicAll stat',
                {
                    'users_ratings': integration_sample,
                    'stat': 'demographicAll'
                },
                pd.DataFrame([
                    ('allAges', '8.8', '2327099', 'tt1375666', 'Inception', 'Inception (2010)', 'Movie', '2010', '8.8', '0'),
                    ('agesUnder18', '9.0', '1050', 'tt1375666', 'Inception', 'Inception (2010)', 'Movie', '2010', '8.8', '0'),
                    ('ages18To29', '9.0', '363089', 'tt1375666', 'Inception', 'Inception (2010)', 'Movie', '2010', '8.8', '0'),
                    ('ages30To44', '8.8', '914737', 'tt1375666', 'Inception', 'Inception (2010)', 'Movie', '2010', '8.8', '0'),
                    ('agesOver45', '8.2', '182612', 'tt1375666', 'Inception', 'Inception (2010)', 'Movie', '2010', '8.8', '0'),
                ], columns=['review_ageRange', 'review_rating', 'review_votes', 'imDbId', 'title', 'fullTitle', 'type', 'year', 'totalRating', 'totalRatingVotes'])
            ),(
                'empty test',
                {
                    'users_ratings': {},
                    'stat': ''
                },
                pd.DataFrame()
            )
        ]
        for sample in testing_samples:
            sampleName, arguments, targetedOutput = sample
            initialOutput = imdb_users_ratings_to_df(**arguments)
            if not ( initialOutput.equals(targetedOutput) or (initialOutput.empty and targetedOutput.empty) ):
                print(initialOutput)
                print(targetedOutput)
                errors.append(sampleName+' FAILED')

        assert not errors, "\nerrors occured in "+self.__class__.__name__+":\n{}".format("\n".join(errors))
