# Feb 16, 2024
# Create a function with the signature count_x(str)
# which takes in a string str and returns the number
# of times the letter 'x' appears in that string
def count_x(str):
    target = "x"        # our target letter
    appearence = 0      # how many times we've seen x

    for letter in str:
        if letter == target:
            appearence = appearence + 1
    return appearence

amount = count_x("akjsdhflkazx")
print(f"the letter x appears {amount} times")
