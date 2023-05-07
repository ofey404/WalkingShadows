import httpx
import pytest_asyncio
from services.world.api import tick
from services.world.server import create_app


@pytest_asyncio.fixture(scope="session")
async def client() -> httpx.AsyncClient:
    async with httpx.AsyncClient(
        app=create_app(
            tick.router,
        ),
        base_url="http://app",
    ) as c:
        # init

        yield c

        # clean up
