def syntax_error():
    print("Here")
    result == 5
    return result

def runtime_error1():
    word = "Dickinson"
    last = word[len(word)]
    print(f"The Last letter in {word} is {last}")

def runtime_error2():
    print("Here")
    result == 5
    return result

def semantic_error():
    print("This program will calculate the sum of two numbers.")
    num1 = input("Please provide the first number: ")
    num2 = input("Please provide the second number: ")
    total = num1 + num2
    result = f"The summation of {num1} and {num2} is {total}"
    print(result)

def doubleX(X):
    return X*2

def semantic_error2():
    val = int(input("Please give me a number: "))
    doubleX(val)
    result = f"If we double {val} we get {val}"
    print(result)

def main():
##    syntax_error()
##    runtime_error1()
##    runtime_error2()
##    semantic_error()
    semantic_error2()

# Top Level Code
main()
