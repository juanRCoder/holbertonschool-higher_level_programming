#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key_ordenado = sorted(a_dictionary)
    for i in key_ordenado:
        value = a_dictionary[i]
        print(f"{i}: {value}")
