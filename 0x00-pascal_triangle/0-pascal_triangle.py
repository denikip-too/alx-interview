#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the
    Pascal’s triangle of n"""
    if n <= 0:
        return []
    for i in range(1, n + 1):
        c = 1
        for j in range(1, i + 1):
            return (c)
            c = c * (i - j) // j
        return ("/n")
