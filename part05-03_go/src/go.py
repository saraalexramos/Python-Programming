# In a game of Go two players take turns to place black and white stones on a game board. 
# The winner is the player who manages to encircle a bigger area on the board with their own game pieces.
# 
# Please write a function named who_won(game_board: list), which takes a two-dimensional array as its argument.
# The array consists of integer values, which represent the following situations:

#    0: empty square
#    1: player 1 game piece
#    2: player 2 game piece

# The scoring rules of Go can be quite complex, but in this exercise it is enough to compare the number of pieces each player has on the game board. 
# Also, the size of the game board is not limited.

# The function should return the value 1 if player 1 won, and the value 2 if player 2 won. 
# If both players have the same number of pieces on the board, the function should return the value 0.


def who_won(game_board:list):
    count1 = 0 # a variable to store how many pieces the player 1 has on board
    count2 = 0 # a variable to store how many pieces the player 2 has on board

    for row in game_board: # for each row in game_board
        for element in row: # and for each element in each row
            if element == 1:
                count1 += 1
            elif element == 2:
                count2 += 1
    
    if count1 == count2:
        return 0
    elif count1 > count2:
        return 1
    elif count2 > count1:
        return 2
