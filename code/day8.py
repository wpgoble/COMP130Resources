import turtle

##joe = turtle.Turtle()
##joe.forward(100)
##joe.left(90)
##joe.forward(100)
##joe.left(90)
##joe.forward(100)
##joe.left(90)
##joe.forward(100)
##joe.left(90)
##for side in range(4):
##    joe.forward(100)
##    joe.left(90)

for banana in range(5):
    print(f"Currently on iteration: {banana+1}")

for apple in range(10, 20):
    print(apple)
print("="*10)
for pineapple in range(11, 20, 2):
    print(pineapple)
print("="*10)
for i in range(10, -1, -1):
    if i == 0:
        print("blast off!")
    else:
        print(i)
