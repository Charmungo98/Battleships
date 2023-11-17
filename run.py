from random import randint, choice


def init_board(size):
    #Initialize the game board
    return [["O"] * size for _ in range(size)]


def place_ships(board, ships):
    #Place ships randomly on the board
    for _ in range(ships):
        ship_placed = False
        while not ship_placed:
            orientation = choice(['horizontal', 'vertical'])
            x, y = randint(0, len(board) - 1), randint(0, len(board) - 1)

            if orientation == 'horizontal' and y < len(board)-2:
                if board[x][y] == "O" and board[x][y + 1] == "O":
                    board[x][y] = "S"
                    board[x][y + 1] = "S"
                    ship_placed = True
            
            elif orientation == 'vertical' and x < len(board) - 2:
                if board[x][y] == "O" and board[x + 1][y] == "O":
                    board[x][y] = "S"
                    board[x + 1][y] = "S"
                    ship_placed = True


def print_board(board, reveal=False):
    #Print the game board
    for row in board:
        if reveal: 
            print(" ".join(row))
        else: 
            print(" ".join(["X" if cell == "X" else cell for cell in row]))


def get_move(player_moves, board_size):
    #Get the player's move
    while True:
        try:
            x, y = map(int, input("Enter coordinates (x y): ").split())
            x, y = x - 1, y - 1
            if not (0 <= x < board_size and 0 <= y < board_size):
                print(f"Invalid coordiantes. Please choose coordinates between 1 and {board_size}.")
            elif (x, y) in player_moves:
                print("You have already chosen these coordinates. Please try again.")
            else:
                return x, y
        except ValueError:
            print("Invalid input. Please enter two integers.")
        


def make_move(board, tracking_board, x, y):
    #Make a move on the board
    if board[x][y] == "S":
        print("Hit!")
        board[x][y] = "X"
        if tracking_board is not None:
            tracking_board[x][y] = "X"
        return True
    else:
        print("Miss!")
        board[x][y] = "-"
        if tracking_board is not None:
            tracking_board[x][y] = "-"
        return False


def has_won(board):
    #Check if all ships have been hit
    return all(cell != "S" for row in board for cell in row)


def computer_move(board):
    #Computer makes a random move
    x, y = randint(0, len(board) - 1), randint(0, len(board) - 1)
    while board[x][y] in ["X", "-"]:
        x, y = randint(0, len(board) - 1), randint(0, len(board) - 1)
    return x, y


def play_battleship(size=6, ships=4):
    #Play the Battleship game
    player_board = init_board(size)
    computer_board = init_board(size)
    player_tracking_board = init_board(size)
    place_ships(player_board, ships)
    place_ships(computer_board, ships)
    player_moves = set()

    print("\n" + "-" * 20 + "\n")
    print("Welcome to Battleship!")
    print("Board size: 6. Ships: 4.")
    print("Ships are 2 co-ordinates long.")
    print("Co-ordinates start at 1 on both x and y axis")
    print("Hit all of your opponents boats to win the game.")
    print("\n" + "-" * 20 + "\n")
    print("Your board:")
    print_board(player_board, reveal=True)
    print("\n" + "-" * 20 + "\n")

    while True:
        print("\nYour turn!")
        x, y = get_move(player_moves, size)
        player_moves.add((x, y))

        if make_move(computer_board, player_tracking_board, x, y):
            if has_won(computer_board):
                print("Congratulations. You win!")
                break
        
        print("\n" + "-" * 20 + "\n")
        print("\nComputer's turn.")
        cx, cy = computer_move(player_board)
        print(f"Computer chose: {cx} {cy}")
        make_move(player_board, None, cx, cy)
        if has_won(player_board):
            print("Computer won!")
            break
        
        print("\n" + "-" * 20 + "\n")
        print("\nYour board:")
        print_board(player_board)
        print("\nOpponents board:")
        print_board(player_tracking_board)
        print("\n" + "-" * 20 + "\n")


play_battleship()