#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lista in matrix:
        for i in lista:
            print("{:d}".format(i), end=" ")
        print()
