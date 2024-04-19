import math
import numpy as np

def f(x):
    return x

def g(x):
    return x**2

def h(x):
    return x**0.5

my_file = open("points.csv", "w")
my_file.write("index,x,x**2,x**0.5\n")
for i in range(1, 11):
    index = i
    x = f(i)
    y = g(i)
    z = h(i)
    my_file.write(f"{index},{x},{y},{z}\n")

my_file.close()
