from Tkinter import *                  # Import everything from Tkinter
from Arena   import Arena               # Import our Arena
from Turtle  import Turtle             # Import our Turtle
from Vector  import *                  # Import everything from our Vector
from WalkingTurtle import *
from Statue import Statue
from Mouse import Mouse
import Cat

meter = 20        # How many pixels is one meter?
statue_radius = 1# What is the statue's radius
cat_radius = 1.5
cat_angle = 0
mouse_angle = 45

x = Vector()
print x.length()

tk = Tk()                              # Create a Tk top-level widget
arena = Arena(tk)                      # Create an Arena widget, arena
arena.pack()                           # Tell arena to pack itself on screen
s = Statue(Vector(200,200),statue_radius,meter)
arena.add(s)
m = Mouse(s,mouse_angle)
c = Cat.Cat(cat_angle,cat_radius,m)
arena.add(c)
arena.add(m)
arena.cat_rad.set('CatRadius: '+str(cat_radius))
arena.cat_rad_label = Label(arena,textvariable=arena.cat_rad)
arena.cat_rad_label.pack()
arena.cat_ang.set('CatAngle: '+str(cat_angle))
arena.cat_ang_label = Label(arena,textvariable=arena.cat_ang)
arena.cat_ang_label.pack()
arena.mouse_ang.set('CatAngle: '+str(mouse_angle))
arena.mouse_ang_label = Label(arena,textvariable=arena.mouse_ang)
arena.mouse_ang_label.pack()


tk.config(menu=arena.menu)
tk.mainloop()                          # Enter the Tkinter event loop