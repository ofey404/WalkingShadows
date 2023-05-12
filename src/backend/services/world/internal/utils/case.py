import json
import unittest
from typing import Tuple

import fastapi
from fastapi.testclient import TestClient
from libs import mongox
from libs.testx import TestCaseWithMongo
from pydantic import BaseModel
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

    def postPydantic(self, url, data: BaseModel) -> Tuple[int, dict]:
        resp = self.client.post(url, json=data.dict())

        data_dict = json.loads(resp.content)
        return resp.status_code, data_dict
