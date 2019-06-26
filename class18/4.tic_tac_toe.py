"""
The beginnings of a game of Tic Tac Toe using a two-dimensional list for the game board.

@author Foo Barstein
@date 26 June 2019
"""

# a blank game board as a two-dimensional list
board = [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]
        ]


def print_board(board):
    """
    Print out the game board nicely
    
    @param board The game board, as a two-dimensional list
    """
    
    print("\nHere is the current status of the board: ")
    
    # loop through each row
    for row in board:
        
        # for each row, loop through the columns
        for col in row:
            # print the column with no line break
            print(format(col, '^3s'), end=' ')
        
        # put a line break at the end of the row
        print()

def position_is_blank(board, row, col):
    """
    Determine whether a given position on the game board has already been played or not
    
    @param board The game board, as a two-dimensional list
    @row The list index of the row to check
    @col The list index of the column to check
    """
    
    # check whether the board at this row and column is empty
    if board[row][col] == "-":
        # return True if so
        return True
    else:
        # return False otherwise
        return False


# start off with X's turn
player = "X"

# loop unti lthis becomes false
keep_going = True


# print out the starting state of the board
print_board(board)

# loop as long as the game is not over
while keep_going:
    
    # assume the user has not entered a valid response this turn...
    response_is_valid = False
    
    # keep looping until we get a good response from the user
    while not response_is_valid:
        # tell them it's their turn
        print( "\nIt's {}'s turn!".format(player) )
        
        # ask them for a move
        response = input("Where would you like to move (e.g. '2,2')? ")
        
        # get the index numbers as ints from the move
        # split the user's response into a list
        move = response.split(",")
        row = int(move[0]) - 1
        col = int(move[1]) - 1
        
        # validate the move
        if position_is_blank(board, row, col):
            # if the move is valid, do it!
            board[row][col] = player
            response_is_valid = True
        else:
            # otherwise, inform the user of the invalid move
            print("\nSorry, that position is taken... try again...")
    
    # print out the board
    print_board(board)
    
    # determine whether the player has won...
    # TBD... you can 
    
    # flip players
    if player == "X":
        player = "O"
    else:
        player = "X"



    