from libs import uvicornx
from services.world.api import world
from services.world.server import create_app
from services.world.settings import get_settings

if __name__ == "__main__":
    s = get_settings()
    uvicornx.run(
        create_app(
            world.tick_router,
            world.event_router,
            world.memory_router,
        ),
        s.uvicorn,
    )
