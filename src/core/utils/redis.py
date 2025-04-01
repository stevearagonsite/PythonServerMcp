import functools
import json
from typing import Any

from loguru import logger
from redis.exceptions import ResponseError

from src.app.core.redis import RedisConnection
from src.app.core import exceptions


class RedisBackend:
    DEFAULT_EXPIRATION_SECONDS = 60 * 60 * 1  # 1 hour
    conn = RedisConnection().connect()

    @classmethod
    async def get(cls, key: str):
        cached_data = await cls.conn.get(key)
        if cached_data:
            return json.loads(cached_data)

    @classmethod
    def set(cls, key: str, data: Any, expire: int | None = DEFAULT_EXPIRATION_SECONDS):
        try:
            compressed_data = json.dumps(data)
            cls.conn.set(key, compressed_data, ex=expire)
        except ResponseError as e:
            logger.exception(e)
            raise exceptions.InternalError(detail="REDIS_ERROR")

    def delete(cls, key: str):
        cls.conn.delete(key)

    @classmethod
    def cache(cls, expire: int | None = DEFAULT_EXPIRATION_SECONDS):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                key = f"{func.__name__}:{args}:{kwargs}"

                # Check if the data exists in Redis cache
                cached_data = cls.get(key)
                if cached_data is not None:
                    return cached_data

                # Execute the function
                result = func(*args, **kwargs)

                # Store the result in Redis cache
                cls.set(key, result, expire=expire)

                return result

            return wrapper

        return decorator
