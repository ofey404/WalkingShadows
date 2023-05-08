import unittest

from testcontainers.mongodb import MongoDbContainer

MONGO_CONTAINER_VERSION = "mongo:6.0.5"


class TestCaseWithMongo(unittest.IsolatedAsyncioTestCase):
    mongo: MongoDbContainer

    @classmethod
    def setUpClass(cls):
        cls.mongo = MongoDbContainer(MONGO_CONTAINER_VERSION)
        cls.mongo.start()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.mongo.stop()
