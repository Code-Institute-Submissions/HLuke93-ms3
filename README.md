# Tic Tac Toe -v- Computer (by Luke Hickson)

Tic-tac-toe (American English), noughts and crosses (Commonwealth English), or Xs and Os (Irish English) is a paper-and-pencil game for two players who take turns marking the spaces in a three-by-three grid with X or O. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner. It is a solved game, with a forced draw assuming best play from both players.  [Live Website Here]().
<br>

![Tic Tac Toe Board](Images/boardimage.png)
<br>

## Table of Contents

1. [Rules of the Game ](#Rules)
2. [User Goals](#User-goals)
3. [User Expectations](#User-expectations)
4. [Features](#features)
   1. [Future Features](#Future-Features)
5. [How the game is Played](#How-the-game-is-Played)
6. [Testing](#Testing)
   1. [Manual Testing](#Manual-Testing) 
   2. [Validator Testing](#Validator-Testing) 
   3. [Solved Bugs](#Solved-Bugs)
7. [Deployment](#Deployment)
8. [Credits](#Credits)
    1. [Technologies Used](#Technologies-Used) 
    2. [Content](#Content) 
    3. [Media](#Media)


<br>

# Rules of the Game (Historically)
<br>

Tic-tac-toe is played on a three-by-three grid by two players, who alternately place the marks X and O in one of the nine spaces in the grid.
There is no universally-agreed rule as to who plays first.
The Aim of the game is the get three of your marks in a horizontal, vertical, or diagonal row.
Players soon discover that the best play from both parties leads to a draw. Hence, tic-tac-toe is often played by young children who may not have discovered the optimal strategy.
<br>

![Tic Tac Toe Board](Images/main.png)
<br>

[Go to the top](#Table-of-Contents)

<br>


# User Goals
<br>

## Game Flow

<br>

![Game Flow](Images/flow.png)

<br>


## I want to create a game that is easy to navigate for users.

Was this achieved?\
Yes\
How was this achieved?\
This was achieved by taking a very simple apporach to the classic Tic Tac Toe.\
The game will run in a smooth loop to allow the user to keep playing as many times as they want to or can end the game.


## I want the user to play against a computer rather than a 2 player game.

Was this achieved?\
Yes\
How was this achieved?\
This was achieved by creating a computer choice function which randomly generates a choice on the board for the computer.  


## I want to make it clear by using a color scheme (Win=Green , Lose=Red) the outcome of the game

Was this achieved?\
Yes\
How was this achieved?\
This was achieved by adding color to the various outcomes of the game. 

## Colors

Winner Message, Green ("\033[1;34m").\
Lose Message, Red ("\033[1;31;31m").\
Draw Message, White ("\033[1;37;40m").\

Main Game Color,Pink ("\033[1;35;35m").\
Reference board color, Blue ("\033[1;34;34m").

<br> 

[Go to the top](#Table-of-Contents)

<br>

# Features

<br>

## Welcome page

This is the first page you see when the app loads. On this page there is a Tic Tac Toe image located at the top of the screen, a welcoem message and a question to the user. The question asks the user "Please Enter Your Name: ".

![Welcome Page](Images/welcome.png)

<br>

## Choose Marker

The player is welcomed by name and asked to choose a marker to play with. "X" or "O".

![Choose Marker Page](Images/markerchoice.png)

<br>

## Ready to Play?

After the user chooses a marker , either the user of computer will play first.
The user is asked one more time if they are ready to play?

![Ready to Play](Images/readytoplay.png)

<br>

## Main Game Screen

The user is presented with the main game screen. A reference board in blue and a game board in pink.
The user is asked to pick a position to drop their marker.
If the computer was chose to go first , it's move will already be on the board.

![Main Board](Images/gamestart.png)

<br>

## User Win Screen

In the event of the user winning, the user is presented with a winner message in green , and asked if they want to play again

![User Win](Images/userwin.png)

<br>

## Computer Win Screen

In the event of the computer winning, the user is presented with a loosing message in red , and asked if they want to play again

![Computer Win](Images/computerwin.png)


<br>

## Draw Screen

In the event of a draw, the user is presented with a draw message in white , and asked if they want to play again

![Draw Screen](Images/draw.png)

<br>

## Thanks for Playing Screen

The user has selectted that they do not want to play again and is displayed the message below.

![Thanks for Playing](Images/thanksforplaying.png)

<br>


[Go to the top](#Table-of-Contents)


<br>



# Future Features

## Minimax Algorithim

In the future i woudl like to implennt the Minimax algorithm for the computer choice.
This would add a much higher level of difficulty to the game.
Currently it is only a randomly generated computer choice.

## 


# Testing

<br>

## Python

Python was tested using PEP8 PEP8 validator

The Python results came back with the following:


![PEP8](Images/pep81.PNG)

![PEP8](Images/pep82.PNG)




[Go to the top](#Table-of-Contents)


<br>

## Manual Testing

<br>



## Game Testing
<br>


<br>


<br>

## Validator Testing
<br>


<br>
## Solved Bugs
<br>


<br>

# Deployment

<br>

[Go to the top](#Table-of-Contents)


<br>

## GitHub Pages
<br>


<br>

# Credits

<br>

[Go to the top](#Table-of-Contents)


<br>

## Technologies Used
<br>


<br>

## Content 
<br>



<br>

## Media

<br>




