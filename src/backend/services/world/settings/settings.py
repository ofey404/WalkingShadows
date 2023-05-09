from functools import cache

from libs import mongox, uvicornx
from pydantic import BaseSettings


class Settings(BaseSettings):
    uvicorn: uvicornx.Settings = uvicornx.Settings()
    mongo: mongox.Settings = mongox.Settings()


@cache
def get_settings() -> Settings:
    return Settings()
