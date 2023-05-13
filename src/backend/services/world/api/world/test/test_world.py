from pathlib import Path

from services.world.api.world.crud import WorldCreateRequest, WorldGetRequest
from services.world.api.world.memory import MemoryGenerateRequest
from services.world.internal import utils
from services.world.internal.llm import MockOpenAI, get_llm


class TestWorld(utils.WorldAppTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.app.dependency_overrides[get_llm] = lambda: MockOpenAI(
            # to_file=Path(__file__).parent / "test_world.json"
            from_file=Path(__file__).parent
            / "test_world.json"
        )

    async def test_world_lifecycle(self):
        world_name = "test_world_name"
        description = "test description"

        code, _ = self.postPydantic(
            f"/api/world/{world_name}/create",
            WorldCreateRequest(description=description),
        )

        self.assertEqual(code, 200)

        # post same again
        code, _ = self.postPydantic(
            f"/api/world/{world_name}/create",
            WorldCreateRequest(description=description),
        )
        self.assertEqual(code, 400)

        # get this world
        code, body = self.postPydantic(
            f"/api/world/{world_name}/get",
            WorldGetRequest(),
        )
        self.assertEqual(code, 200)
        self.assertEqual(body["description"], description)

        # generate content
        code, body = self.postPydantic(
            f"/api/world/{world_name}/memory/generate",
            MemoryGenerateRequest(),
        )
        self.assertEqual(code, 200)
        generated_content = body["generated_memory"]

        # get world again
        code, body = self.postPydantic(
            f"/api/world/{world_name}/get",
            WorldGetRequest(),
        )
        self.assertEqual(code, 200)
        self.assertEqual(
            body["memory"][0]["page_content"],
            generated_content,
        )
