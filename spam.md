following the tdd principle, i'm not writing any code for a thing until i have a failing test for that thing. for example, i just made a thing to test that a certain exception is raised when the board size entered is a string. I'm now going to implement.

23-10-23 19:40: 
just realised i can do:
```python
# piece class
def isMoveValid(board, destination_square):
	... 
```
instead of:
```python
def determineValidSquares(<loads of stuff>):
	...
```
the main advantage, i think, is that this is easier to split up into multiple methods.

the two approaches can be summarised as:
- many valid checks, one move (at a time)
- one valid check, many moves (at once)

i've decided a few things:
1. players dont have pieces, they have colours, and so do pieces. white piece. white's move.
2. instead of a board with squares, we'll just have square objects be the positions that pieeces can have.
   so asking "what square are you on?" really does mean which square object shares a position with the piece


   square with piece property 
   or piece with position property?