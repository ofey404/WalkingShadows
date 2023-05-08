import unittest

import fastapi
from fastapi.testclient import TestClient
from libs import mongox
from libs.testx import TestCaseWithMongo
from services.world.api import world
from services.world.app import create_app
from services.world.settings import Settings, get_settings


class WorldAppTestCase(TestCaseWithMongo):
    app: fastapi.FastAPI

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
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

    def run(
        self, result: unittest.result.TestResult | None = ...
    ) -> unittest.result.TestResult | None:
        with TestClient(self.app) as client:
            self.client: TestClient = client
            super().run(result)
