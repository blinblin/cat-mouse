from Turtle import Turtle
from Vector import *
from Color import *
import math
import sys
      
def see_mouse(cat):
  return cat.radius*cos((cat.angle-cat.mouse.angle)*math.pi/180)>=1.0

def check_statue(cat):
  return cat.radius < cat.statrad 
      
class Cat(Turtle):       #### Inherit behavior from Turtle
  """This cat runs along a circle"""
  def __init__(self, angle, radius, mouse, outline=black, fill=blue, width=1):
    self.position = mouse.center + unit(angle)*radius*mouse.statue.meter
    self.heading = angle - 90 
    self.center = mouse.center
    self.radius = radius
    self.angle = angle
    self.meter = mouse.statue.meter
    self.mouse = mouse
    self.statrad = mouse.statue.radius
    self.original_radius = radius
    self.original_pos = self.position
    self.original_angle = angle
    self.original_heading = angle - 90
    self.style = dict(outline=outline, fill=fill, width=width)
    
  def getnextstate(self):
    old_angle = self.angle
    mouse_angle = self.mouse.angle
    new_angle = self.angle - 360*1.25/(self.radius*2*math.pi)
    
    if (self.radius == 1 and 
    cos((mouse_angle-new_angle)*math.pi/180) > cos((old_angle-new_angle)*math.pi/180) and
    cos((old_angle-mouse_angle)*math.pi/180) > cos((old_angle-new_angle)*math.pi/180)):
      print "Cat Caught The Mouse"
#      sys.exit()
      
    if see_mouse(self):
      self.radius = self.radius - 1
      if check_statue(self):
        self.radius = self.statrad
      self.position = self.center + unit(self.angle)*self.radius*self.meter
    else:
      self.angle = new_angle
      self.position = self.center + unit(self.angle)*self.radius*self.meter
      self.heading = self.angle - 90
    return self.position, self.heading
    
  def reset(self):
    self.angle = self.original_angle
    self.radius = self.original_radius
    return self.original_pos, self.original_heading
    
  def type(self):
    return "cat"