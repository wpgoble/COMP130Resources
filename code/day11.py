##def foo():
##    print("I'm a lumberjack and I'm okay")
##    print("I sleep all night and I work all day")
##
##def double(value):
####    a = value * 2
####    return a
##    return value * 2
##
##foo()
##temp = double(5)
##print(temp)
##temp = double(12)
##print(temp)

def count_x(sample):
    count = 0
    for letter in sample:
        if letter == "x":
            count += 1
    return count

print(count_x("oxygen"))
print(count_x("axbxcxx"))
print(count_x("hello"))
