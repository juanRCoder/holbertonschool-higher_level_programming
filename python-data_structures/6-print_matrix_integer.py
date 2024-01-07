#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lista in matrix:
        for i, v in enumerate(lista):
            if i != len(lista) - 1:
                print("{:d}".format(v), end=" ")
            else:
                print("{:d}".format(v), end="")
        print()
