from typing import List
from pieces import VacantSquare, Piece
from square import Square

class Board:
	def __init__(self, size: None | int = None):
		if size is None:
			size = 8
		if not isinstance(size, int):
			raise ValueError("Board Size must be an integer")
		self.pieces: List[Piece] = []
		self.size = size
		self.createBoard()
	
	def createBoard(self):
		self.squares: List[Square] = []
		for rank in range(1,9):
			for file in range(1,9):
				self.squares.append(Square((file, rank)))

	def findPieceOnSquare(self,square: Square):
		for piece in self.pieces:
			if piece.position == square:
				return piece
		raise VacantSquare()