# Please write a function named block_correct(sudoku: list, row_no: int, column_no: int), which takes a two-dimensional array representing a sudoku grid, and two integers referring to the row and column indexes of a single square, as its arguments. 
# Rows and columns are indexed from 0.

# The function should return True or False depending on whether the 3 by 3 block to the right and down from the given indexes is filled in correctly. 
# That is, whether the block contains each of the numbers 1 to 9 at most once.

# Notice that this function does not strictly follow the rules of sudoku. 
# In a real game of sudoku there are only 9 blocks to check, and these are located at indexes (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3) and (6, 6). 
# Such restrictions on indexes should not be implemented here.

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


if __name__ == "__main__":
    sudoku = [[9, 0, 0, 0, 8, 0, 3, 0, 0],  [2, 0, 0, 2, 5, 0, 7, 0, 0], [0, 2, 0, 3, 0, 0, 0, 0, 4], [2, 9, 4, 0, 0, 0, 0, 0, 0], [0, 0, 0, 7, 3, 0, 5, 6, 0], [7, 0, 5, 0, 6, 0, 4, 0, 0], [0, 0, 7, 8, 0, 3, 9, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 3], [3, 0, 0, 0, 0, 0, 0, 0, 2]]

    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))