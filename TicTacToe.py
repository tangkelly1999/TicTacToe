'''
Date: March 7 2018
Author: Kelly Tang
Description: Tic-Tac-Toe game played against the computer. Make your moves
through the shell. Good luck :)

'''
def winner(board):
    """This function accepts the Tic-Tac-Toe board as a parameter.  
    If there is no winner, the function will return the empty string "".  
    If the user has won, it will return "X", and if the computer has 
    won it will return "O"."""
     
    # Check rows for winner
    for row in range(3):
        if (board[row][0] == board[row][1] == board[row][2]) and\
           (board[row][0] != " "):
            return board[row][0]
 
    # Check columns for winner
    for column in range(3):
        if (board[0][column] == board[1][column] == board[2][column]) and\
           (board[0][column]!=" "):
            return board[0][column]
    # Check diagonal (top-left to bottom-right) for winner
    for block in range(3):
        if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0]!=" "):
            return board[0][0]
        
    # Check diagonal (bottom-left to top-right) for winner
    for block in range(3):
        if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] != " "):
            return board[0][2]
 
     
    # No winner: return the empty string
    return ""
 
def display_board(board):
    """This function accepts the Tic-Tac-Toe board as a parameter.  
    It will print the Tic-Tac-Toe board grid (using ASCII characters)
    and show the positions of any X's and O's.  It also displays 
    the column and row numbers on top and beside the board to help
    the user figure out the coordinates of their next move.  
    This function does not return anything."""
     
    print "   1   2   3"
    print "1: "+board[0][0]+" | "+board[0][1]+" | "+board[0][2]
    print "  ---+---+---"
    print "2: "+board[1][0]+" | "+board[1][1]+" | "+board[1][2]
    print "  ---+---+---"
    print "3: "+board[2][0]+" | "+board[2][1]+" | "+board[2][2]
    print
     
def make_user_move(board):
    """This function accepts the Tic-Tac-Toe board as a parameter.  
    It will ask the user for a row and column.  If the row and 
    column are each within the range of 0 and 2, and that square
    is not already occupied, then it will place an "X" in that square."""
    
    
    valid_move = False
    
    while not valid_move:
        try:
            row = input("What row would you like to move to (0-2):")
            col = input("What col would you like to move to (0-2):")
            row = row-1
            col = col-1
            if (0<=row<=2) and (0<=col<=2) and (board[row][col]==" "):
                board[row][col] = 'X'
                valid_move = True
            else:
                print "Sorry, invalid square. Please try again!\n"
        except NameError:
            print "number only"
    
    
             
def make_computer_move(board):
    """This function accepts the Tic-Tac-Toe board as a parameter.  
    It will randomly pick row and column values between 0 and 2.  
    If that square is not already occupied it will place an "O" 
    in that square.  Otherwise, another random row and column 
    will be generated."""
    
    import random
    row= random.randrange(0,3)
    col= random.randrange(0,3)

    while board[row][col] != " ":
        row= random.randrange(0,3)
        col= random.randrange(0,3)  
        
    board[row][col] = "O"
    print board[row][row]
        
     
def main():
    """Our Main Game Loop:"""
     
    free_cells = 9
    users_turn = True
    ttt_board = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
 
    while not winner(ttt_board) and (free_cells > 0):
        display_board(ttt_board)
        if users_turn:
            make_user_move(ttt_board)
            users_turn = not users_turn
        else:
            make_computer_move(ttt_board)
            users_turn = not users_turn
        free_cells -= 1
         
    display_board(ttt_board)
    if (winner(ttt_board) == 'X'):
        print "Y O U   W O N !"
    elif (winner(ttt_board) == 'O'):
        print "I   W O N !"
    else:
        print "S T A L E M A T E !"    
    print "\n*** GAME OVER ***\n"
  
# Start the game!
main()
