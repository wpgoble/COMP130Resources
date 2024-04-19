def countdown(n):
    if n <= 0:
        print("Blast off!")
    else:
        print(n)
        countdown(n+1)

#countdown(3)

def print_n(str, n):
    for i in range(n):
        print(str)

def print_n2(str, n):
    if n <= 0:
        #pass
        return
    else:
        print(str)
        n = n - 1
        print_n(str, n)

#print_n2("LGM", 3)

def my_length(lst):
    if lst == []:
        return 0
    else:
        lst.pop()
        print(lst)
        return 1 + my_length(lst)


print(my_length([1, 2, 3]))






    
