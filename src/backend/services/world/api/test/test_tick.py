import unittest

import httpx
from services.world.api import tick
from services.world.api.tick import TickRequest
from services.world.server import create_app


class TestTick(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.client = httpx.AsyncClient(
            app=create_app(
                tick.router,
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
