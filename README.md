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

#### User entry
  - Accepts user input for both coordinates.
  - Before the game begins players are prompted to enter their name, the game cannot start till a name or username is provided.
  - Once a name is provided, the game will address the user as the name provided.

![name-input](https://github.com/Charmungo98/Battleships/assets/138699715/1bddc89a-69cb-45df-9b7d-e219aa6e904e)

#### Random generation 
  - Ships locations are randomly generated for both the player and the cpu.
  - Player cannot see where ships of cpu are located until they are hit.
  - CPU coordinares are random. 

#### Interactive coordinate input with validation to prevent out-of-bound guesses.
  - You cannot enter coordinates that are outside of the scope of the board.
  - Only intergers can be entered as coordinate answers
  - The same coordinates cannot be entered twice, the game will provide them with another attempt to provide new coordinates.

![wrong-input](https://github.com/Charmungo98/Battleships/assets/138699715/2cd3b56e-911e-4c6f-897a-1e70147a6b59)

#### Score tracking
  - Score of both user and cpu is tracked and displayed after each round.
  - Upon succession of hitting all opponents ships, a winner is declared.

![score](https://github.com/Charmungo98/Battleships/assets/138699715/974878c6-dad3-49f4-8abc-b29b33aefec7)
![winner](https://github.com/Charmungo98/Battleships/assets/138699715/3cf3824c-63a6-46f9-b2b3-5f8161d7c458)

#### Simple and user-friendly console-based interface. 

### Future Features
  - The user will be able to select the size of the board they wish to use.
  - The user will be able to select the number of ships used on each board and the length of the ships.
  - The user will be able to choose the location of their own ships.
  - The CPU will be able to recognise pattern and use strategic thought to calculate its coordinates. 


# 3. Data Model 

### Overview
  - The Battleship game is designed with an object-oriented approach, focusing on classes and methods to manage game state and logic.
  - The main components are the game board, ships, and player interactions, encapsulated within classes and manipulated via class methods.

### Classes and Their Responsibilities
#### GameBoard Class: Represents the game board.
  - Each instance of this class represents a 6x6 grid.
  - Methods include initializing the board, placing ships, and displaying the board.

#### Ship Class: Represents the ships on the board.
  - Responsible for ship attributes such as size, orientation, and coordinates.
  - Methods include placing the ship on the board and checking if a ship is hit.
  - 
#### Player Class: Represents each player in the game.
  - Stores information like player's name, their board, and their moves.
  - Methods include making a move, tracking hits and misses, and checking for win conditions.
  - 
### Game Board Representation
  - Implemented using a 2D array (lists of lists in Python), where each element corresponds to a cell on the game board.
  - Cell states include "O" (empty water), "S" (part of a ship), "X" (a hit on a ship), and "-" (a missed shot).

### Ship Placement
  - Handled by the Ship class, which randomly places ships on the board with consideration for orientation and avoiding overlaps.
  - The placement method ensures that ships stay within the board's boundaries and do not intersect.

### Player Moves and Score Tracking
  - Managed by the Player class.
  - Player moves are stored in a set to efficiently track all previous attempts and prevent duplicates.
  - Scores are updated in real-time after each turn, based on the outcome of the moves.

### Class Methods for Gameplay
  - make_move(): Belongs to the Player class; used to make a move on the opponent's board.
  - update_score(): Updates the player's score based on successful hits.
  - has_won(): Evaluates the game board to check if a player has met the win condition.

### Win Condition
  - Determined by checking if all parts of the opponent's ships are hit.
  - The method has_won() in the Player class is used for this evaluation.

### User Interface
  - Interactions are handled through the console with printed messages and input prompts.
  - The GameBoard class provides a method to display the board state in a user-friendly format.
