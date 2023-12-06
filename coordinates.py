from typing import Tuple
#TODO: make a-h -> 7-0; 1-8 -> 0-7
# meaning a1 -> (7,0)

def convertToLetter(number: int) -> str:
	return chr(96+number)

def convertToNumber(letter: str)-> int:
	return ord(letter) - 96

def coordinateToTuple(coordinate: str) -> Tuple[int, int]:
	return convertToNumber(coordinate[0]), int(coordinate[1])

def tupleToCoordinate(tuple: Tuple[int,int]) -> str:
	return f"{convertToLetter(tuple[0])}{tuple[1]}"

