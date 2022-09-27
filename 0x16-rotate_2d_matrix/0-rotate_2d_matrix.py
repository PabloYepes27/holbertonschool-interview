#!/usr/bin/python3

""" Rotate 2D Matrix 90 Degrees Clockwise"""


def rotate_2d_matrix(matrix):
    """ Function for rotating 2D Matrix 90 degrees clockwise
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    - Do not return anything. The matrix must be edited in-place.
    - You can assume the matrix will have 2 dimensions and will not be empty.
    """

    dim = len(matrix)

    for i in range(dim - 1, -1, -1):
        for j in range(dim):
            matrix[j].append(matrix[i].pop(0))
