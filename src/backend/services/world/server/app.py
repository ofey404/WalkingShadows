from fastapi import APIRouter, FastAPI


def create_app(*routers: APIRouter) -> FastAPI:
    app = FastAPI()

    for r in routers:
        app.include_router(r)
    return app
