#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    lista = sorted(a_dictionary)
    dicti = {k: a_dictionary[k] for k in lista}
    return dicti

