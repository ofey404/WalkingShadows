import unittest

from logic import NoteRequest, NoteResponse, note
from schema.test import fake_service_context


class TestNote(unittest.TestCase):
    def test_logic(self):
        message = "message"
        response = NoteResponse(message=message)
        ctx = fake_service_context(llm_responses=[message])
        ans = note(ctx, NoteRequest(message="hello"))
        self.assertEqual(ans, response)
