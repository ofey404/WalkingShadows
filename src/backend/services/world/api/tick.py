from fastapi import APIRouter, HTTPException, status
from loguru import logger
from pydantic import BaseModel

router = APIRouter()


class TickRequest(BaseModel):
    now: str  # to enhance idempotency


class TickResponse(BaseModel):
    ...


@router.post(
    "/api/world/{world}/tick",
    response_model=TickResponse,
)
async def handle_tick(
    world: str,
    body: TickRequest,
) -> dict:
    logger.info(f"world: {world}")

    if body.now != "now":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="now must be 'now'",
        )
    return {}
