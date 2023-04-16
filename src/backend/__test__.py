import unittest
from __init__ import APP


class TestServer(unittest.TestCase):
    def setUp(self):
        self.app = APP.app.test_client()

    def test_api_note(self):
        response = self.app.post("/api/note", json={"message": "message"})
        self.assertEqual(response.status_code, 200, str(response.data))
        self.assertIn("message", response.json, str(response.data))
        self.assertEqual(
            "message received: message", response.json["message"], str(response.data)
        )


if __name__ == "__main__":
    unittest.main()
