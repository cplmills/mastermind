import pyray
import constants
from game.casting.peg import Peg
from game.shared.point import Point
from random import shuffle

class VideoService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state 
    on the screen. 
    """

    def __init__(self, debug = False):
        """Constructs a new VideoService using the specified debug mode.
        
        Args:
            debug (bool): whether or not to draw in debug mode.
        """
        self._debug = debug

    def close_window(self):
        """Closes the window and releases all computing resources."""
        pyray.close_window()

    def clear_buffer(self):
        """Clears the buffer in preparation for the next rendering. This method should be called at
        the beginning of the game's output phase.
        """
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        if self._debug == True:
            self._draw_grid()
    
    def draw_peg(self, peg, ypos, xpos, centered=False):
        """Draws the pegs text on the screen.

        Args:
            peg (Actor): The actor to draw.
        """ 
        text = "O"
        y = ypos
        x = xpos

        pyray.draw_text(text, x*15, y+(y*15), 15, peg.get_color().to_tuple())

    def draw_board(self, cast):
        """ Draws the whole board on to the screen"""
        board = cast.get_first_actor("board").get_board()
        ypos = 4

        if (len(board) > 1):
            for guess in board:
                ypos += 1
                if (guess.get_length() == 4):
                    self.draw_guess(ypos, guess)
                    self.draw_codex(cast, guess, ypos)
    
    def draw_actors(self, actors, centered=False):
        """Draws the text for the given list of actors on the screen.

        Args:
            actors (list): A list of actors to draw.
        """ 
        for actor in actors:
            self.draw_actor(actor, centered)

    def draw_actor(self, actor, centered=False):
        """Draws the given actor's text on the screen.

        Args:
            actor (Actor): The actor to draw.
        """ 
        text = actor.get_text()
        x = actor.get_position().get_x()
        y = actor.get_position().get_y()
        font_size = actor.get_font_size()
        color = actor.get_color().to_tuple()

        if centered:
            width = pyray.measure_text(text, font_size)
            offset = int(width / 2)
            x -= offset
            
        pyray.draw_text(text, x, y, font_size, color)

    def draw_guess(self, ypos, guess):
        # Draws a completed guess to the screen
        xpos = 8
        guessno = 0
        if guess.get_nth_guess(guessno) != []:
            for peg in guess.get_pegs():
                self.draw_peg(peg, ypos, xpos+5)
                xpos += 1
                guessno += 1

    def draw_current_guess(self, guess):
        # Draws the current (incomplete) guess to the screen
        guess = guess.get_pegs()
        if (len(guess) != 0):
            for peg in guess:
                self.draw_peg(peg, 1, guess.index(peg))
        
    def draw_codex(self, cast, guess, y):
        # Draws the hint pegs to the side of each guess line
        secret = cast.get_first_actor("secret")
        clues = secret.check_pegs(guess)
        x = 24
        for peg in clues:
            x += 1
            self.draw_peg(peg, y, x)

    def flush_buffer(self):
        """Copies the buffer contents to the screen. This method should be called at the end of
        the game's output phase.
        """ 
        pyray.end_drawing()

    def is_window_open(self):
        """Whether or not the window was closed by the user.

        Returns:
            bool: True if the window is closing; false if otherwise.
        """
        return not pyray.window_should_close()

    def open_window(self):
        """Opens a new window with the provided title.

        Args:
            title (string): The title of the window.
        """
        pyray.init_window(constants.MAX_X, constants.MAX_Y, constants.CAPTION)
        pyray.set_target_fps(constants.FRAME_RATE)

    def _draw_grid(self):
        """Draws a grid on the screen."""
        for y in range(0, constants.MAX_Y, constants.CELL_SIZE):
            pyray.draw_line(0, y, constants.MAX_X, y, pyray.GRAY)
            
        for x in range(0, constants.MAX_X, constants.CELL_SIZE):
            pyray.draw_line(x, 0, x, constants.MAX_Y, pyray.GRAY)
    
    def _get_x_offset(self, text, font_size):
        width = pyray.measure_text(text, font_size)
        return int(width / 2)