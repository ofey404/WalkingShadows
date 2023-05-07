from functools import lru_cache

from libs import mongox, uvicornx
from pydantic import BaseSettings


class Settings(BaseSettings):
    uvicorn: uvicornx.Settings = uvicornx.Settings()
    mongo: mongox.Settings = mongox.Settings()


@lru_cache
def get_settings() -> Settings:
    return Settings()
