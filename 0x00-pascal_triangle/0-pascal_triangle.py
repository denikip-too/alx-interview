#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the
    Pascal’s triangle of n"""
    if n <= 0:
        return []
    list = []
    for i in range(n):
        list.append([])
        list[i].append(1)
        for j in range(1, i):
            list[i].append(list[i - 1][j - 1] + list[i - 1][j])
        if (n != 0):
            list[i].append(1)
    return (list)
