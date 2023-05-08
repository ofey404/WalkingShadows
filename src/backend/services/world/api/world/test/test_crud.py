from services.world.api.world.crud import WorldCreateRequest
from services.world.internal import utils


class TestCrud(utils.WorldAppTestCase):
    async def test_create(self):
        world_name = "test_world_name"
        resp = self.client.post(
            f"/api/world/{world_name}/create",
            json=WorldCreateRequest().dict(),
        )

        self.assertEqual(resp.status_code, 200)

        # post same again
        resp = self.client.post(
            f"/api/world/{world_name}/create",
            json=WorldCreateRequest().dict(),
        )
        self.assertEqual(resp.status_code, 400)
