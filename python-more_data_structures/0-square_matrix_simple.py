#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mtrx = []
    for row in matrix:
        mtrx_2 = []
        for col in row:
            mtrx_2.append(col ** 2)
        mtrx.append(mtrx_2)
    return mtrx
