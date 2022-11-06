#!/usr/bin/env python3

def nested_dict_to_list(dictionary, item_to_transform, new_item_key):
    """Transform a nested python dictionary to a list of python dictionay.
    Args:
        dictionary: the python dictionary you want to transform
        item_to_transform: the item, as a string, of the dictionary you want to transform
        new_item_key: a string corresponding to the new key name that will describe all the keys of item_to_transform

    Returns:
        The transformed python dictionary.
    """
    transformedDictionary = dictionary.copy()
    if not item_to_transform in transformedDictionary:
        return transformedDictionary
    transformedDictionary[item_to_transform] = [{new_item_key: k, **v} for k, v in transformedDictionary[item_to_transform].items()]
    return transformedDictionary
