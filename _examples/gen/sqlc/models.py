# Code generated by sqlc. DO NOT EDIT.
# versions:
#   sqlc v1.23.0
import pydantic
from typing import Optional


class Author(pydantic.BaseModel):
    id: int
    name: str
    age: int
    bio: Optional[str]
    is_active: bool
