# dictionary for the key, value
# pair Movie, Director
movies_weve_seen = {
    "Cars":"John Lasseter"
    }

movies_weve_seen["Rango"] = "Gore Verbinski"

movie_directors = {
    "Gore Verbinski": [
        "Rango", "Pirates 1","Pirates 2","Pirates 3" 
        ]
    }

##print(movie_directors)
director_name = "John Lasseter"
if director_name in movie_directors:
    movie_directors[director_name].append("something")
else:
    movie_directors[director_name] = ["something"]
##print(movie_directors)


def create_dictionary():
    course = input("what is your course? ")
    dickinson = {}
    
    while course != "exit":
        key = course[:4]
        value = course
        if key in dickinson:
            dickinson[key].append(value)
        else:
            dickinson[key] = [value]
        print(dickinson)
        course = input("what is your course? ")



create_dictionary()


















    
