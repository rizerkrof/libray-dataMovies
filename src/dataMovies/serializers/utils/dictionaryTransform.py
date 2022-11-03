#!/usr/bin/env python3

def nested_dict_to_list(dictionary, item_to_transform, new_item_key):
    dictionary[item_to_transform] = [{new_item_key: k, **v} for k, v in dictionary[item_to_transform].items()]
    return dictionary