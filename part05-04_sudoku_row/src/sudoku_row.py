# Please write a function named row_correct(sudoku: list, row_no: int), which takes a two-dimensional array representing a sudoku grid, and an integer referring to a single row, as its arguments. 
# Rows are indexed from 0.

# The function should return True or False, depending on whether the row is filled in correctly, that is, whether it contains each of the numbers 1 to 9 at most once.



def row_correct(sudoku:list, row_no:int):
    row = sudoku[row_no]
    x = "" # bool variable to store True or False - depending if number appear just one time per row, or more

    for element in row: # for each element in row
        row_count = row.count(element)

        if 1 <= element <= 9: # confirm that number is between 1 and 9 - and to ignore all 0's in the row
            if row_count != 1:
                x = "False"
                break
            else:
                x = "True"
    if x == "False":
        return False
    elif x == "True":
        return True



if __name__ == "__main__":
    sudoku = [[9, 0, 0, 0, 8, 0, 3, 0, 0], [2, 0, 0, 2, 5, 0, 7, 0, 0], [0, 2, 0, 3, 0, 0, 4, 0, 4], [2, 9, 4, 0, 0, 0, 0, 0, 0], [0, 0, 0, 7, 3, 0, 5, 6, 0], [7, 0, 5, 0, 6, 0, 4, 0, 0], [0, 0, 7, 8, 0, 3, 9, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 3], [3, 0, 0, 0, 0, 0, 0, 0, 2]]

    print(row_correct(sudoku, 0))
    print(row_correct(sudoku, 1))
    print(row_correct(sudoku, 2))