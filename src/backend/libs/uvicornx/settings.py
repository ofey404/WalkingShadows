import uvicorn
from pydantic import BaseSettings


class Settings(BaseSettings):
    host = "0.0.0.0"
    port = 8000
    reload = False
    log_level = "info"

    class Config:
        env_prefix = "UVICORN_"


def run(app, s: Settings):
    """run() wraps uvicorn.run() with handy configurations"""
    uvicorn.run(
        app,
        host=s.host,
        port=s.port,
        reload=s.reload,
        log_level=s.log_level,
    )
