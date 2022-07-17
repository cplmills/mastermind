from game.shared.color import Color
from game.shared.point import Point
from game.casting.actor import Actor

class Peg(Actor):
    """A colored peg. The peg is responsible for holding its color  
    
    Attributes:
        

    """
    def __init__(self, color):
        super().__init__()
        self.set_color(color)


