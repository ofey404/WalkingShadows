import uvicorn
from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 8000
    log_level: str = "info"

    class Config:
        env_prefix = "UVICORN_"


def run(app, s: Settings):
    """run() wraps uvicorn.run() with handy configurations"""
    uvicorn.run(
        app,
        host=s.host,
        port=s.port,
        log_level=s.log_level,
    )
