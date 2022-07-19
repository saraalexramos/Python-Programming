# Please write a function named transpose(matrix: list), which takes a two-dimensional integer array, i.e., a matrix, as its argument. The function should transpose the matrix. Transposing means essentially flipping the matrix over its diagonal: columns become rows, and rows become columns.

# You may assume the matrix is a square matrix, so it will have an equal number of rows and columns.

import copy


def transpose (matrix: list):
    length = len(matrix[0])

    matrixCopy = copy.deepcopy(matrix)

    i = 0
    while i < length:
        j = 0
        while j < length:
            matrix[j][i] = matrixCopy[i][j]
            j += 1
        i += 1

    
    

if __name__ == "__main__":
    matrix = [[1, 2], [1, 2]]
    x = transpose(matrix)
    print(x)