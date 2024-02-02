# Prof. Goble
# Day 6 -- importing modules and if-statements
#####################################################
# importing both the random and graphics modules
# remember, the graphics.py file must be the same 
# folder as this script. 
import graphics
import random

# First we need to create our window, this is where 
# we will draw our shapes. 
window = graphics.GraphWin("Shapes", 250, 250)
window.setBackground("light blue")

# Now we can create our circle. The circle requires 
# a center point so we know where it will be drawn, 
# and a radius. To create a point we need to use the 
# Point class from the graphics module 
center = graphics.Point(125, 125)
shape1 = graphics.Circle(center, 12)
# here we generate a random number and use 
# if-elif-else statements to determine which 
# color we want to use 
num = random.randint(1, 50)
if num % 3 == 0:
    color = "blue"
    # we can nest our if statements within 
    # other if statements in order to check to 
    # see if other conditions are also true. 
    if num < 10:
        print("here")
elif num % 3 == 1 and num > 10:
    color = "green"
else:
    color = "red"

# once we have determine what color we want, we 
# can set the fill color and then draw the shape 
# to our desired window. 
shape1.setFill(color)
shape1.draw(window)

# if we want the window to stay open after it draws 
# our shape, then we should call the getMouse function 
# from the window so the program will wait until 
# someone clicks on the canvas we made. 
window.getMouse()
# after someone has clicked on the canvas, then we 
# can close our window. 
window.close() 
