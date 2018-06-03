import webbrowser

class Video():
	def __init__(self, title, duration):
		self.title = title
		self.duration = duration

class Movie():
	"""This class allows us to store movie information that are related """

	#all instances can share this rating to see if it's a valid rating
	VALID_RATINGS = ["G", "PG", "PG-13", "R"] #class variable

	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

class TvShow(Movie):
	#title, season, episode, tv_station, def get_local_listing()
