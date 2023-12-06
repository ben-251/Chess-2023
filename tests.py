import bentests as bt
from board import *
from colours import Colour
from output import OutputManager
from square import Square
from coordinates import *

output_manager = OutputManager()

class Display(bt.testGroup):
	def testDisplay1stRank(self):
		board = Board()
		row = output_manager.getNthRowDisplay(board, 1)
		expected_output = f"{Colour.CLEAR.value}1 " + f"{Colour.CLEAR.value}|{Colour.BLACK.value} {Colour.CLEAR.value}|{Colour.WHITE.value} "*4 +f"{Colour.CLEAR.value}|{Colour.CLEAR.value}"
		bt.assertEquals(row,expected_output)

class PieceMethods(bt.testGroup):
	...

class BoardCreation(bt.testGroup):
	def testBoardSizeIsString(self):
		with bt.assertRaises(ValueError):
			board = Board(size="a") # type: ignore Cuz it's wrong on purpose

class Coordinates(bt.testGroup):
	def testSquareAsCoordinate(self):
		bt.assertEquals(tupleToCoordinate((1,1)),"a1") 

	def testCoordinateAsSquare(self):
		bt.assertEquals(coordinateToTuple("h4"),(8,4))
		
bt.test_all(
	Display, 
	PieceMethods,
	BoardCreation,
	Coordinates
)
