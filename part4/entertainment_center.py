import media
import fresh_tomatoes

# instances are being defined here; all storylines are from IMDB
practical_magic = media.Movie("Pratical Magic",
                        "Two witch sisters, raised by their eccentric aunts in a small town, face closed-minded prejudice and a curse which threatens to prevent them ever finding lasting love.",
                        "https://upload.wikimedia.org/wikipedia/en/6/68/Practical_magicposter.jpg",
                        "https://youtu.be/R7uixLkpjPs",
                        "1998", "103 minutes", "PG-13")

julie_julia = media.Movie("Julie & Julia",
                     "Julia Child's story of her start in the cooking profession is intertwined with blogger Julie Powell's 2002 challenge to cook all the recipes in Child's first book.",
                     "https://upload.wikimedia.org/wikipedia/en/0/00/Julie_and_julia.jpg",
                     "https://youtu.be/ozRK7VXQl-k",
                     "2009", "123 minutes", "PG-13")

addams_family = media.Movie("The Addams Family",
                     "Con artists plan to fleece an eccentric family using an accomplice who claims to be their long-lost uncle.",
                     "https://upload.wikimedia.org/wikipedia/en/0/04/The_Addams_Family.jpg",
                     "https://youtu.be/LyyJYyIexq8",
                     "1991", "99 minutes", "PG-13")

ratatouille = media.Movie("Ratatouille",
                     "A rat who can cook makes an unusual alliance with a young kitchen worker at a famous restaurant.",
                     "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                     "https://youtu.be/c3sBBRxDAqk",
                     "2007", "111 minutes", "G")

john_wick = media.Movie("John Wick",
                     "An ex-hit-man comes out of retirement to track down the gangsters that killed his dog and took everything from him.",
                     "https://upload.wikimedia.org/wikipedia/en/9/98/John_Wick_TeaserPoster.jpg",
                     "https://youtu.be/2AUmvWm5ZDQ",
                     "2014", "101 minutes", "R")

conjuring = media.Movie("The Conjuring",
                     "Paranormal investigators Ed and Lorraine Warren work to help a family terrorized by a dark presence in their farmhouse.",
                     "https://upload.wikimedia.org/wikipedia/en/1/1f/Conjuring_poster.jpg",
                     "https://youtu.be/k10ETZ41q5o",
                     "2013", "112 minutes", "R")

# define movies list
movies = [practical_magic, julie_julia, addams_family, ratatouille, john_wick, conjuring]

# generate HTML
fresh_tomatoes.open_movies_page(movies)
