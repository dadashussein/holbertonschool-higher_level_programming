#!/usr/bin/python3
"""Module divides all elements of matrix"""


def matrix_divided(matrix, div):
    """Matrix divider"""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    result = []
    for row in matrix:
        new_row = []
        for elem in row:
            new_row.append(round(elem / div, 2))
        result.append(new_row)

    return result
