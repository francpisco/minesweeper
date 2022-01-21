"""A game of minesweeper. The player must identify randomly placed mines.
A game is won if the player can identify all mines. A game is lost if the
player steps on a mine."""

class Game:
	"""Main class of game. Starting point."""

	def __init__(self):
		"""Initialize game"""
		self.board = Board()


class Board:
	"""Where board of game is defined. A board is a 2D object which contains
	mines and cues."""

	def __init__(self):
		"""Initialize board"""
		