# Importing the media class
import media
import fresh_tomatoes

# Instance for the class Media
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that comes to life",
                        "https://images-na.ssl-images-amazon.com/images"
                        "/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZW"
                        "JkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_UX182_CR0,0,182,26"
                        "8_AL_.jpg",
                        "https://www.youtube.com/watch?v=NTdKQzVFeis")

deadpool = media.Movie("Deadpool",
                       "Wade Wilson is a former Special Forces operative who"
                       " now"
                       " works as a mercenary. His world comes crashing "
                       "down when evil scientist Ajax tortures, disfigures"
                       " and transforms him into Deadpool. The rogue "
                       "experiment leaves Deadpool with accelerated"
                       " healing powers and a twisted sense of humor. "
                       "With help from mutant allies Colossus and"
                       " Negasonic Teenage Warhead, Deadpool uses his"
                       " new skills to hunt down the man who nearly"
                       " destroyed his life.", "https://upload."
                       "wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",
                       "https://www.youtube.com/watch?v=ONHBaC-pfsk")

transformer3 = media.Movie("Transformer 3",
                           "The film is set three years after the events of "
                           "Revenge of the Fallen. The Autobots continue to"
                           " work for NEST, but no longer in secret, and for "
                           "the goal of keeping peace between humans by taking"
                           " out volatile overseas political targets. But "
                           "after discovering a strange artifact during a"
                           " mission in Chernobyl, it becomes apparent to"
                           " Optimus Prime that the United States government"
                           " has been less than forthright with them.",
                           "https://upload.wikimedia.org/wikipedia/en/b"
                           "/bf/Transformers_dark_of_the_moon_ver5.jpg",
                           "https://www.youtube.com/watch?v=Nj0HkNrPK5k")


avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar"
                     "-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

jumanji = media.Movie("Jumanji",
                      "Four teenagers are sucked into a magical video game,"
                      " and the only way they can escape is to work together"
                      " to finish the game.",
                      "https://upload.wikimedia.org/wikipedia/en/d/dc/"
                      "Jumanji_Welcome_to_the_Jungle.png",
                      "https://www.youtube.com/watch?v=2QKg5SZ_35I")

blackPanther = media.Movie("Black Panther",
                           "T'Challa, the King of Wakanda, rises to the "
                           "throne in the isolated, technologically advanced"
                           " African nation, but his claim is challenged by"
                           " a vengeful outsider who was a childhood victim",
                           "https://upload.wikimedia.org/wikipedia/en/0/0c/"
                           "Black_Panther_film_poster.jpg",
                           "https://www.youtube.com/watch?v=xjDjIWPwcPU")

# The movies array contains the different instantiated objects
# of the class Media
movies = [toy_story, avatar, deadpool, transformer3, jumanji, blackPanther]

# Call the open_movies_page instance method passing the movies array argument
# to open the movies webpage
fresh_tomatoes.open_movies_page(movies)

