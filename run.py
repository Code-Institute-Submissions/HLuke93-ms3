import random

import os


def clear():
    """
    Clear the console/screen
    https://stackoverflow.com/questions/2084508/clear-terminal-in-python
    """
    os.system("cls" if os.name == "nt" else "clear")


def display_board(board):
    """
    Function to print out the board
    """
    clear()
    print("\033[1;34;40mREFERENCE BOARD")

    print("---------")
    print("7" + " |" + " 8" + " |" + " 9")
    print("---------")
    print("4" + " |" + " 5" + " |" + " 6")
    print("---------")
    print("1" + " |" + " 2" + " |" + " 3")
    print("---------")
    print("\033[0;37;40m")
    print("\033[1;37;40mGAME BOARD")
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
        print("")

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

    """
    a function that asks for a player's next position (as a number 1-9) and then uses the check space function to check if its a free position. If it is, then return the position for later use.
    """

    position = 0

    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] or not check_if_space(board, int(position)):
        position = input("Choose you position: (1-9): ")

    return int(position)


def computer_choice(board):

    """
    a function that generates a random number for the computer between 1-9 and then  uses the check space function to check if its a free position. If it is, then return the position for later use.
    """

    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not check_if_space(
        board, position
    ):
        position = random.randint(1, 9)
    return position


def check_if_space(board, position):
    """
    a function that returns True or False if a space on the board is freely available.
    """
    return board[position] == " "


def full_board(board):
    """
    function that checks if the board is full
    and returns a boolean value.
    """
    for i in range(1, 10):
        if check_if_space(board, i):
            return False
    return True


def check_for_win(board, mark):

    """
    a function that takes in a board and checks to see if someone has won.
    """

    return (
        (board[7] == mark and board[8] == mark and board[9] == mark)
        or (  # across the top
            board[4] == mark and board[5] == mark and board[6] == mark
        )
        or (  # across the middle
            board[1] == mark and board[2] == mark and board[3] == mark
        )
        or (  # across the bottom
            board[7] == mark and board[4] == mark and board[1] == mark
        )
        or (  # down the middle
            board[8] == mark and board[5] == mark and board[2] == mark
        )
        or (  # down the middle
            board[9] == mark and board[6] == mark and board[3] == mark
        )
        or (  # down the right side
            board[7] == mark and board[5] == mark and board[3] == mark
        )
        or (board[9] == mark and board[5] == mark and board[1] == mark)  # diagonal
    )  # diagonal


def choose_first():

    """
    a function that uses the random module to randomly decide which player goes first.
    """

    if random.randint(0, 1) == 0:
        return "Computer"
    else:
        return "Player 1"


def play_again():

    """
    Function to Play again or not.
    """
    return input("Do you want to play again? Yes or No: ").lower().startswith("y")
    


while True:

    board = [" "] * 10
    clear()
    name = input("Please Enter you Name: ")
    clear()
    print(f"Welcome To Tic Tac Toe {name}.....")
    print("")
    user_marker, computer_marker = player_marker()  # Assign X and O to user and Computer
    turn = choose_first()
    print(f"{turn} will go first")
    print("")

    play_game = input(f"Are you ready to play {name}? Yes or No. ").lower()

    if play_game == "no":
        break

    if play_game.lower() == "yes":
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == "Player 1":

            display_board(board)
            position = player_choice(board)
            place_player_marker(board, user_marker, position)

            if check_for_win(board, user_marker):
                display_board(board)
                print(f"{name} Won")
                game_on = False
            else:
                if full_board(board):
                    display_board(board)
                    print("It's a Draw")
                    break
                else:
                    turn = "Computer"

        else:

            display_board(board)
            position = computer_choice(board)
            place_player_marker(board, computer_marker, position)

            if check_for_win(board, computer_marker):
                display_board(board)
                print("Computer Won")
                game_on = False
            else:
                if full_board(board):
                    display_board(board)
                    print("It's a Draw")
                    break
                else:
                    turn = "Player 1"

    if not play_again():
        break

