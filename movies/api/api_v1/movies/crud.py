from pydantic import BaseModel

from schemas.movie import Movie, MovieCreate, MovieUpdate


class MovieStorage(BaseModel):
    slug_to_movies: dict[str, Movie] = {}

    def get(self):
        return list(self.slug_to_movies.values())

    def get_by_slug(self, slug: str):
        return self.slug_to_movies.get(slug)

    def create(self, movie_in: MovieCreate):
        movie = Movie(
            **movie_in.model_dump(),
        )
        self.slug_to_movies[movie.slug] = movie
        return movie

    def delete_by_slug(self, slug: str) -> None:
        self.slug_to_movies.pop(slug, None)

    def delete(self, movie: Movie) -> None:
        self.delete_by_slug(slug=movie.slug)

    def update(
        self,
        movie: Movie,
        movie_in: MovieUpdate,
    ) -> Movie:
        for field_name, value in movie_in:
            setattr(movie, field_name, value)
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
