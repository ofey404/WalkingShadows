import random

from fastapi import APIRouter, Depends, HTTPException, status
from libs import errx
from loguru import logger
from pydantic import BaseModel
from services.world.internal.models.world import World, check_world_exist, get_world

router = APIRouter()


class WorldCreateRequest(BaseModel):
    description: str
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
    world_exists: bool = Depends(check_world_exist),
) -> dict:
    if not body.overwrite and world_exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"world {world_name} already exists",
        )

    event_id = random.randint(0, 100)
    world = World(
        event_id=event_id,
        name=world_name,
        description=body.description,
    )
    await world.insert()

    return WorldCreateResponse(
        event_id=event_id,
    ).dict()


class WorldGetRequest(BaseModel):
    ...


class WorldGetResponse(World):
    ...


@router.post(
    "/api/world/{world_name}/get",
    response_model=WorldGetResponse,
    responses=errx.add_to_openapi_doc(
        {
            status.HTTP_400_BAD_REQUEST: "world not found",
        }
    ),
)
async def handle_get(
    world_name: str,
    body: WorldGetRequest,
    world=Depends(get_world),
) -> dict:
    return world.dict()
