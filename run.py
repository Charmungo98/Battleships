from random import randint, choice


def init_board(size):
    """Initialize the game board.
    Creates a square game board of the given size filled with '.' to
    represent water. The board is a 2D list (list of lists), where each
    sublist represents a row on the board.
    """
    return [["."] * size for _ in range(size)]


def place_ships(board, ships):
    """Place ships randomly on the board.

    Each ship occupies two consecutive spaces on the board. The function
    randomly selects the orientation (horizontal or vertical) and starting
    point for each ship, ensuring that ships fit within the board and do not
    overlap with each other.

    Args:
    board (list): The game board.
    ships (int): The number of ships to place on the board.
    """
    for _ in range(ships):
        ship_placed = False
        while not ship_placed:
            # Randomly choose orientation and starting point for the ship
            orientation = choice(['horizontal', 'vertical'])
            x, y = randint(0, len(board) - 1), randint(0, len(board) - 1)

            # Place the ship and ensure it doesn't go out of bounds
            if orientation == 'horizontal' and y < len(board)-2:
                if board[x][y] == "." and board[x][y + 1] == ".":
                    board[x][y] = "S"
                    board[x][y + 1] = "S"
                    ship_placed = True

            elif orientation == 'vertical' and x < len(board) - 2:
                # Ensure no overlap with existing ships
                if board[x][y] == "." and board[x + 1][y] == ".":
                    board[x][y] = "S"
                    board[x + 1][y] = "S"
                    ship_placed = True


def print_board(board, reveal=False):
    """Print the game board to the console.
    Prints each row of the board as a string. If 'reveal' is False, hides
    the ships by replacing 'S' with '.' to simulate the fog of war.
    """
    for row in board:
        # Show ship locations if reveal is True, otherwise hide them
        if reveal:
            print(" ".join(row))
        else:
            print(" ".join(["X" if cell == "X" else cell for cell in row]))


def get_move(player_moves, board_size):
    """Prompt the player to enter their move coordinates.

    Continuously prompts the player to enter valid row and column numbers
    until a valid, unchosen move is provided. Checks for valid range and
    duplicate moves.

    Args:
    player_moves (set): A set of tuples representing all previous moves.
    board_size (int): The size of the board (to validate the coordinates).

    Returns:
    tuple: A tuple (x, y) representing the player's chosen move.
    """
    while True:
        try:
            # Get row/column input from player, adjusting for 1-based indexing
            x = int(input("Enter row (1 to {}): ".format(board_size))) - 1
            y = int(input("Enter column(1 to {}): ".format(board_size))) - 1

            # Validate input: within range and not previously chosen
            if not (0 <= x < board_size and 0 <= y < board_size):
                print("Invalid coordiantes.")
                print("Please choose coordinates between 1 and 6.")
            elif (x, y) in player_moves:
                print("Coordinates previously chosen, please try again.")
            else:
                return x, y
        except ValueError:
            print("Invalid input. Please enter an integer.")


def make_move(board, tracking_board, x, y, player_moves):
    """Make a move on the board based on the player's input.

    Updates the board based on the move. Marks a hit if a ship is at the
    coordinates, a miss otherwise. Also updates the tracking board for the
    player to keep track of their moves.

    Args:
    board (list): The opponent's game board.
    tracking_board (list): The player's tracking board for hits/misses.
    x (int): The x-coordinate (row) of the move.
    y (int): The y-coordinate (column) of the move.
    player_moves (set): A set of tuples representing all previous moves.

    Returns:
    str: The result of the move ('hit', 'miss', or 'repeat').
    """

    if (x, y) in player_moves:
        print("You've already hit this spot!")
        return "repeat"
    elif board[x][y] == "S":
        print("Hit!")
        board[x][y] = "X"
        if tracking_board is not None:
            tracking_board[x][y] = "X"
        return "hit"
    else:
        print("Miss!")
        board[x][y] = "-"
        if tracking_board is not None:
            tracking_board[x][y] = "-"
        return "miss"


def has_won(board):
    """Check if all ships have been hit on a given board.
    Determines if the game is won by checking if there are any ship parts
    ('S') remaining on the board.
    """
    return all(cell != "S" for row in board for cell in row)


def computer_move(board):
    """Computer generates a random move.
    Continuously selects random coordinates for the move until an unhit
    spot is chosen. Avoids repeating moves.
    """
    x, y = randint(0, len(board) - 1), randint(0, len(board) - 1)
    while board[x][y] in ["X", "-"]:
        x, y = randint(0, len(board) - 1), randint(0, len(board) - 1)
    return x, y


def play_battleship(size=6, ships=4):
    """Main function to play the Battleship game.

    Initializes the game, places ships, and manages the game loop,
    including player input, computer moves, and checking win conditions.

    Args:
    size (int): The size of the game board.
    ships (int): The number of ships to be placed on each board.
    """
    player_name = input("Enter your name: ")
    player_board = init_board(size)
    computer_board = init_board(size)
    player_tracking_board = init_board(size)
    place_ships(player_board, ships)
    place_ships(computer_board, ships)

    player_moves = set()
    player_score, computer_score = 0, 0

    # Print game instructions and board
    print("\n" + "-" * 20 + "\n")
    print("Welcome to Battleship, {}!".format(player_name))
    print("Board size: 6. Ships: 4.")
    print("Ships are 2 co-ordinates long.")
    print("Co-ordinates start at 1 on both axis at top left corner.")
    print("Hit all of your opponents boats to win the game.")
    print("\n" + "-" * 20 + "\n")
    print("Your board:")
    print_board(player_board, reveal=True)
    print("\n" + "-" * 20 + "\n")

    while True:
        # Handle player's turn
        print("\nYour turn, {}!".format(player_name))
        x, y = get_move(player_moves, size)
        move_result = make_move(computer_board,
                                player_tracking_board, x, y, player_moves)
        if move_result == "hit":
            player_score += 1
        player_moves.add((x, y))

        # Check if player has won
        if has_won(computer_board):
            print("\nYour final hit:")
            print_board(player_tracking_board)
            print("Congratulations, {}! You win!".format(player_name))
            break

        # Handle computer's turn
        print("\n" + "-" * 20 + "\n")
        print("\nComputer's turn.")
        cx, cy = computer_move(player_board)
        print(f"Computer chose: {cx + 1} {cy + 1}")
        computer_move_result = make_move(player_board, None, cx, cy, set())
        if computer_move_result == "hit":
            computer_score += 1

        # Check if computer has won
        if has_won(player_board):
            print("\nComputer's final hit:")
            print_board(player_board)
            print("Sorry, {}! Computer won!".format(player_name))
            break

        # Display current scores
        print("\nScores: {} - {},Computer - {}"
              .format(player_name, player_score, computer_score))
        print("\n" + "-" * 20 + "\n")
        print("\nYour board:")
        print_board(player_board)
        print("\nOpponents board:")
        print_board(player_tracking_board)
        print("\n" + "-" * 20 + "\n")


play_battleship()
