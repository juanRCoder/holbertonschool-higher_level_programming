#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delete = []
    for k, v in a_dictionary.items():
        if v == value:
            delete.append(k)

    for k in delete:
        del a_dictionary[k]

    return a_dictionary
