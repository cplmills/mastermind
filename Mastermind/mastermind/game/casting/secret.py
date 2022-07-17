import constants
from random import randint
from game.casting.actor import Actor
from game.casting.peg import Peg
from game.shared.color import Color

class Secret(Actor):
    """The secret 4 peg combination that needs to be guessed to win the game. 
    
    The responsibility of secret is to keep track of and report on the accuracy of the players guess against the secret code.

    Attributes:
        _secret (list): a list of 4 pegs that make up the seret code
        _colors (list): a list of available color choices for the player to make 
        _solve_pegs (list): a list of 4 pegs that contain the hints (white and red pegs) to help the player guess the correct code

    """
    def __init__(self):
        super().__init__()
        self._secret = []
        self._colors = ["RED", "GREEN", "BLUE", "ORANGE", "WHITE", "YELLOW", "PURPLE", "TURQUOISE"]
        self._solve_pegs = []

        while len(self._secret) < 4:
            random_color = self._colors[randint(0, 7)]
            random_color = Color.get_RGB(random_color)
            self._secret.append(Peg(Color(random_color[0], random_color[1], random_color[2])))

    def check_pegs(self, guess):
        # Returns an array of red and white pegs depending on the guess made
        # a red peg indicates a correct guess in the correct space
        # a white peg indicates a correct guess in the wrong space
        solve = []
        current_guess_peg = 0

        for peg in  guess.get_pegs():
            current_guess_peg += 1
            current_secret_peg = 0
            guess_peg_color = peg.get_color()
            same_place = False
            found_color = False 
            for secret_peg in self._secret:
                current_secret_peg += 1
                secret_peg_color = secret_peg.get_color()
                if (secret_peg_color.to_tuple() == guess_peg_color.to_tuple()):
                    found_color = True
                    if ((current_guess_peg == current_secret_peg)):
                        same_place = True
            if (same_place or found_color):
                if (same_place == True):
                    solve.append(Peg(constants.RED))
                else:
                    solve.append(Peg(constants.WHITE))
        self._solve_pegs = solve

        return solve

    def count_red_pegs(self):
        # Returns the number of red pegs (correct guess in the correct space) in the current guess
        redcount = 0
        for pin in self._solve_pegs:
            if pin.get_color().is_red():
                redcount += 1
        return redcount