import unittest

from beanie import Document
from libs import mongox
from libs.testx import MONGO_CONTAINER_VERSION
from testcontainers.mongodb import MongoDbContainer


class TestDocument(Document):
    content: str


class TestMongo(unittest.IsolatedAsyncioTestCase):
    async def test_insert(self):
        with MongoDbContainer(MONGO_CONTAINER_VERSION) as mongo:
            await mongox.init(
                settings=mongox.Settings(url=mongo.get_connection_url()),
                document_models=[
                    TestDocument,
                ],
            )
            d = TestDocument(content="test")
            await d.insert()
            d2 = await TestDocument.find_one({"content": "test"})
            self.assertIsNotNone(d2)
            self.assertEqual(d2.content, "test")

            d3 = await TestDocument.find_one({"content": "not exist"})
            self.assertIsNone(d3)


if __name__ == "__main__":
    unittest.main()
