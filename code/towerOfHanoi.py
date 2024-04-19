def TowerOfHanoi(n, src, dest, aux):
    if n == 1:
        print("Move disk 1 from source", src, "to dest", dest)
    else:
        TowerOfHanoi(n-1, src, aux, dest)
        print("Move disk", n, "from src", src, "to dest", dest)
        TowerOfHanoi(n-1, aux, dest, src)

def my_power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * my_power(base, exp-1)

def nested_sum(my_list):
    total = 0
    for number in my_list:
        if type(number) == type([]):
            total += nest_sum(number)
        else:
            total += number
    return total

##TowerOfHanoi(4, "A", "C", "B")
print(my_power(2, 3))
