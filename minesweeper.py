"""A game of minesweeper. The player must identify randomly placed mines.
A game is won if the player can identify all mines. A game is lost if the
player steps on a mine."""

import random

# Game characters to fill in on board.
EMPTY_SPACE = "_"
MINE = "m"

# Game constants
BOARD_WIDTH = 20
BOARD_HEIGHT = 20
NUMBER_OF_MINES = 30


def main():
	"""Runs a game of minesweeper."""

	print("""Mineseeper by Francisco Almeida. Find all mines on the board 
		without steping on one.""")

	board = get_board()
	cover_board = get_cover_board()


	while True:
		display_board(board, cover_board)
		x = input("Choose one square to opern X: ")
		y = input("Y: ")
		if x == 'q' or y == 'q':
			break
		open_square(board, cover_board, int(x), int(y))
		display_board(board, cover_board)
		if board[int(x), int(y)] == MINE:
			print("Game lost!!!")
			break





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
	adjacent_squares = get_adjacent_squares(x, y)
	num_of_adj_mines = 0
	for square in adjacent_squares:
		if square in mines:
			num_of_adj_mines += 1
	return num_of_adj_mines


def display_board(board, cover_board):
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
			if cover_board[(x, y)] == False:
				board_str += "[_]"
			else:
				board_str += f" {board[x, y]} "
		board_str += "\n"
	print(board_str)


def get_cover_board():
	"""Returns a layer board to cover clues and mines."""
	cover_board = {}
	for x in range(1, BOARD_WIDTH + 1):
		for y in range(1, BOARD_HEIGHT + 1):
			# This value is False for hidden squares and True for open squares
			cover_board[(x, y)] = False 
	return cover_board


def open_square(board, cover_board, x, y):
	"""Gradually opens squares."""
	cover_board[x, y] = True
	if board[(x, y)] == EMPTY_SPACE:
		open_adjacent_sqrs(cover_board, board, x, y)


def get_adjacent_squares(x, y):
	"""Returns a list of adjacent squares to a given square."""
	return [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x + 1, y),
		(x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]


def open_adjacent_sqrs(cover_board, board, x, y):
	"""Opens squares adjacent to empty squares. Recursive function.
	Calls itself whenever an adjacent square is empty."""
	adjacent_squares = get_adjacent_squares(x, y)
	for square in adjacent_squares:
		i, j = square
		if (i, j) in cover_board and cover_board[i, j] == False:
			cover_board[i, j] = True
			if board[i, j] == EMPTY_SPACE:
				open_adjacent_sqrs(cover_board, board, i, j)


# If this program was run (instead of imported), run the game
if __name__ == "__main__":
	main()