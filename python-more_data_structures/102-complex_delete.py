#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not a_dictionary:
        return a_dictionary
    list_keys = list(a_dictionary.keys())
    for key in list_keys:
        if value == a_dictionary.get(key):
            del a_dictionary[key]
    return a_dictionary
