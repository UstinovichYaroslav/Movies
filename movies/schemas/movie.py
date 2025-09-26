import random

from pydantic import BaseModel


class MovieBase(BaseModel):
    slug: str
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
