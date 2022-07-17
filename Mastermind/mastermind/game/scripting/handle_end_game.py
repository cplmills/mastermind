from game.scripting.action import Action
import constants
from game.shared.point import Point
from game.casting.actor import Actor

class HandleEndGame(Action):
    """ Assists the director in ending the game. 
    
    The responsibility of HandleEndGame is to check if the game has been won or lost or if play should continue

    Attributes:
        _win (bool): A boolean indicating if the game has been won

    """
    def __init__(self, cast, script):
        super().__init__()
        self._win = False
        
    def game_over(self, cast, script):
        # sets up the final message on screen and prevents further gameplay
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)
        position = Point(x, y)

        message = Actor()
        winner_is = f"You WIN!" if self._win else "Try Again Another Time!" 
        message.set_text(f"Game Over! "+ winner_is)
        message.set_position(position)
        cast.add_actor("messages", message)
        script.remove_actions("input")

    def execute(self, cast, script):
        check = cast.get_first_actor("board")
        
        if cast.get_first_actor("secret").count_red_pegs() == 4:
            self._win = True
            self.game_over(cast, script)

        if check.get_length() == 13:
            self.game_over(cast, script)

    