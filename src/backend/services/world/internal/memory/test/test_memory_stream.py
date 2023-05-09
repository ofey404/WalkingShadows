import unittest

from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.redis import Redis
from libs.testx import REDIS_CONTAINER_VERSION
from redis import Redis as RedisClient
from testcontainers.redis import RedisContainer


class TestMemoryStream(unittest.TestCase):
    redis: RedisContainer
    vectorstore: Redis

    @classmethod
    def setUpClass(cls):
        cls.redis = RedisContainer(REDIS_CONTAINER_VERSION)
        cls.redis.start()

        ip = cls.redis.get_container_host_ip()
        port = cls.redis.get_exposed_port(cls.redis.port_to_expose)

        redis_url = f"redis://{ip}:{port}"
        cls.vectorstore = Redis.from_texts(
            texts=[
                "hello world",
            ],
            embedding=OpenAIEmbeddings(),
            redis_url=redis_url,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls.redis.stop()

    # def test_basic(self):
    #     ans = self.vectorstore.add_texts(["hello world"])
    #     print(ans)
