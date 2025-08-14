import asyncio

from sqlalchemy import select
from src.db.database import async_session_maker
from src.cache.redis import RedisClient
from src.cache.redis_async import RedisClientAsync
from src.models.request import Request


class RequestController:

    def __init__(self):
        self.__cache: RedisClient = RedisClient()
        self.__cache_async: RedisClientAsync = RedisClientAsync()

    async def get_requests_async(self) -> list[Request] | None:
        async with async_session_maker() as session:  # <- preferred async session
            try:
                stmt = (
                    select(Request)
                )
                result = await session.execute(stmt)
                return result.scalars().all()

            except Exception as e:
                print(f"Exception occurred: {e}")
                return []
