from graphics import *
import random

odds = random.randint(1, 10)
if odds % 2 == 0:
    color = "blue"
else:
    color = "red"
    
my_window = GraphWin("My Circle", 100, 100)
my_window.setBackground("white")
cir = Circle(Point(50, 50), 10)
cir.draw(my_window)
cir.setFill(color)
my_window.getMouse()
my_window.close()
