from contextlib import asynccontextmanager

from fastapi import APIRouter, FastAPI
from libs import mongox
from services.world.internal import models
from services.world.settings import get_settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    s = get_settings()
    await mongox.init(
        settings=s.mongo,
        document_models=[
            models.World,
            models.Character,
        ],
    )
    yield


def create_app(*routers: APIRouter) -> FastAPI:
    app = FastAPI(lifespan=lifespan)

    for r in routers:
        app.include_router(r)
    return app
