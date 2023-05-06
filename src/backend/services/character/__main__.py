from fastapi import FastAPI
from libs import uvicornx
from services.character.routers import tick
from services.character.settings import get_settings


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(tick.router)
    return app


if __name__ == "__main__":
    s = get_settings()
    uvicornx.run(
        create_app(),
        s.uvicorn,
    )
