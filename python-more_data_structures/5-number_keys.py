#!/usr/bin/python3
def number_keys(a_dictionary):
    number = 0
    for i, _ in enumerate(a_dictionary):
        number += i
    return number
