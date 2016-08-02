import media
import fresh_tomatoes

# Create an instance of Movie that describes the movie Toy Story
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "http://vignette4.wikia.nocookie.net/disney/images/4/4c/Toy-story-movie-posters-4.jpg/revision/latest?cb=20140816182710",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
                        
# Create an instance of Movie that describes the movie Avatar
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://i46.tinypic.com/1zly8if.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
                     
# Create an instance of Movie that describes the movie 2001: A Space Odyssey
space_odyssey = media.Movie("2001: A Space Odyssey",
                            "An imposing black structure provides a connection between the past and the future",
                            "http://t0.gstatic.com/images?q=tbn:ANd9GcQdmmLZ7lXsw1WRy7c5qN3mka2e9ANSpHIG2INi53P6OVS8KyJo",
                            "https://www.youtube.com/watch?v=lfF0vxKZRhc")
                            
# Array of Movie instances to be passed to the open_movies_page function that will pass them into an HTML document to be displayed as a web page
movies = [toy_story, avatar, space_odyssey]

fresh_tomatoes.open_movies_page(movies)
