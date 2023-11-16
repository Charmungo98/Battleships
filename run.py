import random

def init_board(size):
    """Initialize the game board."""
    return [["O"] * size for _ in range(size)]
