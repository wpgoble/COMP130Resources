movies = open("movies.txt", "w")

for i in range(2):
    title = input("What is the movie title? ")
    genre = input("What is the movie genre? ")
    main_character = input("What is the main character's name? ")
    year = input("What year was it released? ")

    movies.write(f"{title},{genre},{main_character},{year}\n")

movies.close()
    
