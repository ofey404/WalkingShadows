from fastapi import APIRouter, FastAPI


def create_app(*router: APIRouter) -> FastAPI:
    app = FastAPI()

    app.include_router(*router)
    return app
