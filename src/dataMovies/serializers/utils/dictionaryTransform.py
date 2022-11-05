#!/usr/bin/env python3

def nested_dict_to_list(dictionary, item_to_transform, new_item_key):
    transformedDictionary = dictionary.copy()
    if not item_to_transform in transformedDictionary:
        return transformedDictionary
    transformedDictionary[item_to_transform] = [{new_item_key: k, **v} for k, v in transformedDictionary[item_to_transform].items()]
    return transformedDictionary
