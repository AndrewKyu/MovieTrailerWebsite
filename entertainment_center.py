import media
import movies_page

toy_story = media.Movie("Toy Story", 
	"A story of a boy and his toys that come to life",
	"https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
	 "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
	"A marine on an alien planet",
	"https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
	"https://www.youtube.com/watch?v=5PSNL1qE6VY")

pokemon_the_first_movie = media.Movie("Pokemon the First Movie",
	"A story about how Ash Ketchum meets Mewtwo",
	"https://vignette.wikia.nocookie.net/pokemon/images/5/57/MS001.png/revision/latest?cb=20110215105244",
	"https://www.youtube.com/watch?v=sSLuNZFa_3k")

#print(avatar.storyline)
#pokemon_the_first_movie.show_trailer()

train_to_busan = media.Movie("Train to Busan",
	"A father tries to send his child to Busan to visit the mother, however due to unfortunate circumstances, the train was full of zombies",
	"https://upload.wikimedia.org/wikipedia/en/9/95/Train_to_Busan.jpg",
	"https://www.youtube.com/watch?v=pyWuHv2-Abk")
movies = [toy_story, avatar, pokemon_the_first_movie, train_to_busan]
#movies_page.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)