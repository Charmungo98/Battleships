from random import randint

def init_board(size):
    #Initialize the game board.#
    return [["O"] * size for _ in range(size)]

def place_ships(board, ships):
    #Place ships randomly on the board.#
    for _ in range(ships):
        ship_placed = False
        while not ship_placed:
            x, y = randint(0, len(board) - 1), randint(0, len(board) - 1)
            if board[x][y] == "O":
                board[x][y] = "S"
                ship_placed = True
                
def print_board(board, reveal=False):
    #Print the game board.#
    for row in board:
        print(" ".join(row if reveal else ["X" if cell == "S" else cell for cell in row]))

def get_move():
    #Get the player's move.#
    try:
        x, y = map(int, input("Enter coordinates (x y): ").split())
        return x, y
    except ValueError:
        print("Invalid input. Please enter two integers.")
        return get_move()