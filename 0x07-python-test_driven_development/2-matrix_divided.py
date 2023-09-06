#!/usr/bin/python3
""""2-matrix_divided"""


def matrix_divided(matrix, div):
    """Divides all elements"""
    message = "matrix must be a matrix (list of lists) of integers/floats"
    size = None
    if not isinstance(matrix, list):
        raise TypeError(message)

    for ls in matrix:
        if not isinstance(ls, list):
            raise TypeError(message)
        for item in ls:
            if not isinstance(item, (int, float)):
                raise TypeError(message)
        if size is None:
            size = len(ls)
        elif size != len(ls):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(i / div, 2) for i in r] for r in matrix]

    return new_matrix
