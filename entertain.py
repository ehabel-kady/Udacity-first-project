# Importing the files that contains the classes needed
import Media
import fresh_tomatoes

# Making instances of the class for each movie
Batman = Media.Movie(
    "Batman Begins",
    "A story of batman trying to stop the evil plans of Ras'a'ghol",
    "https://www.youtube.com/watch?v=neY2xVmOfUM&t=3s",
    "https://upload.wikimedia.org/wikipedia/en/thumb/a/af/"
    "Batman_Begins_Poster.jpg/220px-Batman_Begins_Poster.jpg"
)

darkknight = Media.Movie(
    "The Dark Knight",
    "A story of batman trying to stop the evil plans of the joker",
    "https://www.youtube.com/watch?v=EXeTwQWrcwY",
    "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg"
)

darkknightrises = Media.Movie(
    "The Dark Knight Rises",
    "A story of batman trying to save Gotham city from Bane's danger",
    "https://www.youtube.com/watch?v=g8evyE9TuYk",
    "https://upload.wikimedia.org/wikipedia/en/8/83/Dark_knight_rises_"
    "poster.jpg"
)

prestige = Media.Movie(
    "The Prestige",
    "Two magicians battle with each other using their ability to do tricks",
    "https://www.youtube.com/watch?v=ijXruSzfGEc",
    "https://upload.wikimedia.org/wikipedia/en/thumb/d/d2/Prestige_poster"
    ".jpg/220px-Prestige_poster.jpg"
)

LionKing = Media.Movie(
    "The Lion king",
    "A story of Simba trying to get his pride back from his uncle after the "
    "death of his father",
    "https://www.youtube.com/watch?v=4sj1MT05lAA",
    "https://upload.wikimedia.org/wikipedia/en/thumb/3/3d/The_Lion_King_"
    "poster.jpg/220px-The_Lion_King_poster.jpg"
)

toy_story = Media.Movie(
    "ToyStory",
    "Some toys that came to life",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc&t=6s",
    "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/"
    "Toy_Story.jpg/220px-Toy_Story.jpg"
)

# Adding all the movies to a list
movies = [Batman, darkknight, darkknightrises, prestige, LionKing, toy_story]

# Calling the function in the fresh_tomatoes file that creates the webpage
# of the movies
fresh_tomatoes.open_movies_page(movies)
