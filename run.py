import random

board = [" "]*10

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

print(player_choice(board))
print(computer_choice(board))