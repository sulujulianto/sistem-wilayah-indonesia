import httpx
import pytest

pytestmark = pytest.mark.anyio("asyncio")


async def test_health_ok(async_client: httpx.AsyncClient) -> None:
    response = await async_client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
