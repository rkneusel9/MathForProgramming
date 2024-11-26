#
#  file: treasure.py
#
#  Vectors as geometric objects and in R^2
#
#  RTK, 13-Oct-2023
#  Last update:  15-Oct-2023
#
################################################################

import turtle
import numpy as np
from PIL import ImageGrab
from math import atan

# screen
screen = turtle.Screen()
screen.setup(width=500, height=500)
screen.title("Treasure Island")
screen.bgpic('island.gif')

# turtle
t = turtle.Turtle()
t.speed(1)

# X marks the spot
t.ht()
t.penup()
x,y,w = 62,139,10
t.width(5)
t.pencolor('red')
t.goto(x-w,y); t.pendown()
t.goto(x+w,y); t.penup()
t.goto(x,y+w); t.pendown()
t.goto(x,y-w); t.penup()
t.pencolor('black')
t.width(2)

# move to the start position
t.goto(-200,0)
t.pendown()
t.st()

# follow the map
t.fd(200)
t.stamp()
t.rt(45)
t.fd(130)
t.stamp()
t.lt(60)
t.fd(75)
t.stamp()
t.lt(80)
t.fd(120)
t.stamp()
t.lt(40)
t.fd(130)
t.stamp()
x,y = t.pos()
v = np.array([200+x,y])

# net sum vector
t.penup()
t.ht()
t.goto(-200,0)
angle = atan((139-0)/(62--200))*(180/3.14159265)
t.setheading(angle)
t.st()
t.pendown()
t.width(4)
t.goto(62,139)
t.stamp()

# save the drawing
canvas = screen.getcanvas()
tk_window = canvas.winfo_toplevel()
x1 = tk_window.winfo_rootx()
y1 = tk_window.winfo_rooty()
x2 = x1 + tk_window.winfo_width()
y2 = y1 + tk_window.winfo_height()
ImageGrab.grab(bbox=(x1,y1,x2,y2)).save("treasure.png")

# treasure map vectors in R^2
def pp(v):
    return "(%8.4f, %8.4f)" % (v[0],v[1])

def polar2rect(r, angle):
    """Convert polar vector to Cartesian"""
    theta = (np.pi/180)*angle
    return np.array([r*np.cos(theta), r*np.sin(theta)])

#  treasure map vectors (mag, angle --> x,y):
x0 = polar2rect(200,  0)
x1 = polar2rect(130,-45)
x2 = polar2rect( 75, 15)
x3 = polar2rect(120, 95)
x4 = polar2rect(130,135)

print("Treasure map vectors and sum:")
print("  ", pp(x0))
print("  ", pp(x1))
print("  ", pp(x2))
print("  ", pp(x3))
print("+ ", pp(x4))
print("-----------------------")
print("  ", pp(x0+x1+x2+x3+x4), "<< vector sum")
print("  ", pp(v), "<< turtle position")
print()

# event loop
screen.mainloop()

