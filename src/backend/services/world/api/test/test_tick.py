import httpx
import pytest
from services.world.api.tick import TickRequest


@pytest.mark.asyncio
async def test_tick(client: httpx.AsyncClient) -> None:
    world = "test_world_name"
    resp = await client.post(
        f"/api/world/{world}/tick",
        json=TickRequest(now="now").dict(),
    )
    assert resp.status_code == 200
    assert resp.json() == {}
