from colours import Colour

class Player: 
	def __init__(self, colour: Colour):	
		self.colour: Colour = colour # pieces might not need colour since the players have it, or maybe its the colour that will be used to tell if it's 
	...