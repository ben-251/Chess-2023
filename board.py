class Board:
	def __init__(self, size: None | int = None):
		if size is None:
			self.size = 8
		if not isinstance(size, int):
			raise ValueError("Board Size must be a string")