#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    groups = len(matrix)
    for grp in range(groups):
        for element in range(len(matrix[grp])):
            if element != 0:
                print(" ", end="")
            print("{}".format(matrix[grp][element]), end="")
        print()
