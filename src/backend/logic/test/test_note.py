import unittest

from logic import note
from schema.test import fake_service_context


class TestNote(unittest.TestCase):
    def test_logic(self):
        response = "Test Response"
        ctx = fake_service_context(llm_responses=[response])
        ans = note(ctx, "Hello, world!")
        self.assertEqual(ans, response)
