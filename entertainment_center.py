import fresh_tomatoes
import media

# Lucy
lucy = media.Movie("Lucy",
                    "The woman with the modified DNA to do the seeming impossible",
                    "https://upload.wikimedia.org/wikipedia/en/1/14/Lucy_(2014_film)_poster.jpg",
                    "https://www.youtube.com/watch?v=viJsYmYOZgY")

# Lord of the ring
lord_of_the_ring = media.Movie("Lord of the ring",
                     "A contest for the legendary ring",
                     "http://www.darkcarnival.co.za/wp-content/uploads/2015/11/lord-of-the-rings-two-towers-11.jpg",
                     "https://www.youtube.com/watch?v=-JNVtorI3vw")

# Star Trek
star_trek = media.Movie("Star Trek",
                             "About Star Trek",
                             "http://www.monstersandcritics.com/wp-content/uploads/2015/11/star_trek_the_original_series_by_1darthvader-d6ecswd.jpg",
                             "https://www.youtube.com/watch?v=SL37UPUcEd0")

# Transcendence
transcendence = media.Movie("Transcendence",
                          "About the professor that transcended life!",
                          "http://i.jeded.com/i/transcendence.29748.jpg",
                          "https://www.youtube.com/watch?v=QheoYw1BKJ4")

# Men in black
men_in_black = media.Movie("Men in black",
                                "About men in black",
                                "http://www.sonypictures.com/movies/meninblack3/assets/images/onesheet.jpg",
                                "https://www.youtube.com/watch?v=aoyV49FfjOU")

# Mission impossible
mission_impossible = media.Movie("Mission impossible",
                          "About the impossible mission made possible",
                          "https://i.ytimg.com/vi/bsEYtBGS6ho/maxresdefault.jpg",
                          "https://www.youtube.com/watch?v=qbg99ykA2bk")

# Build website
movies = [lucy, lord_of_the_ring, star_trek,
          transcendence, men_in_black, mission_impossible]

fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.__module__)
