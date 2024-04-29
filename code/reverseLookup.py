def reverse_lookup(dictionary, target):
    for key in dictionary.keys():
        if dictionary[key] == target:
            return key
    return False

movie = {
    "title":"The Bee Movie",
    "director":["Simon Smith",
                "Steve Hickner"],
    "genre": "drama",
    "release year": 2007
    }

movie2 = {
    "title":"Cars",
    "director":["John Lasseter",
                "Brian Fee"],
    "genre": "rom-com",
    "release year": 2006
    }

target = 2007
print(reverse_lookup(movie2, target))

