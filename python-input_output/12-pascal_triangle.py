#!/usr/bin/python3
"""Document for module"""


def pascal_triangle(n):
    """Document for method"""
    if n <= 0:
        return []
    triangle = [[1]]
    for _ in range(1, n):
        row = [1]
        for i in range(1, len(triangle[-1])):
            row.append(triangle[-1][i - 1] + triangle[-1][i])
        row.append(1)
        triangle.append(row)
    return triangle
