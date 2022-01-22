"""A game of minesweeper. The player must identify randomly placed mines.
A game is won if the player can identify all mines. A game is lost if the
player steps on a mine."""

import random

# Game characters to fill in on board.
EMPTY_SPACE = " "
MINE = "m"

# Game constants
BOARD_WIDTH = 20
BOARD_HEIGHT = 20
NUMBER_OF_MINES = 30


def main():
	"""Start game."""


def get_board():
	"""Returns underlying board of a minesweeper game. Using a dictionary"""
	board = {}
	mines = get_mine_places()
	for x in range(1, BOARD_WIDTH + 1):
		for y in range(1, BOARD_HEIGHT + 1):
			if (x, y) in mines:
				board[(x, y)] = MINE
			else:
				nearby_mines = add_nearby_mines(x, y, mines)
				if nearby_mines != 0:
					board[(x, y)] = nearby_mines
				else:
					board[(x, y)] = EMPTY_SPACE
	return board


def get_mine_places():
	"""Returns a list of tuples which describe mines' positions."""
	positions = []
	count = 0
	while count < NUMBER_OF_MINES:
		random_x = random.randint(1, BOARD_WIDTH)
		random_y = random.randint(1, BOARD_HEIGHT)
		mine_position = (random_x, random_y)
		if mine_position not in positions:
			positions.append(mine_position)
			count += 1
	return sorted(positions)

def add_nearby_mines(x, y, mines):
	"""Returns number of nearby mines to give clue to player."""
	adjacent_squares = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), 
		(x - 1, y), (x + 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]
	num_of_adj_mines = 0
	for square in adjacent_squares:
		if square in mines:
			num_of_adj_mines += 1
	return num_of_adj_mines

def display_board(board):
	"""Displays board given a board dictionary."""
	board_str = " "
	for x in range(1, BOARD_WIDTH + 1):
		if x < 10:
			board_str += f"  {x}"
		else:
			board_str += f" {x}"
	board_str += "\n"
	for y in range(1, BOARD_HEIGHT + 1):
		if y < 10:
			board_str += f"{y} "
		else:
			board_str += f"{y}"
		for x in range(1, BOARD_WIDTH + 1):
			board_str += f"[{board[x, y]}]"
		board_str += "\n"
	return board_str


# If this program was run (instead of imported), run the game
if __name__ == "__main__":
	main()