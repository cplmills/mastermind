from game.casting.actor import Actor
from game.casting.peg import Peg
from game.casting.cast import Cast

class Guess(Actor):
    """A Guess containing 4 colored pegs. 
    
    The responsibility of Guess is to keep track of the pegs in each guess made by the player.

    Attributes:
        _guess (list): The guess made by the player, it will contain 4 colored pegs when complete

    """
    def __init__(self):
        super().__init__()
        self._guess = []

    def add_peg_to_guess(self, color):
        # Accepts a color object, assigns that color to a new peg within the current guess
        # returns True if there is still space in the guess, false if the guess is full
        
        if (len(self._guess) < 4):
            self._guess.append(color)
        
        return False if (len(self._guess) == 4) else True
             
    def get_nth_guess(self, n):
        # returns a peg from the current guess
        if (len(self._guess) == 0):
            return []
        else:
            return self._guess[n]

    def get_length(self):
        # returns the length of the guess - how many pegs it currently holds
        return len(self._guess)

    def get_pegs(self):
        # returns the current guess
        return self._guess

