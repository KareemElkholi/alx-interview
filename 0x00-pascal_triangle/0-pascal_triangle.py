#!/usr/bin/python3
"""Pascal's triangle module"""


def pascal_triangle(n):
    """returns a list of lists representing the Pascal's triangle of n"""
    arr = []
    for i in range(n):
        arr.insert(i, [1]*(i+1))
        for j in range(1, int(i/2)+1):
            arr[i][j] = arr[i][i-j] = arr[i-1][j] + arr[i-1][j-1]
    return arr
