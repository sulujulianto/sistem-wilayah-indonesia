import httpx
import pytest

pytestmark = pytest.mark.anyio("asyncio")


async def test_provinces_list_has_minimum_items(async_client: httpx.AsyncClient) -> None:
    response = await async_client.get("/v1/provinces")
    assert response.status_code == 200
    data = response.json()
    assert data["count"] >= 38
    assert len(data["items"]) <= data["count"]
    assert data["limit"] == 20


async def test_province_alias_resolution(async_client: httpx.AsyncClient) -> None:
    response = await async_client.get("/v1/provinces/jabar")
    assert response.status_code == 200
    body = response.json()
    assert body["name"] == "Jawa Barat"


async def test_province_not_found(async_client: httpx.AsyncClient) -> None:
    response = await async_client.get("/v1/provinces/does-not-exist")
    assert response.status_code == 404
    body = response.json()
    assert body["error"]["code"] == "province_not_found"


async def test_province_ambiguous_query_returns_conflict(
    async_client: httpx.AsyncClient,
) -> None:
    response = await async_client.get("/v1/provinces/papua")
    assert response.status_code == 409
    body = response.json()
    assert body["error"]["code"] == "ambiguous_province"
    assert "candidates" in body["error"].get("details", {})
    assert len(body["error"]["details"]["candidates"]) > 1
