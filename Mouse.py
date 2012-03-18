from Turtle import Turtle
from Vector import *
from Color import *
import math
      
class Mouse(Turtle):       #### Inherit behavior from Turtle
  """This mouse runs along a circle"""
  def __init__(self, statue, angle, outline=black, fill=red, width=1):
    self.position = statue.position + unit(angle)*statue.radius*statue.meter
    self.heading = angle - 90 
    self.center = statue.position
    self.radius = statue.radius
    self.angle = angle
    self.meter = statue.meter
    self.statue = statue
    self.ori_pos = self.position
    self.ori_head = angle - 90
    self.ori_ang = angle
    self.style = dict(outline=outline, fill=fill, width=width)
    
  def getnextstate(self):
    self.angle = self.angle - 360/(self.radius*2*math.pi)
    self.position = self.center + unit(self.angle)*self.radius*self.meter
    self.heading = self.angle - 90
    return self.position, self.heading
    
  def reset(self):
    self.angle = self.ori_ang
    return self.ori_pos, self.ori_head
    
  def type(self):
    return "mouse"