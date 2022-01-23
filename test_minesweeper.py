import minesweeper

# print(minesweeper.get_mine_places())

# print(minesweeper.get_board())

board = minesweeper.get_board()
cover_board = minesweeper.get_cover_board()

print(minesweeper.display_board(board, cover_board))

minesweeper.refresh_cover_board(cover_board, 1, 2)

print(minesweeper.display_board(board, cover_board))