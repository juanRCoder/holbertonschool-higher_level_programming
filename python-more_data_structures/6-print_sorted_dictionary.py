#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if isinstance(a_dictionary, dict):
        order = sorted(a_dictionary.keys())
        for k in order:
            print(f"{k}: {a_dictionary[k]}")
    else:
        pass