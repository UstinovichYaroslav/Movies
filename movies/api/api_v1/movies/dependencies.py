from fastapi import HTTPException, status

from .crud import MOVIES
from schemas.movie import Movie


def get_movie(
    movie_slug: int,
) -> Movie:
    movie: Movie | None = next(
        (movie for movie in MOVIES if movie.slug == movie_slug),
        None,
    )
    if movie:
        return movie

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Movie {movie_slug!r} not found",
    )
