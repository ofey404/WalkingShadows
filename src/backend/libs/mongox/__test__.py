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

            # test update
            d2 = await TestDocument.find_one({"content": "test"})
            self.assertIsNotNone(d2)
            self.assertEqual(d2.content, "test")

            d2_id = d2.id
            modified_content = "test update"
            d2.content = modified_content
            await d2.replace()

            # check updated content
            d3 = await TestDocument.get(d2_id)
            self.assertIsNotNone(d3)
            self.assertEqual(d3.content, modified_content)

            # document not exist
            d4 = await TestDocument.find_one({"content": "not exist"})
            self.assertIsNone(d4)


if __name__ == "__main__":
    unittest.main()
