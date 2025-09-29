from typing import Annotated

from annotated_types import Len, MaxLen
from pydantic import BaseModel


class MovieBase(BaseModel):
    name: str
    description: Annotated[
        str,
        MaxLen(200),
    ] = ""
    rating: float


class MovieCreate(MovieBase):
    """
    Модель создания фильма
    """

    slug: Annotated[
        str,
        Len(min_length=3, max_length=10),
    ]


class MovieUpdate(MovieBase):
    """
    Модель для обновления информации о фильме
    """

    description: Annotated[
        str,
        MaxLen(200),
    ]


class Movie(MovieBase):
    """
    Модель фильма
    """

    slug: str
