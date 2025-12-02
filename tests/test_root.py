import httpx
import pytest

pytestmark = pytest.mark.anyio("asyncio")


async def test_root_redirects_to_docs(async_client: httpx.AsyncClient) -> None:
    response = await async_client.get("/", follow_redirects=False)
    assert response.status_code in (302, 307)
    assert response.headers.get("location") == "/docs"


async def test_head_root_redirects_to_docs(async_client: httpx.AsyncClient) -> None:
    response = await async_client.head("/", follow_redirects=False)
    assert response.status_code in (302, 307)
    assert response.headers.get("location") == "/docs"
