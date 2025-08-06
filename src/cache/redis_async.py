# redis_client.py
import redis.asyncio as redis
from src.config.settings import get_general_settings


class RedisClientAsync:
    def __init__(self):
        self.__redis = redis.Redis(
            host=get_general_settings().redis_host,
            port=get_general_settings().redis_port,
            db=get_general_settings().redis_db,
            decode_responses=True,  # Makes values strings instead of bytes
        )

    async def ping(self):
        try:
            await self.__redis.ping()
        except Exception as e:
            print(f"Redis connection failed ❌: {e}")

    async def set(self, key: str, value: str) -> bool:
        return await self.__redis.set(key, value)

    async def get(self, key: str) -> str | None:
        return await self.__redis.get(key)

    async def close(self):
        await self.__redis.close()
