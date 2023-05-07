from fastapi import APIRouter
from loguru import logger
from pydantic import BaseModel

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
