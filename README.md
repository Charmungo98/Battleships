# Battleship!

- This Python-based implementation of the classic Battleship game allows a single player to play against the computer, it is played within the Python terminal. 

- The game is played on a square grid where each player has a fleet of ships. The objective is to sink all of your opponent's ships before they sink all of yours.

Visit the deployed website [here](https://battleship-python98-c71c6949cf34.herokuapp.com/).

# 1. How to play

### Game Setup

- Battleship is based on the classic board/paper and pen game, further information on the game can be found on its [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game) "Link to CSS Wikipedia page")

- At the start of the game, players enter their name for a personalized experience.

- The game board is a 6x6 grid.

- Each player, the user and the computer, secretly places 4 ships on their board. Each ship occupies 2 consecutive cells on the grid.

- The ships can be placed either horizontally or vertically, and their placement is random and hidden from the opponent.

- Ships are placed on the board and indicated by an S. Guesses are marked on the board using -, hits are indicated by an X.

### Gameplay

- The user enters their name before the game begins.

- Players take turns to "fire" at the opponent's grid by guessing the coordinates.

- The game asks for row and column numbers separately. Both coordinates start from 1, with 1,1 being the top left corner of the grid. After each guess, the game informs the player whether it was a hit or a miss.

- If a ship is hit at all its coordinates, it is considered sunk.

- The game board does not reveal ship locations, but it does show the results of each player's shots. The player's and computer's scores (number of successful hits) are displayed after each round.

### Winning the Game

- The game continues until all ships of one player are sunk.

- If all of the computer's ships are sunk first, the player wins. Conversely, if all of the player's ships are sunk first, the computer wins.

- The game announces the winner.

# 2. Features

### Existing Feature

#### Interactive coordinate input with validation to prevent out-of-bound guesses.
  - You cannot enter coordinates that are outside of the scope of the board.
  - Only intergers can be entered as coordinate answers
  - The sae coordinates cannot be entered twice, if a player enters the same coordinates twice, the game will provide them with another attempt to provide new coordinates. 
![wrong-input](https://github.com/Charmungo98/Battleships/assets/138699715/2cd3b56e-911e-4c6f-897a-1e70147a6b59)
