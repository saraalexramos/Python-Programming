# The function copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) takes a two-dimensional array representing a sudoku grid, 
# two integers referring to the row and column indexes of a single square, and a single digit between 1 and 9, as its arguments. 
# The function should return a copy of the original grid with the new digit added in the correct location. The function should not change the original grid received as a parameter.

import copy

def print_sudoku(sudoku:list):
    i = 0
    while i < 9:
        j = 0
        while j < 9:
            if sudoku[i][j] == 0:
                print("_", end = " ")
            if sudoku[i][j] != 0:
                print(sudoku[i][j], end = " ")
            if j == 2 or j == 5:
                print(" ", end = "")
            j += 1
        print()
        if i == 2 or i == 5:
            print()
        i += 1

def copy_and_add(sudoku: list, row_no: int, col_no: int, number: int):
    
    sudokuCopy = copy.deepcopy(sudoku)
    
    sudokuCopy[row_no][col_no] = number
    return sudokuCopy

if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)