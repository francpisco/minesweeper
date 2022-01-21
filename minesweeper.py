"""A game of minesweeper. The player must identify randomly placed mines.
A game is won if the player can identify all mines. A game is lost if the
player steps on a mine."""

import random

# Game characters to fill in on board.
EMPTY_SPACE = " "
MINE = "m"

# Game constants
BOARD_WIDTH = 10
BOARD_HEIGHT = 10
NUMBER_OF_MINES = 10


def main():
	"""Start game."""


def get_board():
	"""Returns underlying board of a minesweeper game. Using a dictionary"""


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



# If this program was run (instead of imported), run the game
if __name__ == "__main__":
	main()