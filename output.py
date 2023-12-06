from board import Board
from colours import Colour

class OutputManager:
	def getNthRowDisplay(self, board: Board, n: int) -> str:
		output = ""
		CLEAR = Colour.CLEAR.value
		output += CLEAR
		output += f"{str(n)} "
		for i, square in enumerate(board.squares):
			if square.position[1] != n:
				continue
			output += CLEAR + "|"
			output += square.getColour().value
			piece_on_square = board.getPieceOnSquare(square)
			if not piece_on_square is None:
				output += piece_on_square.symbol # display uppercase if black
			else:
				output += " "
			if i == board.size-1:
				output += CLEAR + "|"
		output += CLEAR
		return output