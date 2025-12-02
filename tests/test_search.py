import httpx
import pytest

pytestmark = pytest.mark.anyio("asyncio")


async def test_search_allows_short_query(async_client: httpx.AsyncClient) -> None:
    response = await async_client.get("/v1/search", params={"q": "a"})
    assert response.status_code == 200
    data = response.json()
    assert data["query"] == "a"


async def test_search_type_filter(async_client: httpx.AsyncClient) -> None:
    response_kab = await async_client.get(
        "/v1/search", params={"q": "bima", "type": "kabupaten"}
    )
    assert response_kab.status_code == 200
    data_kab = response_kab.json()
    assert data_kab["count"] >= 1
    assert all(item["type"] == "kabupaten" for item in data_kab["results"])

    response_kota = await async_client.get(
        "/v1/search", params={"q": "bima", "type": "kota"}
    )
    assert response_kota.status_code == 200
    data_kota = response_kota.json()
    assert data_kota["count"] >= 1
    assert all(item["type"] == "kota" for item in data_kota["results"])
