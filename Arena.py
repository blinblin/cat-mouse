from Tkinter import *
from math import sin, cos, pi
from Vector import *
from Color import *

class Arena(Frame):
    """This class provides the user interface for an arena of turtles."""

    def __init__(self, parent, width=400, height=400, **options):
        Frame.__init__(self, parent, **options)
        self.width, self.height = width, height
        self.canvas = Canvas(self, width=width, height=height)
        self.canvas.pack()
        parent.title("UC Bereley CS9H Turtle Arena")
        Button(self, text='step', command=self.step).pack(side=LEFT)
        Button(self, text='run', command=self.run).pack(side=LEFT)
        Button(self, text='stop', command=self.stop).pack(side=LEFT)
        Button(self, text='reset', command=self.reset).pack(side=LEFT)
        Button(self, text='quit', command=parent.quit).pack(side=LEFT)
        
        Lb1 = Listbox(self) #listbox for mouse color
        Lb1.insert(1, "Red")
        Lb1.insert(2, "Orange")
        Lb1.insert(3, "Yellow")
        Lb1.insert(4, "Green")
        Lb1.insert(5, "Cyan")
        Lb1.insert(6, "Purple")
        Lb1.insert(7, "Magenta")
        Lb1.insert(8, "Grey")
        Lb1.insert(9, "Black")
        Lb1.insert(10, "White")
        
        self.colordict = {} #dictionary to turn listbox selection into color
        self.colordict[0] = red
        self.colordict[1] = orange
        self.colordict[2] = yellow
        self.colordict[3] = green
        self.colordict[4] = cyan
        self.colordict[5] = purple
        self.colordict[6] = magenta
        self.colordict[7] = grey
        self.colordict[8] = black
        self.colordict[9] = white
        self.mousecolor = Lb1
        self.mousecolor.bind('<<ListboxSelect>>', self.updatecolor)
        Lb1.pack(side=RIGHT)
        
        menubar = Menu(self) #setting up the menu
        filemenu = Menu(menubar,tearoff=0)
        filemenu.add_command(label='About...', command=self.about)
        filemenu.add_command(label='Quit', command=parent.quit)
        menubar.add_cascade(label='File', menu=filemenu)
        self.menu = menubar
        
        self.turtles = []
        self.items = {}
        self.reset_bool = 0
        self.running = 0
        self.period = 10 # milliseconds
        self.canvas.bind('<ButtonPress>', self.press)
        self.canvas.bind('<Motion>', self.motion)
        self.canvas.bind('<ButtonRelease>', self.release)
        
        self.time = 0 #setting up time label
        self.time_text = StringVar()
        self.time_text.set('Time: '+str(self.time))
        self.time_label = Label(self,textvariable=self.time_text)
        self.time_label.pack()
        
        self.cat_rad = StringVar() #cat radius string
        self.cat_ang = StringVar() #cat angle string
        self.mouse_ang = StringVar() #mouse angle string
        
        self.dragging = None
        
    def about(self): #the about window setup
      about = Toplevel(self)
      about.title("About the UC Berkeley CS9H Turtle Arena")
      about.geometry("300x400")
      Message(about, text="Cat and Mouse Simulation",width=200).pack()
      Message(about, text="by").pack()
      Message(about, text="Adam Wang and Boris Lin",width=200).pack()
      adam = PhotoImage(file="adam.gif")
      l = Label(about, image=adam)
      l.photo = adam
      l.pack()
      Button(about, text='Ok', command=about.destroy).pack()
      

    def press(self, event):
        dragstart = Vector(event.x, event.y)
        for turtle in self.turtles:
            if (dragstart - turtle.position).length() < 10:
                self.dragging = turtle
                self.dragstart = dragstart
                self.start = turtle.position
                return

    def motion(self, event):
        drag = Vector(event.x, event.y)
        if self.dragging:
            self.dragging.position = self.start + drag - self.dragstart
            if self.dragging.type() == "cat": #if i'm dragging a cat, then I want to update it's heading,angle,and radius
              self.dragging.heading = (self.dragging.position-self.dragging.center).direction() - 180
              self.dragging.angle = (self.dragging.position-self.dragging.center).direction()
              self.dragging.radius = (self.dragging.position-self.dragging.center).length()/self.dragging.meter
              if self.dragging.radius < 1: #check if i'm dragging into statue
                self.dragging.radius = 1
                self.dragging.position = self.dragging.center + unit(self.dragging.angle)*self.dragging.radius*self.dragging.meter
            self.cat_ang.set('CatAngle: '+str(self.dragging.angle)) #updating catangle label
            self.cat_rad.set('CatRadius: '+str(self.dragging.radius)) #updating catradius label
            self.update(self.dragging)
        for turtle in self.turtles:
          if turtle.type() == "cat": #if my mouse is within 10 pixels of the cat, change its color
            if (drag - turtle.position).length() < 10:
              turtle.style['fill']=black
              self.update(turtle)
            else:
              turtle.style['fill']=blue
              self.update(turtle)
              

    def release(self, event):
        self.dragging = None

    def update(self, turtle):
        """Update the drawing of a turtle according to the turtle object."""
        item = self.items[turtle]
        vertices = [(v.x, v.y) for v in turtle.getshape()]
        self.canvas.coords(item, sum(vertices, ()))
        self.canvas.itemconfigure(item, **turtle.style)
        
    def add(self, turtle):
        """Add a new turtle to this arena."""
        self.turtles.append(turtle)
        self.items[turtle] = self.canvas.create_polygon(0, 0)
        self.update(turtle)

    def step(self, stop=1):
        """Advance all the turtles one step."""
        
        if self.reset_bool: #prevents stepping once after pressing reset while running
          self.reset_bool = 0
          return
        nextstates = {}
        
        self.time+=1 #increment step count
        self.time_text.set('Time: '+str(self.time))
        
        for turtle in self.turtles:
            nextstates[turtle] = turtle.getnextstate()
        for turtle in self.turtles:
            turtle.setstate(nextstates[turtle])
            self.update(turtle)
            
        for turtle in self.turtles: #update cat and mouse angle and radius
          if turtle.type() == "cat":
            self.cat_rad.set('CatRadius: '+str(turtle.radius))
            self.cat_ang.set('CatAngle: '+str(turtle.angle%360))
          if turtle.type() == "mouse":
            self.mouse_ang.set('MouseAngle: '+str(turtle.angle%360))
            
        if stop:
            self.running = 0
        

    def run(self):
        """Start the turtles running."""
        self.running = 1
        self.loop()

    def loop(self):
        """Repeatedly advance all the turtles one step."""
        self.step(0)
        if self.running:
            self.tk.createtimerhandler(self.period, self.loop)

    def stop(self):
        """Stop the running turtles."""
        self.running = 0
        
    def reset(self):
      """Resets the simulation"""
      self.running = 0
      self.time = 0
      self.time_text.set('Time: '+str(self.time))
      self.reset_bool = 1
      nextstates = {}
      
      for turtle in self.turtles: #reset every turtles position and heading and update it
          nextstates[turtle] = turtle.reset()
      for turtle in self.turtles:
          turtle.setstate(nextstates[turtle])
          self.update(turtle)
          
      for turtle in self.turtles: #reset the labels
          if turtle.type() == "cat":
            self.cat_rad.set('CatRadius: '+str(turtle.radius))
            self.cat_ang.set('CatAngle: '+str(turtle.angle))
          if turtle.type() == "mouse":
            self.mouse_ang.set('MouseAngle: '+str(turtle.angle))
            
    def updatecolor(self, event):
      for turtle in self.turtles: #update mouse color
        if turtle.type() == "mouse": 
          turtle.style['fill'] = self.colordict[int(self.mousecolor.curselection()[0])]
          self.update(turtle)