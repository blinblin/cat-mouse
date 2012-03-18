from Turtle import Turtle
from Vector import *
from Color import *
  
def circle(pos,vector,rad,num):
  a = []
  for x in range(num):
    a.append(pos+vector.rotate(x*(360/num))*rad) 
  return a
  
      
class Statue(Turtle):       #### Inherit behavior from Turtle
  """This statue stands still"""
  def __init__(self, position, radius, meter, outline=black, fill=white, width=1):
    self.position, self.heading, self.radius = position, 0, radius
    self.meter = meter
    self.style = dict(outline=outline, fill=fill, width=width)
  
  def getshape(self):
    """Return a list of vectors giving the polygon for this turtle."""
    forward = unit(self.heading)
    a = circle(self.position,forward,self.radius*self.meter,40)
    return a