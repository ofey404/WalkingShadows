from libs import uvicornx
from services.world.api import tick
from services.world.server import create_app
from services.world.settings import get_settings

if __name__ == "__main__":
    s = get_settings()
    uvicornx.run(
        create_app(tick.router),
        s.uvicorn,
    )
