#!/usr/bin/python3
def square_matrix_simple(matrix=[[]]):
    c_matrix = []
    for lista in matrix:
        new_lista = []
        for i in lista:
            new_lista.append(i * i)
        c_matrix.append(new_lista)

    return c_matrix
