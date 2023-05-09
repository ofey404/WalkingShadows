from fastapi import APIRouter
from loguru import logger
from pydantic import BaseModel

router = APIRouter()


class FactGetRequest(BaseModel):
    id: str


class FactGetResponse(BaseModel):
    id: str
    ts: int
    content: str


@router.post(
    "/api/world/{world}/event/get",
    response_model=FactGetResponse,
)
async def handle_event_get(
    world: str,
    body: FactGetRequest,
) -> dict:
    logger.info(f"world: {world}")

    return {"id": body.id, "ts": 0, "content": "test content"}
