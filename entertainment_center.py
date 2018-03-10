import media
import fresh_tomatoes
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys which come to life",
    "https://i.imgur.com/XyxAQqc.jpg",
    "https://www.youtube.com/watch?v=QW0sjQFpXTU"
)

avatar = media.Movie(
    "Avatar",
    "Imaginary planet",
    "https://cdn.traileraddict.com/content/20th-century-fox/avatar-6.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
)


print toy_story.storyline
#toy_story.show_trailer()

#fresh_tomatoes.open_movies_page([avatar,toy_story])

print(media.Movie.VALID_RATINGS)

print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)