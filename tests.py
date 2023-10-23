import bentests as bt
from board import *
import colours
from output import OutputManager

output_manager = OutputManager()

class Display(bt.testCase):
	def testFirstBoardRow(self):
		board = Board()
		row = output_manager.getNthRowDisplay(board, 1)
		bt.assertEquals(row,f"{colours.CLEAR}|{colours.GREY}|{colours.CLEAR}") #TODO: finish this.

class PieceMethods(bt.testCase):
	...

class BoardCreation(bt.testCase):
	def testBoardSizeIsString(self):
		with bt.assertRaises(ValueError):
			board = Board(size="a") #type: ignore Cuz it's wrong on purpose

bt.test_all(
	Display, 
	PieceMethods,
	BoardCreation
)
