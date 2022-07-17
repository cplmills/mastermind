import constants
from game.casting.cast import Cast
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point
from game.casting import secret
from game.casting import peg
from game.casting.actor import Actor
from game.casting.secret import Secret
from game.casting.guess import Guess
from game.casting.board import Board
from game.scripting.handle_end_game import HandleEndGame

def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("guess", Guess())    # creates a blank array for holding a set of 4 guesses
    cast.add_actor("secret", Secret())  # Initialise a new secret combination of 4 pegs
    cast.add_actor("board", Board())    # initialises board to hold 12 guesses

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", HandleEndGame(cast, script))
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()