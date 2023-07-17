#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string == None:
        return 0
    numbers_romans = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'W' : 1000
            }
    int_value = 0
    prev_value = 0

    for roman_symbol in reversed(roman_string):
        value = numbers_romans.get(roman_symbol, 0)
        if value < prev_value:
            int_value -= value
        else:
            int_value += value
        prev_value = value
    return int_value
