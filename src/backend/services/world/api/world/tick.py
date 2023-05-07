from fastapi import APIRouter, HTTPException, status
from libs import errx
from loguru import logger
from pydantic import BaseModel

router = APIRouter()


class TickRequest(BaseModel):
    now: str  # to enhance idempotency


class TickResponse(BaseModel):
    ...


exp_now_must_be_now = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="now must be 'now'",
)


@router.post(
    "/api/world/{world}/tick",
    response_model=TickResponse,
    responses=errx.add_exception_to_openapi(
        exp_now_must_be_now,
    ),
)
async def handle_tick(
    world: str,
    body: TickRequest,
) -> dict:
    logger.info(f"world: {world}")

    if body.now != "now":
        raise exp_now_must_be_now
    return {}
