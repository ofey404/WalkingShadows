import unittest

from fastapi.testclient import TestClient
from libs import mongox
from libs.testx import MONGO_CONTAINER_VERSION
from services.world.api import world
from services.world.api.world.crud import WorldCreateRequest
from services.world.app import create_app
from services.world.settings import Settings, get_settings
from testcontainers.mongodb import MongoDbContainer


class TestCrud(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        self.mongo = MongoDbContainer(MONGO_CONTAINER_VERSION)
        self.mongo.start()

        s = Settings(
            mongo=mongox.Settings(
                url=self.mongo.get_connection_url(),
            )
        )

        self.app = create_app(
            world.crud_router,
            settings_override=s,
        )
        self.app.dependency_overrides[get_settings] = lambda: s

    async def asyncTearDown(self) -> None:
        self.mongo.stop()

    async def test_create(self):
        with TestClient(self.app) as client:
            world_name = "test_world_name"
            resp = client.post(
                f"/api/world/{world_name}/create",
                json=WorldCreateRequest().dict(),
            )

            self.assertEqual(resp.status_code, 200)

            # post same again
            resp = client.post(
                f"/api/world/{world_name}/create",
                json=WorldCreateRequest().dict(),
            )
            self.assertEqual(resp.status_code, 400)
