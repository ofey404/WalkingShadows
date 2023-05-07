from functools import lru_cache

from libs import uvicornx
from pydantic import BaseSettings


class Settings(BaseSettings):
    log_level: str = "info"
    uvicorn: uvicornx.Settings = uvicornx.Settings()


@lru_cache
def get_settings() -> Settings:
    return Settings()
