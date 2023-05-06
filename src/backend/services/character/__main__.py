import logging

import uvicorn
from fastapi import FastAPI
from libs import uvicornx
from services.character.routers import tick
from services.character.settings import get_settings

logger = logging.getLogger(__name__)
app = FastAPI()

app.include_router(tick.router)

if __name__ == "__main__":
    uvicornx.run(
        app,
        uvicornx.get_settings(),
    )
