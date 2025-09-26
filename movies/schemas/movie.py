import random

from pydantic import BaseModel


class MovieBase(BaseModel):
    name: str
    description: str
    rating: float


class MovieCreate(MovieBase):
    """
    Модель создания фильма
    """


class Movie(MovieBase):
    """
    Модель фильма
    """
    id: int
