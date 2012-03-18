"""This module uses the convention that x increases toward the right and
y increases downwards, as when drawing on the screen.  All angles are in
degrees.  A direction of 0 is up, 90 is right, 180 is down, and 270 is left."""

from math import sin, cos, atan2, pi

class Vector:
    """Objects of this class are two-dimensional vectors."""

    def __init__(self, x=0, y=0):
        self.x, self.y = float(x), float(y)

    def __add__(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y)

    def __sub__(self, vector):
        return Vector(self.x - vector.x, self.y - vector.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return self*scalar

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def dot(self, vector):
        return self.x*vector.x + self.y*vector.y

    def length(self):
        return (self.x*self.x + self.y*self.y)**0.5

    def unit(self):
        """Return the unit vector parallel to this vector."""
        return Vector(self.x/self.length(), self.y/self.length())

    def direction(self):
        """Return the direction of this vector as an angle in degrees."""
        return 180 - atan2(self.x, self.y)*180/pi

    def rotate(self, angle):
        """Return this vector rotated clockwise by an angle in degrees."""
        radians = angle*pi/180
        return Vector(self.x*cos(radians) - self.y*sin(radians),
                      self.x*sin(radians) + self.y*cos(radians))

def unit(direction):
    """Return a unit vector in the given direction."""
    return Vector(0, -1).rotate(direction)