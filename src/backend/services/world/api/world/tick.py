from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from libs import errx
from loguru import logger
from pydantic import BaseModel
from services.world.settings import Settings, get_settings

router = APIRouter()


class TickRequest(BaseModel):
    now: str  # to enhance idempotency


class TickResponse(BaseModel):
    ...


def get_sub_dependency(settings: Annotated[Settings, Depends(get_settings)]) -> dict:
    return settings.dict()


def get_multiple_dependency(
    body: TickRequest, settings: Annotated[Settings, Depends(get_settings)]
):
    return body, settings.dict()


@router.post(
    "/api/world/{world}/tick",
    response_model=TickResponse,
    responses=errx.add_to_openapi_doc(
        {
            status.HTTP_400_BAD_REQUEST: "now must be 'now'",
        }
    ),
)
async def handle_tick(
    world: str,
    body: TickRequest,
    settings: Annotated[Settings, Depends(get_settings)],
    sub_dependency: Annotated[dict, Depends(get_sub_dependency)],
    multiple_dependency: Annotated[tuple, Depends(get_multiple_dependency)],
) -> dict:
    logger.info(f"world: {world}")
    logger.info(f"settings: {settings.dict()}")
    logger.info(f"sub_dependency: {sub_dependency}")
    logger.info(f"multiple_dependency: {multiple_dependency}")

    if body.now != "now":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="now must be 'now'",
        )

    return {}
