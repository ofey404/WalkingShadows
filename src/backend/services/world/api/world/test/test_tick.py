import unittest

import httpx
from services.world.api import world
from services.world.api.world.tick import TickRequest
from services.world.server import create_app


class TestTick(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.client = httpx.AsyncClient(
            app=create_app(
                world.tick_router,
            ),
            base_url="http://app",
        )

    async def test_tick(self):
        world = "test_world_name"
        resp = await self.client.post(
            f"/api/world/{world}/tick",
            json=TickRequest(now="now").dict(),
        )

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), {})
