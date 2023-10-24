from board import Board
from colours import Colour
from pieces import VacantSquare

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
			try:
				output += board.findPieceOnSquare(square).symbol
			except VacantSquare:
				output += " "
			if i == board.size-1:
				output += CLEAR + "|"
		output += CLEAR
		return output