def divide():
    while True:
        try:
            first_num = input("First number: ")
            if first_num == 'q':
                break
            first_num = int(first_num)
        except:
            print("First input needs to be a number or q")
            continue

        secondVal = True
        while secondVal:
            try:
                second_num = input("Second number: ")
                if second_num == 'q':
                    break
                second_num = int(second_num)
            except:
                print("Second input needs to be a number or q")
                continue
            else:
                secondVal = False
        try:
            print(f"{first_num / second_num = }")
        except ZeroDivisionError:
            print("You cannont divide by zero")
            break

    # check if divide by zero
    # if inputs are numbers or non-q letters


def welcome():
    print("Give me two numbers and I'll divide them")
    print("Press 'q' to quit.")
    divide()


welcome()
