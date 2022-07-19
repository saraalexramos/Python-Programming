# In this exercise we will complete two more functions for the sudoku project from the previous section: print_sudoku and add_number.

# The function print_sudoku(sudoku: list) takes a two-dimensional array representing a sudoku grid as its argument. 
# The function should print out the grid in the format specified in the examples below.

# The function add_number(sudoku: list, row_no: int, column_no: int, number:int) takes a two-dimensional array representing a sudoku grid, two integers referring to the row and column indexes of a single square, and a single digit between 1 and 9, as its arguments. 
# The function should add the digit to the specified location in the grid.


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


def add_number(sudoku: list, row_no: int, col_no: int, number: int):
    sudoku[row_no][col_no] = number
    return sudoku



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

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)