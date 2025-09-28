import random
from typing import Annotated

from fastapi import APIRouter, Depends, status

from .crud import storage
from .dependencies import get_movie
from schemas.movie import Movie, MovieCreate

router = APIRouter(
    prefix="/movies",
    tags=["Movies"],
)


@router.get(
    "/movies",
    response_model=list[Movie],
)
def read_movies_list():
    return storage.get()


@router.get(
    "/movies/{movie_slug}",
    response_model=Movie,
)
def read_movie_details(
    movie: Annotated[
        Movie,
        Depends(get_movie),
    ],
):
    return movie


@router.post(
    "/",
    response_model=Movie,
    status_code=status.HTTP_201_CREATED,
)
def create_movie(
    movie_create: MovieCreate,
):

    return storage.create(movie_create)


@router.delete(
    "/",
    status_code=status.HTTP_204_NO_CONTENT,
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
def delete_movie(
    movie: Annotated[
        Movie,
        Depends(get_movie),
    ],
):
    storage.delete(movie=movie)
