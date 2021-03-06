import webbrowser

class Movie():
    """This is a documentation of Movie class"""
    VALID_RATINGS=["G","PG","PG-13","R"]
    def __init__(self,movie_title,story_line,poster_url,trailer_url):
        self.title = movie_title
        self.storyline = story_line
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)