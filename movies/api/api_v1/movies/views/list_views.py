from fastapi import APIRouter, status

from api.api_v1.movies.crud import storage
from schemas.movie import Movie, MovieCreate, MovieRead

router = APIRouter(
    prefix="/movies",
    tags=["movies"],
)


@router.get(
    "/",
    response_model=list[MovieRead],
)
def read_movies_list():
    return storage.get()


@router.post(
    "/",
    response_model=MovieRead,
    status_code=status.HTTP_201_CREATED,
)
def create_movie(
    movie_in: MovieCreate,
):
    return storage.create(movie_in=movie_in)
