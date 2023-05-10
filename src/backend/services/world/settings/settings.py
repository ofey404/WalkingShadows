from functools import cache

from libs import mongox, openaix, uvicornx
from pydantic import BaseSettings


class Settings(BaseSettings):
    openai: openaix.Settings = openaix.Settings()
    uvicorn: uvicornx.Settings = uvicornx.Settings()
    mongo: mongox.Settings = mongox.Settings()


@cache
def get_settings() -> Settings:
    return Settings()
