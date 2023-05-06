import logging

import uvicorn
from fastapi import FastAPI
from services.character.routers import tick
from services.character.settings import get_settings

app = FastAPI()

app.include_router(tick.router)

if __name__ == "__main__":
    s = get_settings()
    uvicorn.run(
        app,
        host=s.host,
        port=s.port,
        reload=s.reload,
    )
