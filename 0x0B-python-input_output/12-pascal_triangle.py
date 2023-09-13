#!/usr/bin/python3
"""One function pascal_triangle"""


def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        line = []
        if i > 0:
            line.append(1)
        for j in range(1, i):
            line.append(triangle[i - 1][j] + triangle[i - 1][j - 1])
        line.append(1)
        triangle.append(line)
    return triangle
