import unittest

from __init__ import create_app
from langchain.llms.fake import FakeListLLM
from schema import Config, Secret, ServiceContext


def fake_service_context() -> ServiceContext:
    return ServiceContext(
        config=Config(
            port=5000,
            debug=True,
        ),
        secret=Secret(
            openai_api_key="",
        ),
        llm=FakeListLLM(
            responses=[
                "Action: Python REPL\nAction Input: print(2 + 2)",
                "Final Answer: 4",
            ]
        ),
    )


class TestServer(unittest.TestCase):
    def setUp(self):
        self.ctx = fake_service_context()
        self.app = create_app(self.ctx).app.test_client()

    def test_api_note(self):
        response = self.app.post("/api/note", json={"message": "message"})
        self.assertEqual(response.status_code, 200, str(response.data))
        self.assertIn("message", response.json, str(response.data))
        self.assertEqual(
            "message received: message, port: 5000",
            response.json["message"],
            str(response.data),
        )


if __name__ == "__main__":
    unittest.main()
