from random import random

class Color:
    """An instance of Color is a color value represented as three floats
       from 0.0 to 1.0 that indicate the red, green, and blue components."""

    def __init__(self, r, g, b):
        self.r, self.g, self.b = r, g, b

    def __repr__(self):
        return 'Color(%f, %f, %f)' % (self.r, self.g, self.b)

    def __str__(self):
        """Convert this Color to a string usable with Tk, HTML, or CSS."""
        return '#%02x%02x%02x' % (self.r*255, self.g*255, self.b*255)

    def invert(self):
        """Return the inverse of this color."""
        return Color(1 - self.r, 1 - self.g, 1 - self.b)

    def lighten(self, amount=0.5):
        """Lighten this color by blending it towards white."""
        return self.blend(white, amount)

    def darken(self, amount=0.5):
        """Lighten this color by blending it towards black."""
        return self.blend(black, amount)

    def blend(self, color, amount=0.5):
        """Blend a color towards another color."""
        return Color(self.r*(1-amount) + color.r*amount,
                     self.g*(1-amount) + color.g*amount,
                     self.b*(1-amount) + color.b*amount)

    def multiply(self, color):
        """Multiply this color together with another color."""
        return Color(self.r*color.r, self.g*color.g, self.b*color.b)

white = Color(1, 1, 1)
grey = Color(0.5, 0.5, 0.5)
black = Color(0, 0, 0)

red = Color(1, 0, 0)
orange = Color(1, 0.5, 0)
yellow = Color(1, 1, 0)
green = Color(0, 1, 0)
cyan = Color(0, 1, 1)
blue = Color(0, 0, 1)
purple = Color(0.5, 0, 1)
magenta = Color(1, 0, 1)

def randomcolor():
    """Generate a random color."""
    return Color(random(), random(), random())