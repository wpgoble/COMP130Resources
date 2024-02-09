##import turtlex
##
##josef = turtle.Turtle()
##
##for side in range(6):
##    josef.forward(100)
##    if side == 2:
##        josef.left(60)
##    elif side == 5:
##        josef.left(180)
##    else:
##        josef.left(120)
##    print(f"iteration number: {side}")

##name = input("please provide a name or word: ")
##
##for letter in name:
##    print(letter)

mostWord = ""
mostNumber = 0
for i in range(3):
    str = input("Please give me a word: ")
    target = "j"
    appearence = 0

    for letter in str:
        if letter == target:
            appearence += 1

    if appearence > mostNumber:
        mostWord = str
        mostNumber = appearence

    print(f"{target} appeared in {str} {appearence} times")
print(f"{target} appeared in {mostWord} {mostNumber} times")
