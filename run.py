from random import randint


def init_board(size):
    #Initialize the game board
    return [["O"] * size for _ in range(size)]


def place_ships(board, ships):
    #Place ships randomly on the board
    for _ in range(ships):
        ship_placed = False
        while not ship_placed:
            x, y = randint(0, len(board) - 1), randint(0, len(board) - 1)
            if board[x][y] == "O":
                board[x][y] = "S"
                ship_placed = True


def print_board(board, reveal=False):
    #Print the game board
    for row in board:
        print(" ".join(row if reveal else ["X" if cell == "S" else cell for cell in row]))


def get_move():
    #Get the player's move
    try:
        x, y = map(int, input("Enter coordinates (x y): ").split())
        return x, y
    except ValueError:
        print("Invalid input. Please enter two integers.")
        return get_move()


def make_move(board, x, y):
    #Make a move on the board
    if board[x][y] == "S":
        print("Hit!")
        board[x][y] = "H"
        return True
    else:
        print("Miss!")
        board[x][y] = "M"
        return False


def has_won(board):
    #Check if all ships have been hit
    return all(cell != "S" for row in board for cell in row)


def computer_move(board):
    #Computer makes a random move
    x, y = randint(0, len(board) - 1), randint(0, len(board) - 1)
    while board[x][y] in ["H", "M"]:
        x, y = randint(0, len(board) - 1), randint(0, len(board) - 1)
    return x, y


def play_battleship(size=10, ships=5):
    #Play the Battleship game
    player_board = init_board(size)
    computer_board = init_board(size)
    place_ships(player_board, ships)
    place_ships(computer_board, ships)

    print("Welcome to Battleship!")
    print("Your board:")
    print_board(player_board, reveal=True)

    while True:
        print("\nYour turn!")
        x, y = get_move()
        if make_move(computer_board, x, y):
            if has_won(computer_board):
                print("You won!")
                break
        
        print("\nComputer's turn.")
        cx, cy = computer_move(player_board)
        print(f"Computer chose: {cx} {cy}")
        make_move(player_board, cx, cy)
        if has_won(player_board):
            print("Computer won!")
            break
        
        print("\nYour board:")
        print_board(player_board)