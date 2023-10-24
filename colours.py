'''
Arguably overused enum used for:
- piece colours
- square colours (and display)
- player colours
'''

import colorama
from enum import Enum

class Colour(Enum):
	BLACK = colorama.Back.BLACK + colorama.Fore.WHITE
	WHITE = colorama.Back.WHITE + colorama.Fore.BLACK
	CLEAR = colorama.Back.RESET + colorama.Fore.RESET
	RED = colorama.Back.RED + colorama.Fore.BLACK