from services.world.api.world.crud import router as crud_router
from services.world.api.world.event import router as event_router
from services.world.api.world.memory import router as memory_router
from services.world.api.world.tick import router as tick_router

__all__ = [
    tick_router,
    event_router,
    memory_router,
    crud_router,
]
