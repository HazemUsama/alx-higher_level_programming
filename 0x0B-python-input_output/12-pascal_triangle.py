#!/usr/bin/python3
"""One function pascal_triangle"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        line = [1]
        for j in range(i - 1):
            line.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
        line.append(1)
        triangle.append(line)
    return triangle
