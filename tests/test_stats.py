import httpx
import pytest

pytestmark = pytest.mark.anyio("asyncio")


async def test_stats_totals(async_client: httpx.AsyncClient) -> None:
    response = await async_client.get("/v1/stats")
    assert response.status_code == 200
    data = response.json()
    assert data["total_provinsi"] == 38
    assert data["total_kabupaten"] == 416
    assert data["total_kota"] == 98
    assert data["total_wilayah"] == 514
