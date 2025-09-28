from fastapi import HTTPException, status

from .crud import storage
from schemas.movie import Movie


def get_movie(
    slug: str,
) -> Movie:
    movie: Movie | None = storage.get_by_slug(slug)

    if movie:
        return movie

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Movie {slug!r} not found",
    )
