import random
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException, status
from libs import errx
from loguru import logger
from pydantic import BaseModel
from services.world.internal.models.world import World

router = APIRouter()


class WorldCreateRequest(BaseModel):
    overwrite: bool = False


class WorldCreateResponse(BaseModel):
    event_id: int


@router.post(
    "/api/world/{world_name}/create",
    response_model=WorldCreateResponse,
    responses=errx.add_to_openapi_doc(
        {
            status.HTTP_400_BAD_REQUEST: "world already exists",
        }
    ),
)
async def handle_create(
    world_name: str,
    body: WorldCreateRequest,
) -> dict:
    if not body.overwrite:
        exists = await World.find_one({"name": world_name}).exists()
        if exists:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"world {world_name} already exists",
            )

    event_id = random.randint()
    world = World(
        event_id=event_id,
        name=world_name,
    )
    await world.insert()

    return WorldCreateResponse(
        event_id=event_id,
    ).dict()
