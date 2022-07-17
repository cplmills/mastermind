class Color:
    """A color.

    The responsibility of Color is to hold and provide information about itself. Color has a few 
    convenience methods for comparing them and converting to a tuple.

    Attributes:
        _red (int): The red value.
        _green (int): The green value.
        _blue (int): The blue value.
        _alpha (int): The alpha or opacity.
    """
    
    def __init__(self, red, green, blue, alpha = 255):
        """Constructs a new Color using the specified red, green, blue and alpha values. The alpha 
        value is the color's opacity.
        
        Args:
            red (int): A red value.
            green (int): A green value.
            blue (int): A blue value.
            alpha (int): An alpha or opacity.
        """
        self._red = red
        self._green = green
        self._blue = blue 
        self._alpha = alpha

    def is_red(self):
        return True if self._red == 255 and self._green == 0 and self._blue == 0 else False
    
    def to_tuple(self):
        """Gets the color as a tuple of four values (red, green, blue, alpha).

        Returns:
            Tuple(int, int, int, int): The color as a tuple.
        """
        return (self._red, self._green, self._blue, self._alpha)   

    def get_RGB(color):
        # returns a list containing the RGB codes for the supplied color
        if color == "WHITE":
            return [255, 255, 255, 0]
        elif color == "RED":
            return [255, 0, 0, 0]
        elif color == "YELLOW":
            return [255, 255, 0, 0]
        elif color == "GREEN":
            return [0, 255, 0, 0]
        elif color == "BLUE":
            return [0, 0, 255, 0]
        elif color == "ORANGE":
            return [255, 127, 0, 0]
        elif color == "PURPLE":
            return [177, 156, 217, 0]
        elif color == "TURQUOISE":
            return [64, 244, 208, 0]
        elif color == "BLACK":
            return [0, 0, 0, 0]