from colorama import init
from colours import Colour
from square import Square

class VacantSquare(Exception):
	...

class Piece:
	'''
	Base Class for all Pieces. Most methods and attributes go here, and can be overloaded if necessary.
	'''
	def __init__(self, position: Square, colour: Colour):
		self.position = position
		self.colour = colour
		self.symbol = " "
	
	def isMoveValid(self, endPosition) -> bool:
		# use the current position and see if it's possible to move to the new square
		raise NotImplementedError
		

class Pawn(Piece): ...

class Bishop(Piece): ...

class Knight(Piece): ...

class Rook(Piece): ...

class King(Piece): ...

class Queen(Piece): ...