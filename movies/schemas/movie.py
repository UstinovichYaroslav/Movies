import random

from pydantic import BaseModel


class MovieBase(BaseModel):
    id: int
    name: str
    description: str
    rating: float


class MovieCreate(MovieBase):
    """
    Модель создания фильма
    """

    ignore_extra_fields = id


class Movie(MovieBase):
    """
    Модель фильма
    """
