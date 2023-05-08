import unittest

import fastapi
from fastapi.testclient import TestClient
from libs import mongox
from libs.testx import MONGO_CONTAINER_VERSION
from services.world.api import world
from services.world.api.world.crud import WorldCreateRequest
from services.world.app import create_app
from services.world.settings import Settings, get_settings
from testcontainers.mongodb import MongoDbContainer


class TestCrud(unittest.IsolatedAsyncioTestCase):
    mongo: MongoDbContainer = None
    app: fastapi.FastAPI = None

    @classmethod
    def setUpClass(cls):
        cls.mongo = MongoDbContainer(MONGO_CONTAINER_VERSION)
        cls.mongo.start()

        s = Settings(
            mongo=mongox.Settings(
                url=cls.mongo.get_connection_url(),
            )
        )

        cls.app = create_app(
            world.crud_router,
            settings_override=s,
        )
        cls.app.dependency_overrides[get_settings] = lambda: s

    @classmethod
    def tearDownClass(cls) -> None:
        cls.mongo.stop()

    def run(
        self, result: unittest.result.TestResult | None = ...
    ) -> unittest.result.TestResult | None:
        with TestClient(self.app) as client:
            self.client = client
            super().run(result)

    async def test_create(self):
        world_name = "test_world_name"
        resp = self.client.post(
            f"/api/world/{world_name}/create",
            json=WorldCreateRequest().dict(),
        )

        self.assertEqual(resp.status_code, 200)

        # post same again
        resp = self.client.post(
            f"/api/world/{world_name}/create",
            json=WorldCreateRequest().dict(),
        )
        self.assertEqual(resp.status_code, 400)
