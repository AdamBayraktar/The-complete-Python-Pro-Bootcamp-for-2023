


class AddMovieToDb:
    def __init__(self, movie):
        self.title = movie["original_title"]
        self.year = movie["release_date"]
        self.description = movie["overview"]
        self.img_url = movie["poster_path"]
        self.movie_id = movie["id"]

    def create(self, Movies):
        the_movie = Movies(
            title = self.title,
            year = self.year,
            description = self.description,
            img_url = 'https://image.tmdb.org/t/p/w500' + self.img_url,
            movie_id = self.movie_id
        )
        return the_movie