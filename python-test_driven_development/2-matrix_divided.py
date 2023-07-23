#!/usr/bin/python3
"""This module is composed by a function that divides the numbers of a matrix
"""


def matrix_divided(matrix, div):
    """This function divides all the elements of an array
    """
    message_error = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix or not isinstance(matrix, list):
        raise TypeError(message_error)

    len_row = len(matrix[0])
    for rows in matrix:
        if not rows or not isinstance(rows, list):
            raise TypeError(message_error)

        if len(rows) != len_row and len_row != 0:
            raise TypeError("Each row of the matrix must have the same size")

        for element in rows:
            if not isinstance(element, (int, float)):
                raise TypeError(message_error)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = list(
            map(lambda row: list(
                map(lambda element: round(element / div, 2), row)
                ), matrix)
            )
    return new_matrix
