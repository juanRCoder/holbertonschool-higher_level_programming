#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_ta = len(tuple_a)
    len_tb = len(tuple_b)
    if len_ta == 0:
        a1 = 0
        a2 = 0
    elif len_ta == 1:
        a1 = tuple_a[0]
        a2 = 0
    else:
        a1 = tuple_a[0]
        a2 = tuple_a[1]
    if len_tb == 0:
        b1 = 0
        b2 = 0
    elif len_tb == 1:
        b1 = tuple_b[0]
        b2 = 0
    else:
        b1 = tuple_b[0]
        b2 = tuple_b[1]
    suma = (a1 + b1, a2 + b2)
    return suma
