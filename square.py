from typing import Tuple
from colours import *
from coordinates import convertToLetter

class Square:
	def __init__(self, position: Tuple[int, int]):
		self.position = position
	
	def getColour(self) -> Colour:
		if self.position[0] % 2 == self.position[1] % 2:
			return Colour.BLACK
		else:
			return Colour.WHITE
	
