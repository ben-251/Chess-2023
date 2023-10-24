import bentests as bt
from board import *
from colours import Colour
from output import OutputManager
from square import Square

output_manager = OutputManager()

class Display(bt.testCase):
	def testDisplay1stRank(self):
		board = Board()
		row = output_manager.getNthRowDisplay(board, 1)
		expected_output = f"{Colour.CLEAR.value}1 " + f"{Colour.CLEAR.value}|{Colour.BLACK.value} {Colour.CLEAR.value}|{Colour.WHITE.value} "*4 +f"{Colour.CLEAR.value}|{Colour.CLEAR.value}"
		bt.assertEquals(row,expected_output)

class PieceMethods(bt.testCase):
	...

class BoardCreation(bt.testCase):
	def testBoardSizeIsString(self):
		with bt.assertRaises(ValueError):
			board = Board(size="a") # type: ignore Cuz it's wrong on purpose

class Squares(bt.testCase):
	def testSquareString(self):
		bt.assertEquals(str(Square((1,1))),"a1") 

bt.test_all(
	Display, 
	PieceMethods,
	BoardCreation,
	Squares
)
