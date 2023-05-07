from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class EventGetRequest(BaseModel):
    ...


class EventGetResponse(BaseModel):
    ...


@router.post(
    "/api/world/{world}/event/get",
    responses={},
)
async def handle_event_get(
    world: str,
    body: EventGetRequest,
) -> dict:
    return {}
