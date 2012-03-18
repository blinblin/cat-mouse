from Turtle import Turtle
from Vector import *
from Color import *

class WalkingTurtle(Turtle):       #### Inherit behavior from Turtle
    """This turtle walks in a straight line forever."""

    def __init__(self, position, heading, speed, fill=blue, **style):
        Turtle.__init__(self, position, heading, fill=fill, **style)
        self.speed = speed

    def getnextstate(self):
        """Advance straight ahead."""
        return self.position + unit(self.heading)*self.speed, self.heading