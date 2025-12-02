import httpx
import pytest

pytestmark = pytest.mark.anyio("asyncio")


META_FIELDS = [
    "dataset_name",
    "dataset_version",
    "last_updated",
    "source_notes",
    "coverage",
    "computed_coverage",
]


async def test_meta_returns_metadata(async_client: httpx.AsyncClient) -> None:
    response = await async_client.get("/v1/meta")
    assert response.status_code == 200
    data = response.json()
    for field in META_FIELDS:
        assert field in data
    assert data["coverage"]["total_provinsi"] == 38
    assert data["computed_coverage"]["total_provinsi"] == 38
    assert data["coverage"]["total_kabupaten"] == data["computed_coverage"]["total_kabupaten"]
    assert data["coverage"]["total_kota"] == data["computed_coverage"]["total_kota"]
