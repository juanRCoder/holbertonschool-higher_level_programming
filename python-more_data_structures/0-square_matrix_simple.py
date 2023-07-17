#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    len_matrix = len(matrix)
    for i in range(len_matrix):
        new_matrix[i] = list(map(lambda x: x**2, matrix[i]))
    return (new_matrix)
