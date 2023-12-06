from colorama import init
from colours import Colour
from square import Square
from typing import List

class Piece:
	'''
	Base Class for all Pieces. Most methods and attributes go here, and can be overloaded if necessary.
	'''
	def __init__(self, position: Square, colour: Colour):
		self.position = position
		self.colour = colour
		self.backrank = self.getBackrank()
		self.symbol = " "
	
	def getBackrank(self):
		match self.colour:
			case Colour.BLACK:
				backrank = 0 # top to bottom, black is on "top"
			case Colour.WHITE:
				backrank = 7

	def getPossibleSquares(self):
		'''
		Returns the squares on the board that the piece can theoretically move to.
		Ignores blocking pieces, checks, etc.
		'''
		possible_squares:List[Square] = []
		for step in self.getPossibleStepDeltas():
			possible_squares.append(self.position.translate(step))

	def getSquaresBetween(self,startPosition:Square, endPosition:Square):
		...

	def getPossibleStepDeltas(self):
		'''
		Gets the possible steps to move to each square. 
		For example a pawn can either move (0,1) or (0,2).
		a knight: (1,2), (1,-2), (-1,-2), (-1,2), (2,1), ...
		'''
		return []
		

class Pawn(Piece): 
	symbol = "p"
	def __init__(self,position, colour):
		super().__init__(position, colour)
		self.direction = self.getDirection()

	def getDirection(self):
		match self.colour:
			case Colour.WHITE:
				direction = -1 # read top to bottom, white is going backwards.
			case Colour.BLACK:
				direction = 1
			case _:
				raise ValueError("Invalid colour")
		return direction
			

class Bishop(Piece):
	symbol = "b"

class Knight(Piece):
	symbol = "n"

class Rook(Piece):
	symbol = "r"

class King(Piece):
	symbol = "k"

class Queen(Piece):
	symbol = "q"