# Code generated by sqlc. DO NOT EDIT.
# versions:
#   sqlc v1.23.0
# source: query.sql
from typing import AsyncIterator, Iterator, Optional

import sqlalchemy
import sqlalchemy.ext.asyncio

from . import models


CREATE_AUTHOR = """-- name: create_author \\:one
insert into authors (
	name, bio, age
) values (
	:p1, :p2, :p3
)
returning id, name, age, bio, is_active
"""


DELETE_AUTHOR = """-- name: delete_author \\:exec
delete from authors
where id = :p1
"""


GET_AUTHOR = """-- name: get_author \\:one
select id, name, age, bio, is_active from authors
where id = :p1 LIMIT 1
"""


LIST_AUTHORS = """-- name: list_authors \\:many
select id, name, age, bio, is_active from authors
order by name
"""


LOCK_AUTHOR = """-- name: lock_author \\:one
select id, name, age, bio, is_active from authors
where id = :p1 LIMIT 1 FOR UPDATE NOWAIT
"""


UPDATE_AUTHOR = """-- name: update_author \\:one
update authors
	set name = :p2,
	bio = :p3,
	age = :p4
where id = :p1
returning id, name, age, bio, is_active
"""


class Querier:
    def __init__(self, conn: sqlalchemy.engine.Connection):
        self._conn = conn

    def create_author(self, *, name: str, bio: Optional[str], age: int) -> Optional[models.Author]:
        row = self._conn.execute(sqlalchemy.text(CREATE_AUTHOR), {"p1": name, "p2": bio, "p3": age}).first()
        if row is None:
            return None
        return models.Author(
            id=row[0],
            name=row[1],
            age=row[2],
            bio=row[3],
            is_active=row[4],
        )

    def delete_author(self, *, id: int) -> None:
        self._conn.execute(sqlalchemy.text(DELETE_AUTHOR), {"p1": id})

    def get_author(self, *, id: int) -> Optional[models.Author]:
        row = self._conn.execute(sqlalchemy.text(GET_AUTHOR), {"p1": id}).first()
        if row is None:
            return None
        return models.Author(
            id=row[0],
            name=row[1],
            age=row[2],
            bio=row[3],
            is_active=row[4],
        )

    def list_authors(self) -> Iterator[models.Author]:
        result = self._conn.execute(sqlalchemy.text(LIST_AUTHORS))
        for row in result:
            yield models.Author(
                id=row[0],
                name=row[1],
                age=row[2],
                bio=row[3],
                is_active=row[4],
            )

    def lock_author(self, *, id: int) -> Optional[models.Author]:
        row = self._conn.execute(sqlalchemy.text(LOCK_AUTHOR), {"p1": id}).first()
        if row is None:
            return None
        return models.Author(
            id=row[0],
            name=row[1],
            age=row[2],
            bio=row[3],
            is_active=row[4],
        )

    def update_author(self, *, id: int, name: str, bio: Optional[str], age: int) -> Optional[models.Author]:
        row = self._conn.execute(sqlalchemy.text(UPDATE_AUTHOR), {
            "p1": id,
            "p2": name,
            "p3": bio,
            "p4": age,
        }).first()
        if row is None:
            return None
        return models.Author(
            id=row[0],
            name=row[1],
            age=row[2],
            bio=row[3],
            is_active=row[4],
        )


class AsyncQuerier:
    def __init__(self, conn: sqlalchemy.ext.asyncio.AsyncConnection):
        self._conn = conn

    async def create_author(self, *, name: str, bio: Optional[str], age: int) -> Optional[models.Author]:
        row = (await self._conn.execute(sqlalchemy.text(CREATE_AUTHOR), {"p1": name, "p2": bio, "p3": age})).first()
        if row is None:
            return None
        return models.Author(
            id=row[0],
            name=row[1],
            age=row[2],
            bio=row[3],
            is_active=row[4],
        )

    async def delete_author(self, *, id: int) -> None:
        await self._conn.execute(sqlalchemy.text(DELETE_AUTHOR), {"p1": id})

    async def get_author(self, *, id: int) -> Optional[models.Author]:
        row = (await self._conn.execute(sqlalchemy.text(GET_AUTHOR), {"p1": id})).first()
        if row is None:
            return None
        return models.Author(
            id=row[0],
            name=row[1],
            age=row[2],
            bio=row[3],
            is_active=row[4],
        )

    async def list_authors(self) -> AsyncIterator[models.Author]:
        result = await self._conn.stream(sqlalchemy.text(LIST_AUTHORS))
        async for row in result:
            yield models.Author(
                id=row[0],
                name=row[1],
                age=row[2],
                bio=row[3],
                is_active=row[4],
            )

    async def lock_author(self, *, id: int) -> Optional[models.Author]:
        row = (await self._conn.execute(sqlalchemy.text(LOCK_AUTHOR), {"p1": id})).first()
        if row is None:
            return None
        return models.Author(
            id=row[0],
            name=row[1],
            age=row[2],
            bio=row[3],
            is_active=row[4],
        )

    async def update_author(self, *, id: int, name: str, bio: Optional[str], age: int) -> Optional[models.Author]:
        row = (await self._conn.execute(sqlalchemy.text(UPDATE_AUTHOR), {
            "p1": id,
            "p2": name,
            "p3": bio,
            "p4": age,
        })).first()
        if row is None:
            return None
        return models.Author(
            id=row[0],
            name=row[1],
            age=row[2],
            bio=row[3],
            is_active=row[4],
        )
