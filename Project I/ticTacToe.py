from random import randrange

# Function to display the tic-tac-toe board


def display_board(board):
    # Print the board in a formatted manner
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")


# Initialize the empty tic-tac-toe board
board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]

# Function to allow the user to make a move


def enter_move(board):
    avilable = free_board(board)
    while True:
        # Prompt the user to enter a number
        move = int(input("Enter a number: "))
        if 0 < move < 10:  # Check if the move is between 1 and 9
            break
    move -= 1  # Convert the move to a valid index (0-8)
    row = move // 3  # Calculate the row index of the move
    col = move % 3  # Calculate the column index of the move
    list_rc = (row, col)
    if list_rc in avilable:
        # If the chosen position is available, place "O" in that position
        board[row][col] = "O"
        return board[row][col]
    else:
        if list_rc not in avilable:
            # If the chosen position is not available, prompt the user to repeat the input
            print("Field already occupied - repeat your input!")
            return enter_move(board)

# Function to get the list of free positions on the board


def free_board(board):
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ["O", "X"]:
                free.append((row, col))
    return free

# Function to check if a player has won


def win_check(board):
    players = ["X", "O"]
    for rc in range(3):
        for player in players:
            if board[rc][0] == player and board[rc][1] == player and board[rc][2] == player:  # check row rc
                return True
            elif board[0][rc] == player and board[1][rc] == player and board[2][rc] == player:
                return True
            elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
                return True
            elif board[2][0] == player and board[1][1] == player and board[0][2] == player:
                return True

    return False

# Function for the computer's move


def pc_move(board):
    avilable = free_board(board)
    for i in range(10):
        if i != 0:
            move = randrange(10)
    move -= 1
    row = move // 3
    col = move % 3
    list_rc = (row, col)
    if list_rc in avilable:
        # If the chosen position is available, place "X" in that position
        board[row][col] = "X"
        return board[row][col]
    else:
        if list_rc not in avilable:
            # If the chosen position is not available, try a different random move
            return pc_move(board)


# Set the center position to "X" to give the computer an advantage
board[1][1] = "X"

# Display the initial board
display_board(board)

# Game loop
free_space = free_board(board)
while len(free_space):
    if free_board(board) == []:
        # If the board is full and no one has won, it's a tie
        print("Tie")
        break
    if len(free_board(board)) % 2 == 0:
        # It's the user's turn
        enter_move(board)
        display_board(board)
        if win_check(board) == True:
            # Check if the user has won
            print("You Win!")
            break
    elif len(free_board(board)) % 2 != 0:
        # It's the computer's turn
        pc_move(board)
        display_board(board)
        if win_check(board) == True:
            # Check if the computer has won
            print("You lose!")
            break
