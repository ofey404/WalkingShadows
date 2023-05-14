from contextlib import asynccontextmanager

from fastapi import APIRouter, Depends, FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from libs import mongox
from loguru import logger
from services.world.internal import models
from services.world.settings import Settings, get_settings


def create_app(
    *routers: APIRouter,
    settings_override: Settings = None,
) -> FastAPI:
    @asynccontextmanager
    async def lifespan(
        app: FastAPI,
    ):
        # startup
        s = settings_override or get_settings()
        logger.info(f"connecting to db, with setting {s.json()}")
        client = await mongox.init(
            settings=s.mongo,
            document_models=[
                models.World,
                models.Character,
            ],
        )
        yield

        # shutdown
        logger.info(f"disconnect from db, with setting {s.json()}")
        client.close()

    app = FastAPI(
        lifespan=lifespan,
        middleware=[
            Middleware(
                CORSMiddleware,
                allow_origins=["*"],
                allow_methods=["*"],
                allow_headers=["*"],
            )
        ],
    )

    for r in routers:
        app.include_router(r)

    return app
