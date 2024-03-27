################################
# Name: William Goble
# Practice Exam
################################
import turtle
import random

# Question 1
def print_sequence_of_7_nums(start, increment):
    for i in range(7):
        print(start + (i * increment))

# Question 2
def print_sequence(start, increment, length):
    for i in range(length):
        print(start + (i * increment))

# Question 3
def print_sequence_and_product(start, increment, length):
    product = 1
    for i in range(length):
        val = start + (i * increment)
        print(val)
        product = product * val
    print(f"Product is {product}")

# Question 4
def draw_corner1(t, x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.forward(size)
    t.left(90)
    t.forward(size)

# Question 5
def draw_corner2(t, x, y, size, direction):
    t.setheading(direction)
    draw_corner1(t,x, y, size)


# Question 6
def draw_scaled_corners(t, x, y, initial_size, num_corners, dir_change):
    dir = 0
    for i in range(num_corners):
        # stuff from previous question
        draw_corner2(t, x, y, initial_size, dir)

        dir += dir_change
        initial_size = initial_size / 2
        

# Question 7
def draw_colored_corners(t, x, y, initial_size, num_corners, dir_change):
    size = initial_size
    angle = 0
    for i in range(num_corners):
        color = ""
        num = random.randint(0, 2)
        if num == 0:
            color = "red"
        elif num == 1:
            color = "blue"
        else:
            color = "green"
        t.pencolor(color)
        draw_corner2(t, x, y, size, angle)
        size /= 2
        angle += dir_change
        

# Question 8
def draw_2_sets_of_corners(t, initial_size, num_corners, dir_change):
    """
    Below is the basic idea for how you would solve this. This solution
    works most of the time, but there are still instances when there is
    overlap. I'm not going to ask this intense of a question.
    """
    x1 = random.randint(-200, 200)
    y1 = random.randint(-200, 200)
    x2 = random.randint(-200, 200)
    y2 = random.randint(-200, 200)
    
    while x2 >= (x1 + dir_change) and x2 <= (x1 + initial_size + dir_change):
        x2 = random.randint(-200, 200)
    while y2 >= (y1 + dir_change) and y2 >= (y1 + initial_size + dir_change):
        y2 = random.randint(-200, 200)

    draw_colored_corners(t, x1, y1, initial_size, num_corners, dir_change)
    draw_colored_corners(t, x2, y2, initial_size, num_corners, dir_change)

    
################################
# Top Level Code
################################
#print_sequence_of_7_nums(5, 3)
#print("#" * 15)
#print_sequence(8, 11, 4)
#print("#" * 15)
#print_sequence_and_product(2, 4, 3)
bob = turtle.Turtle()
turtle.tracer(0)
#draw_corner1(bob, -250, 50, 100)
#draw_corner2(bob, -50, 50, 100, -20)
#draw_scaled_corners(bob, -50, 50, 200, 5, 10)
#draw_colored_corners(bob, -50, 50, 200, 5, 10)
draw_2_sets_of_corners(bob, 200, 6, 30)
turtle.update()
