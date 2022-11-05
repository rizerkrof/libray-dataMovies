#!/usr/bin/env python3

from src.dataMovies.serializers.utils.dictionaryTransform import nested_dict_to_list

import unittest

class TestDictionaryTransform(unittest.TestCase):

    def test_nested_dict_to_list(self):
        errors = []
        testing_samples = [
            (
                'simple test',
                {
                    'dictionary': {
                        'not_a_target': 'not_me_:)',
                        'target': {
                            'one' : {
                                'test1': 'one_test1',
                                'test2': 'one_test2'
                            },
                            'two' : {
                                'test1': 'two_test1',
                                'test2': 'two_test2'
                            },
                            'three' : {
                                'test1': 'three_test1',
                                'test2': 'three_test2'
                            }
                        }
                    },
                    'item_to_transform': 'target',
                    'new_item_key': 'number'
                },
                {
                    'not_a_target': 'not_me_:)',
                    'target': [
                        {
                            'number': 'one',
                            'test1': 'one_test1',
                            'test2': 'one_test2'
                        },{
                            'number': 'two',
                            'test1': 'two_test1',
                            'test2': 'two_test2'
                        },{
                            'number': 'three',
                            'test1': 'three_test1',
                            'test2': 'three_test2'
                        }
                    ]
                }
            ),(
                'empty test',
                {
                    'dictionary': {},
                    'item_to_transform': 'target',
                    'new_item_key': 'number'
                },
                {}
            )
        ]
        for sample in testing_samples:
            sampleName, arguments, targetedOutput = sample
            initialOutput = nested_dict_to_list(**arguments)
            if not ( initialOutput == targetedOutput ):
                print(initialOutput)
                print(targetedOutput)
                errors.append(sampleName+' FAILED')

        self.assertTrue(not errors, "\nerrors occured in "+self.__class__.__name__+":\n{}".format("\n".join(errors)))
