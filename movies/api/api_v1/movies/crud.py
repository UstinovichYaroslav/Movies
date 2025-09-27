from pydantic import BaseModel

from schemas.movie import Movie, MovieCreate



class MovieStorage(BaseModel):
    slug_to_movies: dict[str, Movie] = {}

    def get(self):
        return list(self.slug_to_movies.values())

    def get_by_slug(self, slug: str):
        return self.slug_to_movies.get(slug)

    def create(self, movie: MovieCreate):
        movie = Movie(**movie.model_dump())
        self.slug_to_movies[movie.slug] = movie
        return movie

storage = MovieStorage()

storage.create(
    MovieCreate(
        slug="1",
        name="бегущий по лезвию",
        description="американский художественный фильм",
        rating=9.9,
    ),
)
storage.create(
    MovieCreate(
        slug="2",
        name="гарри поттер",
        description="серия фильмов",
        rating=10,
    ),
)

