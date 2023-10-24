def convertToLetter(number: int) -> str:
	return chr(96+number)

def convertToNumber(letter: str)-> int:
	return ord(letter) - 96