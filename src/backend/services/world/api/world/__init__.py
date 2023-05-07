from services.world.api.world.event import router as event_router
from services.world.api.world.tick import router as tick_router

__all__ = [
    tick_router,
    event_router,
]
