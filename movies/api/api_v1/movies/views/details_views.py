from typing import Annotated

from fastapi import APIRouter, Depends
from starlette import status

from api.api_v1.movies.crud import storage
from api.api_v1.movies.dependencies import get_movie
from schemas.movie import Movie

router = APIRouter(
    prefix="/{slug}",
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Movie not found.",
            "application/json": {
                "example": {
                    "detail": "Movie 'slug' not found",
                }
            },
        },
    },
)


@router.get(
    "/",
    response_model=Movie,
)
def read_movie_details(
    movie: Annotated[
        Movie,
        Depends(get_movie),
    ],
):
    return movie


@router.delete(
    "/",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_movie(
    movie: Annotated[
        Movie,
        Depends(get_movie),
    ],
):
    storage.delete(movie=movie)
