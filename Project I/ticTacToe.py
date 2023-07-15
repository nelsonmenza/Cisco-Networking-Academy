from random import randrange


def display_board(board):

    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")


board = [[3 * j + i + 1 for i in range(3)]
         for j in range(3)]  # make an empty board


def enter_move(board):
    while True:
        move = int(input("Enter a number: "))
        if move > 0 or move < 10:
            break
    move -= 1
    row = move//3
    col = move % 3
    board[row][col] = "O"
    return board[row][col]


def free_board(board):
    free = []
    board_free = ()
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ["O", "X"]:
                free.append((row, col))
    return free


# def win_check(board):
def enter_move_pc(board):
    for i in range(10):
        move = randrange(8)
    move -= 1
    row = move//3
    col = move % 3
    board[row][col] = "X"
    return board[row][col]


board[1][1] = "X"
