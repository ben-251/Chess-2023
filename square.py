from typing import List
from colours import *
from coordinates import convertToLetter

class Square:
	def __init__(self, position: List[int]):
		self.position = position
	
	def getColour(self) -> Colour:
		if self.position[0] % 2 == self.position[1] % 2:
			return Colour.BLACK
		else:
			return Colour.WHITE
	
	def translate(self, step):
		new_position = self.position
		new_position[0] += step[0]
		new_position[1] += step[1]
		return Square(new_position) # Questionable
	
