from typing import Callable

from fastapi import APIRouter, Depends
from langchain import schema
from loguru import logger
from pydantic import BaseModel
from services.world.internal.llm import generate_world_memory
from services.world.internal.models.world import World, get_world

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
    generated_memory: str


@router.post(
    "/api/world/{world_name}/memory/generate",
    response_model=MemoryGenerateResponse,
)
async def handle_memory_generate(
    world_name: str,
    body: MemoryGenerateRequest,
    world: World = Depends(get_world),
    generated_memory: str = Depends(generate_world_memory),
) -> dict:
    """generate new memory entry"""

    world.add_memory(generated_memory)
    await world.replace()

    return MemoryGenerateResponse(
        generated_memory=generated_memory,
    ).dict()
