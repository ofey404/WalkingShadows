from services.world.api.world.crud import WorldCreateRequest, WorldGetRequest
from services.world.internal import utils


class TestCrud(utils.WorldAppTestCase):
    async def test_create(self):
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
