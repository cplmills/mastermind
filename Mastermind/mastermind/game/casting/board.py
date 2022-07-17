from game.casting.guess import Guess

class Board():
    """A space on the screen to hold all of the players guesses and hints. 
    
    The responsibility of Board is to display the output from the game in 2d 
    space.

    Attributes:
        _board (list of Guess objects): A list of guesses made by the player in the game

    """
    def __init__(self):
        # setup a board with 12 banks of guesses
        self._board = [Guess()]

    def get_board(self):
        # returns the entire board (all guesses)
        return self._board

    def add_guess_to_board(self, guess):
        # adds a guess to the board
        self._board.append(guess)

    def get_guess(self, num):
        # returns a particular guess (num) from the board
        return self._board[num]

    def get_length(self):
        # returns the length of the board - the number of guesses made by the player so far
        return len(self._board)

