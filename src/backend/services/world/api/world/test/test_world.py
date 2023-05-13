from services.world.api.world.crud import WorldCreateRequest, WorldGetRequest
from services.world.api.world.memory import MemoryGenerateRequest
from services.world.internal import utils


class TestWorld(utils.WorldAppTestCase):
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

        code, body = self.postPydantic(
            f"/api/world/{world_name}/memory/generate",
            MemoryGenerateRequest(),
        )
        self.assertEqual(code, 200)
        print(f"body: {body}")
