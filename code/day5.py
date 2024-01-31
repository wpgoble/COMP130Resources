# Prof. Goble
# Examples of conditional statements
import random

answer = random.randint(1, 10)
value = int(input("Guess a number between 1 and 10 "))
#value = int(value)

if answer == value:
    print("You've won!")
else:
    print(f"You lost.. The answer is {answer}")
