from game.casting.actor import Actor
from game.shared.point import Point
import constants

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, video_service):
        """Constructs a new Director using the specified video service.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service
        
    def start_game(self, cast, script):
        """Starts the game using the given cast and script. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
            script (Script): The script of actions.
        """
        self._video_service.open_window()

        # write instructions and headings to screen
        message1 = Actor()
        message2 = Actor()
        message3 = Actor()
        message4 = Actor()
        message5 = Actor()
        message6 = Actor()
        heading1 = Actor()
        heading2 = Actor()

        headtxt1 = "Current Guess"
        headtxt2 = "Past Guesses               Hints"
        
        text1 = "Mastermind"
        text2 = "I have a secret code, you have to guess it!"
        text3 = "Choose from (W)hite, (R)ed, (T)urquoise, (Y)ellow, (O)range, (P)urple, (G)reen, or (B)lue Colors"
        text4 = "I will tell you if you have a peg in the correct place with a red peg" 
        text5 = "or if you have the right color in the wrong place with a white peg"
        text6 = "You have 12 guesses to figure it out!"

        message1.set_text(text1)
        message2.set_text(text2)
        message3.set_text(text3)
        message4.set_text(text4)
        message5.set_text(text5)
        message6.set_text(text6)

        heading1.set_text(headtxt1)
        heading2.set_text(headtxt2)

        x = int(constants.MAX_X / 2)
        y = 30
        message1.set_position(Point(x, (y+1)*constants.CELL_SIZE))
        message2.set_position(Point(x, (y+2)*constants.CELL_SIZE))
        message3.set_position(Point(x, (y+3)*constants.CELL_SIZE))
        message4.set_position(Point(x, (y+4)*constants.CELL_SIZE))
        message5.set_position(Point(x, (y+5)*constants.CELL_SIZE))
        message6.set_position(Point(x, (y+6)*constants.CELL_SIZE))

        heading1.set_position(Point(4*constants.CELL_SIZE,0))
        heading2.set_position(Point(20*constants.CELL_SIZE, 5*constants.CELL_SIZE))
        
        cast.add_actor("messages", message1)
        cast.add_actor("messages", message2)
        cast.add_actor("messages", message3)
        cast.add_actor("messages", message4)
        cast.add_actor("messages", message5)
        cast.add_actor("messages", message6)
        cast.add_actor("messages", heading1)
        cast.add_actor("messages", heading2)

        while self._video_service.is_window_open():
            self._execute_actions("input", cast, script)
            self._execute_actions("update", cast, script)
            self._execute_actions("output", cast, script)
        self._video_service.close_window()

    def _execute_actions(self, group, cast, script):
        """Calls execute for each action in the given group.
        
        Args:
            group (string): The action group name.
            cast (Cast): The cast of actors.
            script (Script): The script of actions.
        """
        actions = script.get_actions(group)    
        for action in actions:
            action.execute(cast, script)    

 