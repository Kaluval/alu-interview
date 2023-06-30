#!/usr/bin/python3
"""
pascal's triangle
"""


def pascal_triangle(n):
    """get pascal triangle to a certain index"""
    if n <= 0:
        return []
    result = [[1], [1, 1]]
    for i in range(2, n):
        list_above = [0] + result[i - 1] + [0]
        row = []
        for j in range(0, len(list_above) - 1):
            row.append(list_above[j] + list_above[j + 1])
        result.append(row)
    return result[:n]
