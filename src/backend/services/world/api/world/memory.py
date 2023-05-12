from fastapi import APIRouter, Depends
from loguru import logger
from pydantic import BaseModel
from services.world.settings import Settings, get_settings

router = APIRouter()


class MemoryGetRequest(BaseModel):
    id: str


class MemoryGetResponse(BaseModel):
    id: str
    ts: int
    content: str


@router.post(
    "/api/world/{world}/memory/get",
    response_model=MemoryGetResponse,
)
async def handle_memory_get(
    world: str,
    body: MemoryGetRequest,
) -> dict:
    logger.info(f"world: {world}")

    return {"id": body.id, "ts": 0, "content": "test content"}


class MemoryGenerateRequest(BaseModel):
    ...


class MemoryGenerateResponse(BaseModel):
    ...


@router.post(
    "/api/world/{world}/memory/next",
    response_model=MemoryGenerateResponse,
)
async def handle_memory_generate(
    world: str,
    body: MemoryGenerateRequest,
    settings: Settings = Depends(get_settings),
) -> dict:
    logger.info(f"world: {world}")
