#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    value = 0
    prev = 0
    for i in reversed(roman_string):
        if not isinstance(roman_string, str) or roman_string is None:
            return 0

        current = romans[i]
        if current < prev:
            value -= current
        else:
            value += current

        prev = current

    return value
