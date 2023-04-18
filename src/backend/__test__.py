import unittest

from __init__ import create_app
from schema.test import fake_service_context


class TestServer(unittest.TestCase):
    def setUp(self):
        self.response = "Test response"
        self.ctx = fake_service_context([self.response])
        self.app = create_app(self.ctx).app.test_client()

    def test_api_note(self):
        response = self.app.post("/api/note", json={"message": "message"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json)
        self.assertEqual(
            self.response,
            response.json["message"],
        )

        # Empty llm_responses would cause list index out of range error
        self.ctx = fake_service_context([])
        response = self.app.post("/api/note", json={"message": "message"})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(
            "list index out of range",
            response.json["message"],
        )


if __name__ == "__main__":
    unittest.main()
