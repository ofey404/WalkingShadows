import unittest

from beanie import init_beanie
from libs.testx import MONGO_CONTAINER_VERSION
from motor.motor_asyncio import AsyncIOMotorClient
from services.world.internal.models.character import Character
from testcontainers.mongodb import MongoDbContainer


class TestCharacter(unittest.IsolatedAsyncioTestCase):
    async def test_create(self):
        with MongoDbContainer(MONGO_CONTAINER_VERSION) as mongo:
            url = mongo.get_connection_url()
            client = AsyncIOMotorClient(url)
            await init_beanie(
                database=client.test_database,
                document_models=[
                    Character,
                ],
            )
            c = Character(
                akasha_id="akasha_id",
                property={"key": "value"},
                memory=[],
                event=[],
            )
            await c.insert()
            c2 = await Character.find_one({"akasha_id": "akasha_id"})
            print(f"c2: {c2}")
            self.assertEqual(c2.property["key"], "value")
