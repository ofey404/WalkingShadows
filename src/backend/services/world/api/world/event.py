from fastapi import APIRouter

router = APIRouter()


@router.post(
    "/api/world/{world}/event",
)
async def handle_event(
    world: str,
) -> dict:
    return {}
