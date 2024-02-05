# demo using if-elif-else
# compare two inputs to see if
# one is strictly greater than,
# strictly less than, or equal to the other
print("pick two numbers between 1 and 10 ")
num1 = input("Enter first value: ")
num1 = int(num1)
num2 = int(input("Enter second value: "))

if num1 == num2:
    print(f"{num1} is equal to {num2}")
else:
    if num1 > num2:
        print(f"{num1} is greater than to {num2}")
    else:
        print(f"{num1} is less than to {num2}")

# FizzBuzz with 2, 3, and 6
x = int(input("Please pick int "))
if x % 6 == 0:
    pass
elif x % 2 == 0:
    print("Say Fizz")
elif x % 3 == 0:
    print("Say Buzz")
else:
    print(f"Say {x}")

# writing FizzBuzz with only if statements
if x % 3 == 0:
    print("Fizz", end="")
if x % 5 == 0:
    print("Buzz", end="")
if not (x % 3 == 0 or x % 5 == 0):
    print(x, end="")
print()











