# state vs stack diagram
def my_add(x, y):
    total = x + y
    return total

def print_name(n):
    print(n)

a = 15
b = 12.5
c = my_add(a, b)
name = "William"
name2 = print_name(name)
print(name2)

# adding elements to a dictionary
philly_sports = {}
philly_sports["baseball"] = "Phillies"
philly_sports["football"] = ["Eagles",
                             "Union"]
# while loop construction
ctr = 0
while ctr <= 3:
    ctr += 1

# iterating over a list
movies = ["Cars", "Cars2", "Cars 3", "Rango"]
##for movie in movies:
##    print(movie)

##for i in range(len(movies)):
##    print(movies[i])
##    if len(movies[i]) < 5:
##        print("Short film")
##i = 0
##while i <= len(movies):
##    i += 1
##    print(movies[i])
##    if len(movies[i]) < 5:
##        print("Short film")
def foo():
    i = 0
    while i < len(movies):
        print(movies[i])
        if len(movies[i]) < 5:
            print("Short film")
        i += 1

def pet_name(dog):
    print(f"My dog's name is {dog}")

dog = "Bruce"
dog2 = "gracie"
pet_name(dog2)

weekday = ["Monday", "Tuesday", "Wedsnesday", "Thursday", "Friday"]
today = "Friday"
if today in weekday:
    pass
















        
















