import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "http://vignette4.wikia.nocookie.net/disney/images/4/4c/Toy-story-movie-posters-4.jpg/revision/latest?cb=20140816182710",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://i46.tinypic.com/1zly8if.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

space_odyssey = media.Movie("2001: A Space Odyssey",
                            "An imposing black structure provides a connection between the past and the future",
                            "http://t0.gstatic.com/images?q=tbn:ANd9GcQdmmLZ7lXsw1WRy7c5qN3mka2e9ANSpHIG2INi53P6OVS8KyJo",
                            "https://www.youtube.com/watch?v=lfF0vxKZRhc")

movies = [toy_story, avatar, space_odyssey]

fresh_tomatoes.open_movies_page(movies)
