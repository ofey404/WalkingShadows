from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    host = "0.0.0.0"
    port = 8000
    reload = False


@lru_cache
def get_settings() -> Settings:
    return Settings()
