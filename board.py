from typing import List
from pieces import Piece
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
				self.squares.append(Square([file, rank]))

	def getPieceOnSquare(self,square: Square):
		"""
        Returns the piece on the specified square, or None if the square is unoccupied.

        Parameters:
        - square: Square object representing the location on the board.
        """
		for piece in self.pieces:
			if piece.position == square:
				return piece
		return None

	def isMoveValid(self, piece:Piece, endPosition:Square) -> bool:
		'''
		Returns true if the move is valid according to the rules of chess, 
		checking for things like pieces between, checks, etc.
		''' 
		if self.isPathObstructed(piece, endPosition):
			return False
		if self.isSquareOccupied(piece, endPosition):
			return False
	
		raise NotImplementedError

	def isPathObstructed(self, piece:Piece, endPosition:Square):
		'''
		Returns true if there is a piece between the piece and it's destination.
		'''
		# get a generator function and loop through until you reach end position or a piece has been hit
	
	def isSquareOccupied(self, piece: Piece, endPosition: Square):
		'''
		Returns true if there is a piece of the same colour on that square.
		'''
		...
