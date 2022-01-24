import random

board = [" "]*10 # Remove this (Only for testing)

def display_board(board):
    """
    Function to print out the board
    """
    print("--------")
    print(board[7] + " |" + board[8] + " |" + board[9])
    print("--------")
    print(board[4] + " |" + board[5] + " |" + board[6])
    print("--------")
    print(board[1] + " |" + board[2] + " |" + board[3])
    print("--------")



def player_marker():
    """
    Function that can take a player input and assisgn their marker as 
    "X" or "O"
    """
    marker = ""

    while not (marker == "X" or marker == "O"):
        marker = input("Player 1: Do you want to be X or O? ").upper()

    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")


def place_player_marker(board, marker, position):
    """
    function that takes in the board list , a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.
    """

    board[position] = marker

def player_choice(board):

    position = 0

    while position not in [1,2,3,4,5,6,7,8,9]:
        position = int(input("Choose you position: (1-9): "))
    return position

def computer_choice(board):

    position = 0
    while position not in [1,2,3,4,5,6,7,8,9]:
        position = random.randint(1,9)
    return position

def check_if_space(board, position):
    """
    a function that returns True or False if a space on the board is freely available.
    """
    if board[postion] == " ":
        return True

def full_board(board):
    """
    function that checks if the board is full 
    and returns a boolean value.
    """
    for space in range(1,10):
        if check_if_space(board, space):
            return False
        return True

def check_for_win(board, marker):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
