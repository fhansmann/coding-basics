# Game of X/O

# data structure: list, tupel, dictionary
# tuple are not changabe / immutable
# dictionary uses key words
# thus list is best suited, they allow to access elements via number

board = ["  " for i in range(9)]

def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print()  #Use print when you want to show a value to a human. return is a keyword. When a return statement is reached, Python will stop the execution of the current function
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(icon):
    
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2
        
    print("Your turn player {}".format(number))
    
    choice = int(input("Enter your move (1-9): ").strip())
    if board[choice -1] == "  ":
        board[choice -1 ] = icon
    else:
        print()
        print("That space is taken!")
    
def is_draw():
    if "  " not in board:
        return True
    else:
        return False

while True:
    print_board()
    player_move("X")
    print_board()
    player_move("O")
   
#no winning function
