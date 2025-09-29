from typing import Annotated

from annotated_types import Len, MaxLen
from pydantic import BaseModel

DescriptionString = Annotated[
    str,
    MaxLen(200),
]


class MovieBase(BaseModel):
    name: str
    description: DescriptionString = ""
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

    description: DescriptionString


class MoviePartialUpdate(MovieBase):
    name: str | None = None
    description: DescriptionString | None = None
    rating: float | None = None


class Movie(MovieBase):
    """
    Модель фильма
    """

    slug: str
