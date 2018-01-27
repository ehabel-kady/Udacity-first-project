import webbrowser


class Movie():
    """ A Class the store data related to movies"""
    def __init__(self, name, storyline, trailer, poster):
        """ the constructor method of the class Movie"""
        # Assigning the values of the instances to the class variables
        self.title = name
        self.mov_story = storyline
        self.trailer_youtube_url = trailer
        self.poster_image_url = poster

    def show_trailer(self):
        """
        A class method that plays the movie trailers in a seperate
        webpage
        """
        webbrowser.open(self.trailer_youtube_url)
