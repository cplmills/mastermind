import constants
from game.scripting.action import Action
from game.shared.point import Point
from game.casting.peg import Peg
from game.shared.color import Color
from game.casting.guess import Guess


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        result = True
        # left
        current_guess = cast.get_first_actor("guess")    
        if self._keyboard_service.is_key_down('r'):
            result = current_guess.add_peg_to_guess(Peg(constants.RED))
        
        # right
        if self._keyboard_service.is_key_down('g'):
            result = current_guess.add_peg_to_guess(Peg(constants.GREEN))

        # up
        if self._keyboard_service.is_key_down('b'):
            result = current_guess.add_peg_to_guess(Peg(constants.BLUE))

        # down
        if self._keyboard_service.is_key_down('y'):
            result = current_guess.add_peg_to_guess(Peg(constants.YELLOW))

        # left
        if self._keyboard_service.is_key_down('o'):
            result = current_guess.add_peg_to_guess(Peg(constants.ORANGE))
        
        # right
        if self._keyboard_service.is_key_down('p'):
            result = current_guess.add_peg_to_guess(Peg(constants.PURPLE))
        
        # up
        if self._keyboard_service.is_key_down('w'):
            result = current_guess.add_peg_to_guess(Peg(constants.WHITE))
        
        # down
        if self._keyboard_service.is_key_down('t'):
            result = current_guess.add_peg_to_guess(Peg(constants.TURQUOISE))
        
        # If there is no more space in the current guess
        if not (result):
            board = cast.get_first_actor("board")
            board.add_guess_to_board(current_guess)
            cast.remove_actor("guess", current_guess)
            cast.add_actor("guess", Guess())
        

