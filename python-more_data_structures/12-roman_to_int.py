#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    dictionary_romans = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    acumulador = 0
    comparador = 0

    for roman in reversed(roman_string):
        value = dictionary_romans[roman]

        if value < comparador:
            acumulador -= value
        else:
            acumulador += value

        comparador = value

    return acumulador
