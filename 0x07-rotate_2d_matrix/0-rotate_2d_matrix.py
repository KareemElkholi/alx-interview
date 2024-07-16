#!/usr/bin/python3
"""Rotate 2D Matrix module"""


def rotate_2d_matrix(matrix):
    """rotate the matrix 90 degrees clockwise"""
    n = len(matrix)-1
    for i in range(int((n+1)/2)):
        for j in range(i, n-i):
            t = matrix[i][j]
            matrix[i][j] = matrix[n-j][i]
            matrix[n-j][i] = matrix[n-i][n-j]
            matrix[n-i][n-j] = matrix[j][n-i]
            matrix[j][n-i] = t
