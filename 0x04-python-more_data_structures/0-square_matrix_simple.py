#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    new_matrix = [[new ** 2 for new in old] for old in matrix]
    return new_matrix
