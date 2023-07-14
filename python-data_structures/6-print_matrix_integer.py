#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    groups = len(matrix)
    for i in range(groups):
        for j in range(len(matrix[i])):
            if j != 0:
                print(" ", end="")
            print("{}".format(matrix[i][j]), end="")
        print()
