import unittest
from __init__ import app


class TestServer(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_random_number(self):
        response = self.app.get("/note")
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json)
        self.assertEqual("this is my message", response.json["message"])


if __name__ == "__main__":
    unittest.main()
