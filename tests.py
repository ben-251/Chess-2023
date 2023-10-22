import bentests as bt
from board import *

class Display(bt.testCase):
	...

class PieceMethods(bt.testCase):
	...

class BoardCreation(bt.testCase):
	def testBoardSizeIsString(self):
		with bt.assertRaises(ValueError): # or even a custom exception
			board = Board(size="a") #type: ignore Cuz it's wrong on purpose

bt.test_all(
	Display, 
	PieceMethods,
	BoardCreation
)
