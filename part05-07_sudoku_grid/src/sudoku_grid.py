# Please write a function named sudoku_grid_correct(sudoku: list), which takes a two-dimensional array representing a sudoku grid as its argument. 
# The function should use the functions from the three previous exercises to determine whether the complete sudoku grid is filled in correctly. 
# Copy the functions from the exercises above into your Python code file for this exercise.

# The function should check each of the nine rows, columns and 3 by 3 blocks in the grid. 
# If all contain each of the numbers 1 to 9 at most once, the function returns True. If a single one is filled in incorrectly, the function returns False.

# The image of a sudoku grid above these exercises has the nine blocks within the grid indicated with thicker borders.
#  These are the blocks the function should check, and they begin at the indexes (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3) and (6, 6).

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

def column_correct(sudoku:list, column_no:int):
    elements_in_col = [] # a list to stored elements in the column
    x = "" # a helper variable to store True/ False depending if number appear just one time per row, or more  
    
    for row in sudoku:
        #"print("r", row)
        elements_in_col.append(row[column_no])
        #print("e", elements_in_col)

        for element in elements_in_col:
            count_elements = elements_in_col.count(element)
            if 1 <= element <= 9:
                
                if count_elements == 1:
                    x = True
                else:
                    x = False
                    break

    return x

def block_correct(sudoku:list, row_no:int, col_no:int):
    elements_in_block = [] # list to store elements in block 
    x = "" # a helper variable to store True/ False depending if number appear just one time per row, or more  

    for row in sudoku[row_no:(row_no + 3)]:
        for col in row[col_no:(col_no + 3)]:
            elements_in_block.append(col)

    for element in elements_in_block:
        count = elements_in_block.count(element)
        if 1 <= element <= 9:
            if count == 1:
                x = True
            elif count != 1:
                x = False
                break
    return x


def sudoku_grid_correct(sudoku:list):
    
    for row in range (9):
        status = row_correct(sudoku, row)
        if status == False:
            return False
            break

    for col in range (9):
        status = column_correct(sudoku, col)
        if status == False:
            return False
            break
    
    grids = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]
    
    for grid in grids:
        status = block_correct(sudoku, grid[0], grid[1])
        if status == False:
            return False
            break

    return True




if __name__ == "__main__":
    sudoku1 = [[9, 0, 0, 0, 8, 0, 3, 0, 0],[2, 0, 0, 2, 5, 0, 7, 0, 0],[0, 2, 0, 3, 0, 0, 0, 0, 4],[2, 9, 4, 0, 0, 0, 0, 0, 0],[0, 0, 0, 7, 3, 0, 5, 6, 0],[7, 0, 5, 0, 6, 0, 4, 0, 0],[0, 0, 7, 8, 0, 3, 9, 0, 0],[0, 0, 1, 0, 0, 0, 0, 0, 3],[3, 0, 0, 0, 0, 0, 0, 0, 2]]
    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [[2, 6, 7, 8, 3, 9, 5, 0, 4],[9, 0, 3, 5, 1, 0, 6, 0, 0],[0, 5, 1, 6, 0, 0, 8, 3, 9],[5, 1, 9, 0, 4, 6, 3, 2, 8],[8, 0, 2, 1, 0, 5, 7, 0, 6],[6, 7, 4, 3, 2, 0, 0, 0, 5],[0, 0, 0, 4, 5, 7, 2, 6, 3],[3, 2, 0, 0, 8, 0, 0, 5, 7],[7, 4, 5, 0, 0, 3, 9, 0, 1]]
    print(sudoku_grid_correct(sudoku2))
